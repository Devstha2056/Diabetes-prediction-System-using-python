import numpy as np
import pickle
import streamlit as st

# Loading the saved model
loaded_model = pickle.load(open("hosting/trained_model.sav", 'rb'))

# Creating a function for prediction
def diabetes_prediction(input_data):
    # Convert input data to numeric values
    input_data = [float(x) for x in input_data]

    # Reshape the array as we are predicting for one instance
    input_data_reshaped = np.array(input_data).reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)

    if prediction[0] == 0:
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'

def main():
    # Title of the web app
    st.title('Diabetes Prediction Web App')
    
    # Input fields for user data
    pregnancies = st.number_input('Number of Pregnancies', min_value=0, max_value=20, step=1)
    glucose = st.number_input('Glucose Level', min_value=0, max_value=200, step=1)
    blood_pressure = st.number_input('Blood Pressure value', min_value=0, max_value=150, step=1)
    skin_thickness = st.number_input('Skin Thickness value', min_value=0, max_value=150, step=1)
    insulin = st.number_input('Insulin Level', min_value=0, max_value=1000, step=1)
    bmi = st.number_input('BMI value', min_value=0.0, max_value=100.0, step=0.1)
    diabetes_pedigree_function = st.number_input('Diabetes Pedigree Function value', min_value=0.0, max_value=2.5, step=0.01)
    age = st.number_input('Age of the Person', min_value=0, max_value=150, step=1)
    
    # Button to trigger prediction
    if st.button('Diabetes Test Result'):
        if '' not in [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]:
            st.error('Please fill in all input fields.')
        else:
            diagnosis = diabetes_prediction([pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age])
            st.success(diagnosis)

if __name__ == '__main__':
    main()
