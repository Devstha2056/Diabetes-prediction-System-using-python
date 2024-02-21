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
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the Person')
    
    # Button to trigger prediction
    if st.button('Diabetes Test Result'):
        if '' not in [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]:
            diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
            st.success(diagnosis)
        else:
            st.error('Please fill in all input fields.')

if __name__ == '__main__':
    main()

    
    
    
    
    
    
    
    
    
    
    
    
  
    
  
