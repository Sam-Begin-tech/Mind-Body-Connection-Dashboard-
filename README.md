# Mind-Body-Connection-Dashboard-
Mind-Body Connection Dashboard


---
This project is a web-based health and wellness dashboard that provides users with insights into their physical activity, sleep patterns, and emotional well-being. It integrates AI models for calorie prediction, sleep forecasting, and journal sentiment analysis to offer personalized suggestions for improved physical and emotional health.

## **Features**

1. **Sentiment Analysis on Journal Entries**
   - Analyzes users' journal entries for emotional sentiment (positive, negative, neutral).
   - Provides actionable suggestions for improving emotional well-being.

2. **Calorie Prediction**
   - Uses a trained regression model to predict calories burned based on the user's steps and active minutes.
   - Suggests fitness improvements based on activity data.

3. **Sleep Analysis**
   - Forecasts the user's sleep duration for the next seven days using a SARIMA model.
   - Combines sleep insights with calorie and sentiment data to generate holistic feedback.

4. **Personalized Feedback**
   - Correlates data from sentiment analysis, calorie predictions, and sleep forecasts to provide customized health and wellness recommendations.

---

## **Technologies Used**

- **Backend:** Python (Flask Framework)
- **AI Models:** Regression Model, SARIMA for time series forecasting, LangChain for text-based insights, OpenAI LLM
- **Frontend:** HTML Templates (Jinja2)
- **Data Storage:** JSON for user metrics and mock journal entries

---

## **Setup and Usage**

### **Prerequisites**

1. Install Python (>=3.7).
2. Install required Python libraries:


3. Ensure the following files are present:
   - `calorie_prediction.pkl`: Pre-trained regression model for calorie prediction.
   - `static/data.json`: User data file with metrics.
   - `static/mock_journal_data.json`: Mock journal data for analysis.
   - `templates/dashboard.html`: Frontend template for displaying results.

### **Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/Sam-Begin-tech/Mind-Body-Connection-Dashboard-.git
   cd Mind-Body-Connection-Dashboard-
   pip install requirements.txt
   ```

2. Place the required files (`data.json`, `mock_journal_data.json`, and `calorie_prediction.pkl`) in the specified directories.

3. Start the Flask server:
   ```bash
   python app.py
   ```

4. Open a browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

---

## **Project Structure**

```
├── app.py                            # Flask app to serve the dashboard
├── sentiment_analysis_agent.py       # Journal sentiment analysis logic
├── fitness_agent.py                  # Calorie prediction and fitness suggestions
├── sleep_analysis_agent.py           # Sleep forecasting using SARIMA
├── static/
│   ├── data.json                     # User data file (metrics)
│   ├── mock_journal_data.json        # Mock journal entries
├── templates/
│   ├── dashboard.html                # HTML template for the dashboard
```

---

## **AI Agent Details**

### **1. Sentiment Analysis (JournalAnalyzer)**

- Uses LangChain and OpenAI's GPT to analyze journal entries for emotional sentiment and provides actionable suggestions.
- **Chains Used:**
  - **Sentiment Analysis Chain:** Analyzes individual entries for sentiment and suggestions.
  - **Summary Chain:** Aggregates results into a holistic emotional summary.

### **2. Calorie Prediction (Fitness Agent)**

- A regression model (`calorie_prediction.pkl`) predicts calories burned based on:
  - Steps
  - Active minutes
- Provides tailored suggestions for fitness improvements.

### **3. Sleep Analysis (Sleep Agent)**

- Implements a SARIMA model to forecast sleep hours for the next 7 days.
- Helps users plan better sleep routines and correlates sleep data with emotional and fitness metrics.

---

## **How It Works**

1. **Input Data:** The application uses user metrics from `data.json` and journal entries from `mock_journal_data.json`.
2. **AI Predictions:**
   - Predicts calories burned using the regression model.
   - Forecasts sleep hours using SARIMA.
   - Analyzes journal entries for sentiment and emotional insights.
3. **Dashboard:** Results are displayed on a web dashboard with actionable feedback.

---

