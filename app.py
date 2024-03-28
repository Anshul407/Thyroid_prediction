import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('thyroid_prediction_model.sav')

# Function to predict thyroid condition
def predict_thyroid(data):
    return model.predict(data)

# Main function for Streamlit app
def main():
    # Title
    st.title('Thyroid Condition Prediction App')

    # Input fields
    age = st.slider('Age', 18, 100, 25)
    sex = st.radio('Gender', ['Male', 'Female'])
    on_thyroxine = st.radio('On Thyroxine', ['No', 'Yes'])
    query_on_thyroxine = st.radio('Query on Thyroxine', ['No', 'Yes'])
    # Add remaining input fields similar to the ones above for other columns

    # Convert categorical input to numeric
    sex_encoded = 1 if sex == 'Female' else 0
    on_thyroxine_encoded = 1 if on_thyroxine == 'Yes' else 0
    query_on_thyroxine_encoded = 1 if query_on_thyroxine == 'Yes' else 0
    # Convert other categorical inputs to numeric similarly

    # Prepare input data as DataFrame
    data = pd.DataFrame({
        'age': [age],
        'sex': [sex_encoded],
        'on_thyroxine': [on_thyroxine_encoded],
        'query_on_thyroxine': [query_on_thyroxine_encoded],
        # Add remaining columns and their values similarly
    })

    # Predict thyroid condition
    if st.button('Predict'):
        prediction = predict_thyroid(data)
        # You can customize the output based on your model's prediction
        st.success(f'Predicted Thyroid Condition: {prediction[0]}')

# Run the app
if __name__ == '__main__':
    main()
