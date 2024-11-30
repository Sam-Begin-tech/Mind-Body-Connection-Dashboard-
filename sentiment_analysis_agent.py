from langchain.chains import SimpleSequentialChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
import json

class JournalAnalyzer:
    def __init__(self, llm=None):
        self.llm = llm or OpenAI(temperature=0)  

        # Define Prompts
        self.sentiment_prompt = PromptTemplate(
            input_variables=["entry"],
            template=(
                "Analyze the following journal entry for sentiment (positive, negative, or neutral) "
                "and provide an emotional suggestion based on the sentiment:\n\n"
                "Journal Entry: {entry}\n\n"
                "Response should be JSON with keys 'sentiment' and 'suggestion'."
            ),
        )

        self.summary_prompt = PromptTemplate(
            input_variables=["results"],
            template=(
                "Here are the detailed sentiment results for a set of journal entries:\n"
                "{results}\n\n"
                "Summarize the overall emotional state, providing percentages for positive, negative, "
                "and neutral sentiments, and any overarching advice for the user. which helps for physical and emotional well being"
            ),
        )
        self.combined_feedback_prompt = PromptTemplate(
            input_variables=["predicted_calories", "emotional_summary", "forecast_df"],
            template=(
                "Here is a summary of the user's emotional state, predicted calories burned, "
                "and the forecasted sleep duration for the next 7 days:\n\n"
                "Emotional Summary:\n{emotional_summary}\n\n"
                "Predicted Calories Burned:\n{predicted_calories}\n\n"
                "Forecasted Sleep Data:\n{forecast_df}\n\n"
                "Correlate these insights (e.g., poor sleep and high stress levels may impact fitness performance) "
                "and generate combined feedback for the user.\n"
                "Example Feedback: 'Your sleep quality and HRV have been low this week, and your journal entries reflect stress. "
                "Consider reducing workout intensity and practicing mindfulness.'"
            ),
        )   


    def sentiment_analysis_chain(self, journal_data):
        results = []
        for entry in journal_data["journal_entries"]:
            prompt = self.sentiment_prompt.format(entry=entry["entry"])
            response = self.llm(prompt)
            response_json = json.loads(response)  # Ensure JSON output
            results.append({
                "date": entry["date"],
                "entry": entry["entry"],
                "sentiment": response_json.get("sentiment", "neutral"),
                "suggestion": response_json.get("suggestion", "Keep on your day!")
            })
        return results

    def generate_summary_chain(self, results):
        formatted_results = json.dumps(results, indent=2)
        prompt = self.summary_prompt.format(results=formatted_results)
        response = self.llm(prompt)
        return response
    

    def generate_combined_feedback(self, predicted_calories, emotional_summary, forecast_df):
        # Safely extract predicted calories
        predicted_calories_str = str(predicted_calories.get("predicted_calories", "N/A"))
        # Parse forecast_df if it's a string
        if isinstance(forecast_df, str):
            try:
                forecast_df = json.loads(forecast_df)  # Convert JSON string to Python object
            except json.JSONDecodeError as e:
                raise ValueError(f"Invalid JSON format for forecast_df: {e}")

        # Validate forecast_df structure
        if not isinstance(forecast_df, dict) or "index" not in forecast_df or "data" not in forecast_df:
            raise ValueError("forecast_df must be a dictionary with 'index' and 'data' keys.")

        # Format forecasted sleep data
        try:
            forecasted_sleep_data = "\n".join(
                f"Date: {date}, Predicted Sleep: {sleep[0]:.2f} hours"
                for date, sleep in zip(forecast_df["index"], forecast_df["data"])
            )
        except (KeyError, TypeError, IndexError) as e:
            raise ValueError(f"Error processing forecast_df: {e}")

        # Generate the prompt
        prompt = self.combined_feedback_prompt.format(
            predicted_calories=predicted_calories_str,
            emotional_summary=emotional_summary,
            forecast_df=forecasted_sleep_data,
        )

        # Get response from LLM
        response = self.llm(prompt)
    
        return response

    def analyze_journals_with_chains(self, journal_data):
        # Step 1: Analyze sentiment and suggestions
        detailed_results = self.sentiment_analysis_chain(journal_data)
        
        # Step 2: Generate overall summary
        overall_summary = self.generate_summary_chain(detailed_results)
        
        # Combine outputs
        return {
            "detailed_results": detailed_results,
            "summary": overall_summary
        }
