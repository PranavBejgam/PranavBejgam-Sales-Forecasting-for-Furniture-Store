import streamlit as st
import pandas as pd
import joblib

# Load the model
best_model = joblib.load('sales_forecasting_pipeline.pkl')

# UI elements
st.title("Sales Forecasting for Furniture Store")

# Collect input data from user
ship_mode = st.selectbox('Ship Mode', ['Second Class', 'First Class', 'Standard Class', 'Same Day'])
segment = st.selectbox('Segment', ['Consumer', 'Corporate', 'Home Office'])
country = st.text_input('Country', 'United States')
city = st.text_input('City', 'New York')
state = st.text_input('State', 'New York')
region = st.selectbox('Region', ['East', 'West', 'Central', 'South'])
category = st.selectbox('Category', ['Furniture', 'Office Supplies', 'Technology'])
sub_category = st.text_input('Sub-Category', 'Chairs')
sales = st.number_input('Sales', 0.0)
quantity = st.number_input('Quantity', 1)
discount = st.slider('Discount', 0.0, 1.0)
profit = st.number_input('Profit', 0.0)
order_year = st.number_input('Order Year', 2023)
order_month = st.number_input('Order Month', 8)
order_day = st.number_input('Order Day', 15)

# Prepare the input data as a DataFrame
new_data = pd.DataFrame({
    'Ship Mode': [ship_mode],
    'Segment': [segment],
    'Country': [country],
    'City': [city],
    'State': [state],
    'Region': [region],
    'Category': [category],
    'Sub-Category': [sub_category],
    'Sales': [sales],
    'Quantity': [quantity],
    'Discount': [discount],
    'Profit': [profit],
    'Order Year': [order_year],
    'Order Month': [order_month],
    'Order Day': [order_day]
})

# Make predictions when the user clicks the button
if st.button('Predict Sales'):
    prediction = best_model.predict(new_data)
    st.write(f"Predicted Sales: {prediction[0]:.2f}")


from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib

app = Flask(__name__)

# Load the model
best_model = joblib.load('sales_forecasting_pipeline.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()
    new_data = pd.DataFrame([data])
    
    prediction = best_model.predict(new_data)
    
    return jsonify({'prediction': prediction[0]})

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib

app = Flask(__name__)

# Load the model
best_model = joblib.load('sales_forecasting_pipeline.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()
    new_data = pd.DataFrame([data])
    
    prediction = best_model.predict(new_data)
    
    return jsonify({'prediction': prediction[0]})

if __name__ == "__main__":
    app.run(debug=True)
