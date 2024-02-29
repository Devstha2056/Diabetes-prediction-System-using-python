import numpy as np
import pickle
import streamlit as st

# Loading the saved model
loaded_model = pickle.load(open("hosting/trained_model.sav", 'rb'))
# Creating a function for prediction
def diabetes_prediction(input_data):

    # Reshape the array as we are predicting for one instance
    input_data_reshaped = np.array(input_data).reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)

    if prediction[0] == 0:
        result = "not diabetic"
        doctor_suggestion = "Based on the provided information, you seem to be at low risk of diabetes. However, it's always important to maintain a healthy lifestyle and regular check-ups with your doctor."
    else:
        result = "diabetic"
        doctor_suggestion = "Based on the provided information, you appear to have a higher risk of diabetes. It is recommended to consult with a healthcare professional for further evaluation and guidance."

    return f"The model predicts that the person is {result}. {doctor_suggestion}"

def main():
    # Title of the web app
    st.title('Diabetes Prediction Web App')
    
    # Input fields for user data with default value None
    pregnancies = st.number_input('Number of Pregnancies', value=None, max_value=20)
    glucose = st.number_input('Glucose Level', value=None, max_value=200)
    blood_pressure = st.number_input('Blood Pressure value', value=None, max_value=150)
    skin_thickness = st.number_input('Skin Thickness value', value=None, max_value=150)
    insulin = st.number_input('Insulin Level', value=None, max_value=1000)
    bmi = st.number_input('BMI value', value=None, max_value=100.0)
    diabetes_pedigree_function = st.number_input('Diabetes Pedigree Function value', value=None, max_value=2.50000)
    age = st.number_input('Age of the Person', value=None, max_value=150)
    
    diagnosis = ''

    # Creating a button for Prediction
    if st.button('Test Result'):
        # Check if any input field is empty
        if None in [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]:
            st.error('Please fill in all input fields.')
        else:
            diagnosis = diabetes_prediction([pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age])

    st.success(diagnosis)

if __name__ == '__main__':
    main()
