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
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'

def main():
    # Title of the web app
    st.title('Diabetes Prediction Web App')
    
    # Input fields for user data with default value None
    pregnancies = st.number_input('Number of Pregnancies', value=None, max_value=20)
    glucose = st.number_input('Glucose Level', value=None, max_value=200)
    blood_pressure = st.number_input('Blood Pressure value', value=None, max_value=150)
    skin_thickness = st.number_input('Skin Thickness value', value=None, max_value=100)
    insulin = st.number_input('Insulin Level', value=None, max_value=1000)
    bmi = st.number_input('BMI value', value=None, max_value=60.0)
    diabetes_pedigree_function = st.number_input('Diabetes Pedigree Function value', value=None, max_value=2.5)
    age = st.number_input('Age of the Person', value=None, max_value=150)
    
    diagnosis = ''

    # Creating a button for Prediction
    if st.button('Test Result'):
        # Check if any input field is empty
        if '' not  in [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]:
            st.error('Please fill in all input fields.')
        else:
            diagnosis = diabetes_prediction([pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age])

    st.success(diagnosis)

if __name__ == '__main__':
    main()
