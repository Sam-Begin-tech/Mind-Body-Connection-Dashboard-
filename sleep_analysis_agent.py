# import numpy as np
import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX

def sleepAnalysis(file_path):
    # Load the JSON file
    data = pd.read_json(file_path)
    
    # Flatten the nested structure
    df = pd.json_normalize(data['metrics'])
    df['date'] = pd.to_datetime(df['date'])
    
    # Fit the SARIMA model
    arima_model = SARIMAX(df['sleep_hours'], order=(1, 1, 1))
    arima_result = arima_model.fit()

    # Set the 'date' column as the index
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)

    last_date = df.index[0]

    # Generate forecast for the next 7 days
    forecast_dates = pd.date_range(start=last_date, periods=8, freq='D')[1:]  # Next 7 days
    forecast = arima_result.forecast(steps=7)

    # Combine dates and forecast into a DataFrame
    forecast_df = pd.DataFrame({'date': forecast_dates, 'predicted_sleep_hours': forecast})
    forecast_df.set_index('date', inplace=True)

    # Print the forecast DataFrame
    return forecast_df
