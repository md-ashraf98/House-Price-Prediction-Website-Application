from flask import Flask, request, render_template
import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

app = Flask(__name__)

# Load the Dataset
data = pd.read_csv(r'C:\Users\moham\PycharmProjects\HousePricePredictionWebApplication\House_Price_Data.csv')

# print(data)
unique_locations = data['Location'].unique().tolist()

# Load the model and pipeline
with open('E:\HousePricePredictionWebApplication\website\House_prediction_model.pkl', 'rb') as file:
    pipeline = pickle.load(file)


@app.route('/')
def index():
    return render_template('index.html', locations=unique_locations)


@app.route('/predict', methods=['POST'])
def predict():
    location = request.form['Location']
    bedrooms = int(request.form['Bedrooms'])
    bathrooms = int(request.form['Bathrooms'])
    area_in_sqft = float(request.form['Area in sqft.'])
    furnishing_status = int(request.form['Furnishing Status'])
    guestrooms = int(request.form['Guestrooms'])
    parking_area = int(request.form['Parking Area'])

    # creating a DataFrame from user input
    input_data = {
        'Location': [location],
        'Bedrooms': [bedrooms],
        'Bathrooms': [bathrooms],
        'Area in sqft.': [area_in_sqft],
        'Furnishing Status': [furnishing_status],
        'Guestrooms': [guestrooms],
        'Parking Area': [parking_area]
    }

    input_df = pd.DataFrame(input_data)

    # Make predictions
    prediction = pipeline.predict(input_df)[0]

    return render_template('index.html', locations=unique_locations,
                           prediction_text=f'Predicted Price: ${prediction:,.2f}')


if __name__ == "__main__":
    app.run(debug=True)