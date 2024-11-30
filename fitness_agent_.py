import joblib
import numpy as np

# Load the trained model
model = joblib.load('calorie_prediction.pkl')

def workout_suggestion(steps, active_minutes, predicted_calories):
    if steps < 8000 and active_minutes < 45:
        return "Increase your weekly activity by 10% to improve cardiovascular health."
    elif predicted_calories < 300:
        return "Consider increasing your active minutes or adding strength training."
    else:
        return "Great job! Keep up the good work and try adding variety to your workouts."
    

def predictCalorie(steps,active_minutes):
    try:
        
        # Predict calories burned using the trained model
        features = np.array([[steps, active_minutes]])
        predicted_calories = model.predict(features)[0]
        suggestion = workout_suggestion(steps, active_minutes, predicted_calories)
        response={
            'predicted_calories': predicted_calories,
            'suggestion': suggestion
        }

        # Return the prediction and suggestion
        return response

    except Exception as e:
        response={
            'predicted_calories': "No value",
            'suggestion': "Nill"
        }
        return response
    
response=predictCalorie(8000,40)
print(response)
