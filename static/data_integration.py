from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Example: Simulated wearable data from JSON
wearable_data = {
  "metrics": [
    {
      "date": "2024-11-20",
      "steps": 9200,
      "heart_rate": 73,
      "sleep_hours": 7.0,
      "hrv": 48,
      "active_minutes": 75
    },
    {
      "date": "2024-11-19",
      "steps": 8700,
      "heart_rate": 74,
      "sleep_hours": 6.8,
      "hrv": 46,
      "active_minutes": 68
    },
    {
      "date": "2024-11-18",
      "steps": 8000,
      "heart_rate": 76,
      "sleep_hours": 6.2,
      "hrv": 44,
      "active_minutes": 62
    },
    {
      "date": "2024-11-17",
      "steps": 8900,
      "heart_rate": 72,
      "sleep_hours": 7.3,
      "hrv": 49,
      "active_minutes": 78
    },
    {
      "date": "2024-11-16",
      "steps": 9500,
      "heart_rate": 71,
      "sleep_hours": 7.5,
      "hrv": 51,
      "active_minutes": 82
    },
    {
      "date": "2024-11-15",
      "steps": 8600,
      "heart_rate": 75,
      "sleep_hours": 6.4,
      "hrv": 45,
      "active_minutes": 67
    },
    {
      "date": "2024-11-14",
      "steps": 9100,
      "heart_rate": 72,
      "sleep_hours": 7.1,
      "hrv": 48,
      "active_minutes": 74
    },
    {
      "date": "2024-11-13",
      "steps": 8700,
      "heart_rate": 73,
      "sleep_hours": 6.7,
      "hrv": 47,
      "active_minutes": 70
    },
    {
      "date": "2024-11-12",
      "steps": 8800,
      "heart_rate": 74,
      "sleep_hours": 6.9,
      "hrv": 46,
      "active_minutes": 72
    },
    {
      "date": "2024-11-11",
      "steps": 9000,
      "heart_rate": 71,
      "sleep_hours": 7.4,
      "hrv": 50,
      "active_minutes": 79
    },
    {
      "date": "2024-11-10",
      "steps": 9400,
      "heart_rate": 72,
      "sleep_hours": 7.2,
      "hrv": 49,
      "active_minutes": 81
    },
    {
      "date": "2024-11-09",
      "steps": 8900,
      "heart_rate": 73,
      "sleep_hours": 6.8,
      "hrv": 48,
      "active_minutes": 69
    },
    {
      "date": "2024-11-08",
      "steps": 8700,
      "heart_rate": 74,
      "sleep_hours": 6.5,
      "hrv": 46,
      "active_minutes": 65
    },
    {
      "date": "2024-11-07",
      "steps": 8600,
      "heart_rate": 76,
      "sleep_hours": 6.3,
      "hrv": 45,
      "active_minutes": 64
    },
    {
      "date": "2024-11-06",
      "steps": 9200,
      "heart_rate": 71,
      "sleep_hours": 7.0,
      "hrv": 49,
      "active_minutes": 76
    },
    {
      "date": "2024-11-05",
      "steps": 9500,
      "heart_rate": 72,
      "sleep_hours": 7.3,
      "hrv": 51,
      "active_minutes": 80
    },
    {
      "date": "2024-11-04",
      "steps": 8800,
      "heart_rate": 74,
      "sleep_hours": 6.9,
      "hrv": 46,
      "active_minutes": 71
    },
    {
      "date": "2024-11-03",
      "steps": 8500,
      "heart_rate": 75,
      "sleep_hours": 6.6,
      "hrv": 45,
      "active_minutes": 66
    },
    {
      "date": "2024-11-02",
      "steps": 9000,
      "heart_rate": 73,
      "sleep_hours": 7.2,
      "hrv": 48,
      "active_minutes": 73
    },
    {
      "date": "2024-11-01",
      "steps": 8700,
      "heart_rate": 74,
      "sleep_hours": 6.8,
      "hrv": 47,
      "active_minutes": 68
    }
  ]
}




def normalize_data(data):
    """Normalize metrics using Min-Max scaling."""
    df = pd.DataFrame(data)
    metrics_to_normalize = ["steps", "heart_rate", "sleep_hours", "hrv"]
    for metric in metrics_to_normalize:
        min_val = df[metric].min()
        max_val = df[metric].max()
        df[f"{metric}_normalized"] = (df[metric] - min_val) / (max_val - min_val)
    return df.to_dict(orient="records")




@app.route('/')
def get_normalized_data():
    """Endpoint to get normalized wearable data."""
    normalized_data = normalize_data(wearable_data["metrics"])
    return jsonify(normalized_data)



if __name__ == "__main__":
    app.run(debug=True)
