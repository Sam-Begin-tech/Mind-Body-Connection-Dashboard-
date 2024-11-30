# AI Agents for Health & Well-being

This repository contains a set of AI-driven agents designed to provide health and well-being suggestions based on various data inputs. These agents include a calorie prediction agent, a sentiment analysis agent for journal entries, and a sleep analysis agent using ARIMA forecasting.

## Agents Overview

### 1. **Calorie Prediction Agent**
This agent predicts the number of calories burned based on user activity (steps and active minutes) and provides workout suggestions based on the predicted calories.

#### Features:
- **Predicts calories burned** based on steps and active minutes using a trained model.
- **Provides workout suggestions** based on the predicted calories and activity level.

## Sentiment Analysis & Suggestions for Journal Entries
** This agent performs sentiment analysis on journal entries and provides emotional suggestions based on the sentiment (positive, negative, or neutral). It generates a detailed analysis and an overall summary of the user's emotional state.**

### Features:
- Analyzes sentiment (positive, negative, or neutral) of journal entries.
- Provides emotional suggestions based on sentiment.
- Summarizes the overall emotional state and gives advice.
### Requirements:
- langchain for chaining multiple steps and interacting with LLM models.
- OpenAI for sentiment analysis and summarization.
- json for handling and formatting responses.


## Sleep Analysis Agent with ARIMA Forecasting
**This agent uses the ARIMA model to forecast sleep hours for the next 7 days based on historical data and provides sleep suggestions based on average sleep hours.**

Features:
Forecasts sleep hours for the next 7 days using ARIMA.
Generates sleep suggestions based on the predicted average sleep hours.
  
## Installation
To use these agents, clone this repository and install the required dependencies.

```bash
  
git clone https://github.com/Sam-Begin-tech/Mind-Body-Connection-Dashboard-.git

  cd Mind-Body-Connection-Dashboard-
  pip install -r requirements.txt
