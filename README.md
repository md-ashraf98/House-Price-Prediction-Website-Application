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

To use the House Price Prediction web application, follow these steps:

1. **Clone the Repository:**
    - Begin by cloning the repository to your local machine:
    ```bash
    git clone https://github.com/your-username/house-price-prediction.git
    ```

2. **Navigate to the Project Directory:**
    - Move into the project's directory:
    ```bash
    cd house-price-prediction
    ```

3. **Install the Required Dependencies:**
    - Ensure all the necessary Python packages are installed using the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

4. **Start the Flask Application:**
    - Run the Flask application to start the web server:
    ```bash
    python app.py
    ```

5. **Access the Application:**
    - Open your web browser and navigate to:
    ```plaintext
    http://127.0.0.1:5000/
    ```

6. **Using the Application:**
    - **Cover Page:** You'll start on the cover page. Click the "Let's Get Started" button to proceed to the main page.
    - **Main Page:** 
        - Enter the details of your property, such as location, number of bedrooms, bathrooms, area in square feet, furnishing status, etc.
        - Click the "Predict Price" button to generate the estimated house price.
    - **View Prediction:** The predicted house price will be displayed on the main page in Indian Rupees.

7. **Shut Down the Application:**
    - To stop the Flask server, return to your terminal and press `Ctrl+C`.

8. **(Optional) Customize the Project:**
    - Feel free to modify the HTML, CSS, and Python code to better suit your needs. You can also retrain the model with new data if desired.


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
