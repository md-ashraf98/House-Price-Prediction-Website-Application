# House Price Prediction Web Application

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Project Overview
The **House Price Prediction Web Application** is a tool designed to predict house prices based on various input features. This project uses a machine learning model, specifically a Random Forest Regressor, to analyze the data and make predictions. The application is built using the Flask web framework and provides a user-friendly interface for entering property details to get instant price estimates.

## Features
- **Location-Based Predictions:** Predict house prices based on specific locations.
- **Intuitive Interface:** Simple and easy-to-use web interface for entering property details.
- **Feature-Rich Model:** Considers multiple factors like location, number of bedrooms, bathrooms, area in square feet, furnishing status, and more.
- **Real-Time Predictions:** Provides instant predictions displayed in Indian Rupees (INR).

## Technology Stack
- **Frontend:** HTML, CSS
- **Backend:** Flask
- **Machine Learning:** Scikit-learn, Pandas, NumPy
- **Model:** Random Forest Regressor
- **Deployment:** Flask web server

## Installation
To get started with the project, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/house-price-prediction.git
    ```

2. **Navigate to the project directory:**
    ```bash
    cd house-price-prediction
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Flask application:**
    ```bash
    python app.py
    ```

5. **Access the application in your browser:**
    ```plaintext
    http://127.0.0.1:5000/
    ```

## Usage
1. **Cover Page:** Start at the cover page and click "Let's Get Started" to proceed to the main page.
   
2. **Main Page:** Enter property details, including location, number of bedrooms, bathrooms, area in square feet, furnishing status, etc. After filling in the details, click "Predict Price" to get the estimated price.

3. **Prediction Result:** The predicted house price will be displayed on the same page.

## Model Details
- **Model:** Random Forest Regressor
- **Input Features:** 
  - Location
  - Bedrooms
  - Bathrooms
  - Area (in square feet)
  - Furnishing Status
  - Guestrooms
  - Parking Area
  - Basement
  - Air Conditioning
- **Data Preprocessing:** Categorical variables are encoded using OneHotEncoder, and numerical features are scaled using StandardScaler.
- **Training:** The model was trained on a dataset of house prices and optimized for prediction accuracy.

## File Structure
```plaintext
House-Price-Prediction/
│
├── static/
│   ├── Bg-cover.jpg
│   ├── tv-embedded-wall.jpg
│   └── style.css
│
├── templates/
│   ├── Cover.html
│   └── index.html
│
├── app.py
├── House_Price_Data.csv
├── House_price_prediction_model.pkl
└── README.md
