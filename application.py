import joblib
import numpy as np #We need to send inputs in the model by creating an array of required parameters thats why we use numpy
from config.paths_config import MODEL_OUTPUT_PATH
from flask import Flask, render_template, request

app = Flask(__name__) # Initialize flask app

loaded_model = joblib.load(MODEL_OUTPUT_PATH)

@app.route('/', methods = ['GET', 'POST'])

def index():
    if request.method=='POST':

        lead_time = int(request.form["lead_time"])
        no_of_special_request = int(request.form["no_of_special_request"])
        avg_price_per_room = float(request.form["avg_price_per_room"])
        arrival_month = int(request.form["arrival_month"])
        arrival_date = int(request.form["arrival_date"])

        market_segment_type = int(request.form["market_segment_type"])
        no_of_week_nights = int(request.form["no_of_week_nights"])
        no_of_weekend_nights = int(request.form["no_of_weekend_nights"])

        type_of_meal_plan = int(request.form["type_of_meal_plan"])
        room_type_reserved = int(request.form["room_type_reserved"])


        features = np.array([[lead_time,no_of_special_request,avg_price_per_room,arrival_month,arrival_date,market_segment_type,no_of_week_nights,no_of_weekend_nights,type_of_meal_plan,room_type_reserved]])

        print("🚀 Input features:", features)
        prediction = loaded_model.predict(features)
        print("✅ Prediction:", prediction)


        return render_template('index.html', prediction=prediction[0])
    
    return render_template("index.html" , prediction=None)

# not cancelled = 39,0,101.5,8,14,3,2,0,1,0,1
# cancelled = 146,2,132.3,10,19,4,4,1,0,3,0

if __name__=="__main__":
    app.run(host='0.0.0.0' , port=5050)