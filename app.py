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
    
    on_antithyroid_medication = st.radio('On Antithyroid Medication', ['No', 'Yes'])
    sick = st.radio('Sick', ['No', 'Yes'])
    pregnant = st.radio('Pregnant', ['No', 'Yes'])
    thyroid_surgery = st.radio('Thyroid Surgery', ['No', 'Yes'])
    i131_treatment = st.radio('I131 Treatment', ['No', 'Yes'])
    query_hypothyroid = st.radio('Query Hypothyroid', ['No', 'Yes'])
    query_hyperthyroid = st.radio('Query Hyperthyroid', ['No', 'Yes'])
    lithium = st.radio('Lithium', ['No', 'Yes'])
    goitre = st.radio('Goitre', ['No', 'Yes'])
    tumor = st.radio('Tumor', ['No', 'Yes'])
    hypopituitary = st.number_input('Hypopituitary')
    psych = st.radio('Psych', ['No', 'Yes'])
    tsh_measured = st.radio('TSH Measured', ['No', 'Yes'])
    tsh = st.number_input('TSH')
    t3_measured = st.radio('T3 Measured', ['No', 'Yes'])
    t3 = st.number_input('T3')
    tt4_measured = st.radio('TT4 Measured', ['No', 'Yes'])
    tt4 = st.number_input('TT4')
    t4u_measured = st.radio('T4U Measured', ['No', 'Yes'])
    t4u = st.number_input('T4U')
    fti_measured = st.radio('FTI Measured', ['No', 'Yes'])
    fti = st.number_input('FTI')
    tbg_measured = st.radio('TBG Measured', ['No', 'Yes'])
    tbg = st.number_input('TBG')
    
    referral_source_stmw = st.radio('Referral Source STMW', ['No', 'Yes'])
    referral_source_svhc = st.radio('Referral Source SVHC', ['No', 'Yes'])
    referral_source_svhd = st.radio('Referral Source SVHD', ['No', 'Yes'])
    referral_source_svi = st.radio('Referral Source SVI', ['No', 'Yes'])
    referral_source_other = st.radio('Referral Source Other', ['No', 'Yes'])

    # Convert categorical input to numeric
    sex_encoded = 1 if sex == 'Female' else 0
    on_thyroxine_encoded = 1 if on_thyroxine == 'Yes' else 0
    query_on_thyroxine_encoded = 1 if query_on_thyroxine == 'Yes' else 0
    # Convert other categorical inputs to numeric similarly

    # Prepare input data as DataFrame
    data ={
        'age': [age],
        'sex': [sex_encoded],
        'on_thyroxine': [on_thyroxine_encoded],
        'query_on_thyroxine': [query_on_thyroxine_encoded],
        'on_antithyroid_medication': [on_antithyroid_medication],
        'sick': [sick],
        'pregnant': [pregnant],
        'thyroid_surgery': [thyroid_surgery],
        'I131 treatment': [i131_treatment],
        'query hypothyroid': [query_hypothyroid],
        'query hyperthyroid': [query_hyperthyroid],
        'lithium': [lithium],
        'goitre': [goitre],
        'tumor': [tumor],
        'hypopituitary': [hypopituitary],
        'psych': [psych],
        'TSH measured': [tsh_measured],
        'TSH': [tsh],
        'T3 measured': [t3_measured],
        'T3': [t3],
        'TT4 measured': [tt4_measured],
        'TT4': [tt4],
        'T4U measured': [t4u_measured],
        'T4U': [t4u],
        'FTI measured': [fti_measured],
        'FTI': [fti],
        'TBG measured': [tbg_measured],
        'TBG': [tbg],
        'referral source_STMW': [referral_source_stmw],
        'referral source_SVHC': [referral_source_svhc],
        'referral source_SVHD': [referral_source_svhd],
        'referral source_SVI': [referral_source_svi],
        'referral source_other': [referral_source_other]
    }

    data_array = np.array(list(data.values())).reshape(1, -1)  # Convert to numpy array and reshape

    # Predict thyroid condition
    if st.button('Predict'):
        prediction = predict_thyroid(data_array)
        # You can customize the output based on your model's prediction
        st.success(f'Predicted Thyroid Condition: {prediction[0]}')

# Run the app
if __name__ == '__main__':
    main()
