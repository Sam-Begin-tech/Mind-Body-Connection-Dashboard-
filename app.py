from flask import Flask, request, jsonify, render_template
from sentiment_analysis_agent import JournalAnalyzer 
from fitness_agent import predictCalorie
from sleep_analysis_agent import sleepAnalysis
import json
import pandas as pd
# Initialize the Flask application
app = Flask(__name__)


# Define a route for predictions
@app.route('/')
def predict():
    try:
        file_path = './static/data.json'

        # Load mock journal data from the JSON file
        with open('./static/mock_journal_data.json', 'r') as file:
            mock_journal_data = json.load(file)
        with open('./static/data.json', 'r') as file:
            userdata = json.load(file)

            
     

            

        data = pd.read_json(file_path)
     
 

        # Flatten the nested structure
        df = pd.json_normalize(data['metrics'])
      
        # call the regression model
        calories=predictCalorie(df['steps'][0],df['active_minutes'][0])
        

        # Call the function to generate forecast
        forecast_df = sleepAnalysis(file_path)
        # return jsonify(forecast_df)
        journal_analyzer = JournalAnalyzer()

        # Analyze the mock data
        output = journal_analyzer.analyze_journals_with_chains(mock_journal_data)
      
        # Access the overall summary
        summary = output["summary"]
        print("forecast_json")
        forecast_json = forecast_df.to_json(orient='split', date_format='iso')


        forecast_json_string = json.loads(forecast_json)

        output = journal_analyzer.generate_combined_feedback(calories, summary,forecast_json)
        print(type(output))
        # overall_summary = output.replace("\n", " ").strip()
        # overall_summary = output["summary"]
        
        return render_template('dashboard.html', 
                           predicted_calories=calories,
                           emotional_summary=summary,
                           forecast_df=forecast_json,
                           overall_summary=output,
                           forecasted_sleep_data=forecast_json_string,
                           user_data=userdata['metrics']
                           
                           )



    except Exception as e:
        return jsonify({'error': str(e)}), 400
    





# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
