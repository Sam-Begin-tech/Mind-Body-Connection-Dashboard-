# Fitness & sentiment Analysis Flask Application

This repository contains a Flask application designed to analyze user fitness data, sleep patterns, and journal entries. It combines predictions, summaries, and insights from multiple AI agents into a unified API response.

---

## 🚀 Features

- **Calorie Prediction**: Uses regression models to estimate calories burned based on steps and active minutes.
- **Sleep Analysis**: Generates sleep pattern forecasts using  `Time series SARIMA` model.
- **Journal Sentiment Analysis**: Analyzes user journal entries for emotional summaries using `OpenAI LLM`.
- **Integrated Feedback**: Combines calorie predictions, sleep forecasts, and journal analysis into comprehensive feedback.
- **API Endpoint**: A single endpoint that processes and returns a response with all insights.

---

## 🛠️ Technologies Used

- **Flask**: Backend framework for handling HTTP requests and responses.
- **Pandas**: For data manipulation and analysis.
- **JSON**: Used to handle and process user and mock data.
- **Custom Modules**:
  - `JournalAnalyzer` for journal sentiment analysis.
  - `predictCalorie` for calorie prediction.
  - `sleepAnalysis` for sleep pattern forecasting.

---

## 🗂️ File Structure

├── app.py # Main Flask application
├── static/ 
    │ 
    ├── data.json # User fitness data 
    │ 
    ├── mock_journal_data.json 
├── sentiment_analysis_agent.py 
├── fitness_agent.py 
├── sleep_analysis_agent.py 
├── templates/ 
└── README.md 



---

## 🔧 How to Run Locally

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/repo-name.git
   cd repo-name

   pip install -r requirements.txt
   python app.py



![Output Screenshot](assets/All agents providing holistic recommendations.png "Screenshot of the output")




  


