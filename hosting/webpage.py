from altair import themes
import numpy as np
import pickle
import streamlit as st
import datetime

loaded_model = pickle.load(open("hosting/trained_model.sav", 'rb'))

doctors = [
    {"name": "Dr. Buddha Bahadur Karki", "specialization": "DM Diabetes and Endocrine"},
    {"name": "Dr. Dipak Malla", "specialization": "Internal Medicine & Diabetic and Endracrinologist"},
    {"name": "Dr. Nabin Kumar Sinjali", "specialization": "Internal Medicine Specialist"}
]
#background_image_url = "https://d2jx2rerrg6sh3.cloudfront.net/images/Article_Images/ImageForArticle_22744_16565132428524067.jpg"

# Add a CSS style to set the background image
# st.markdown(
#     f"""
#     <style>
#     .stApp {{
#         background-image: url("{background_image_url}");
#         background-size: cover;
#         background-color: rgba(0,0,0,0)
#         background-size: 100% 100%;
#         textColor="#0a0a0a"
#     }}
#     </style>
#     """,
#     unsafe_allow_html=True,
# )
def diabetes_prediction(input_data):
    # Reshape the input data for prediction
    input_data_reshaped = np.array(input_data).reshape(1, -1)
    # Predict using the loaded model
    prediction = loaded_model.predict(input_data_reshaped)
    # Interpret the prediction
    if prediction[0] == 0:
        result = "**Not Diabetic**"
        doctor_suggestions = [
            "1. Based on the provided information, you seem to be at low risk of diabetes. However, it's always important to maintain a healthy lifestyle and have regular check-ups with your doctor.",
            "2. You have a balanced lifestyle. Keep up the good work and continue with healthy habits.",
            "3. Stay hydrated and make sure to get enough sleep for overall well-being.",
            "4. Consider regular health check-ups to monitor your health status.",
            "5. Regular exercise and a balanced diet are key to maintaining good health. Keep it up!",
            "------------------Thank you----------------"
        ]
    else:
        result = "**Diabetic**"
        # Randomly select a doctor from the list
        doctor = np.random.choice(doctors)
        doctor_name = doctor["name"]
        doctor_specialization = doctor["specialization"]
        doctor_suggestions = [
            f"Based on the provided information, you appear to have a higher risk of diabetes. It is recommended to consult with {doctor_name}, {doctor_specialization}, for further evaluation and guidance.",
            "Making a few changes in your lifestyle now may help you avoid the serious health complications of diabetes in the future, such as nerve, kidney and heart damage. It's never too late to start..",
            "1. Lose extra weight",
            "2. Be more physically active.",
            "3. Eat healthy plant foods.",
            "4. Avoid sugary foods.",
            "------------------Thank you----------------"
        ]
    return result, doctor_suggestions



def main():
  
    st.title('**Hospital Report: Diabetes Prediction**')

    st.header('**Patient Information**')
    name = st.text_input('Name',placeholder="Type your Name...")
    gender = st.selectbox('Gender', ['Male', 'Female', 'Other'])
    address = st.text_area('Address',placeholder="Type a Address...")
    #contact = st.text_area('Contact',placeholder="Type a number...")
    d = st.date_input("Date:",'today' )
    
    st.write('---')  # Separator line
    st.header('**Medical Data**')
    if gender == 'Male':
        pregnancies = 0
    else:
     pregnancies= st.number_input('Number of Pregnancies', value=None, min_value=0,max_value=20,placeholder="Insert the value between 0 to 20")
    # pregnancies = st.number_input('Number of Pregnancies', value=None,max_value=20)
    glucose = st.number_input('Glucose Level (mg/dL)', value=None,min_value=0, max_value=200,placeholder="Insert the value between 0 to 200")
    blood_pressure = st.number_input('Blood Pressure (mm Hg)', value=None,min_value=0, max_value=150,placeholder="Insert the value between 0 to 150")
    skin_thickness = st.number_input('Skin Thickness (mm)', value=None,min_value=0, max_value=150,placeholder="Insert the value between 0 to 100")
    insulin = st.number_input('Insulin Level (mu U/ml)', value=None, min_value=0,max_value=1000,placeholder="Insert the value between 0 to 1000")
    bmi = st.number_input('BMI (Body Mass Index)', value=None,min_value=0.0, max_value=100.0,placeholder="Insert the value between 0 to 100")
    diabetes_pedigree_function = st.number_input('Diabetes Pedigree Function', value=None,min_value=0.0, max_value=2.5, format='%f',placeholder="Insert the value between 0 to 2.5")
    age = st.number_input('Age of the Person', value=None,min_value=0, max_value=150,placeholder="Insert the value between 0 to 150")
    st.write('---')  # Separator line

    if st.button('**Generate Report**'):
        if None in [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]:
            st.error('Please fill in all medical data fields.')
        else:
            result, doctor_suggestions = diabetes_prediction([pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age])
            # Display the report
            st.header('**Diabetes Prediction Report**')
            st.write('Date:', d)
            st.write(f'Patient Name: {name}')
            st.write(f'Gender: {gender}')
            st.write(f'Address: {address}')
           # st.write(f'Patient contact: {contact}')
            st.write('---')
            st.write(f'pregnancies: {pregnancies}')
            st.write(f'glucose: {glucose}')
            st.write(f'blood_pressure: {blood_pressure}') 
            st.write(f'skin_thickness: {skin_thickness}')
            st.write(f'insulin: {insulin}')
            st.write(f'bmi: {bmi}')
            st.write(f'diabetes_pedigree_function: {diabetes_pedigree_function}')
            st.write(f'age: {age}')
            # st.write(f'pregnancies: {pregnancies}, glucose: {glucose}, blood_pressure: {blood_pressure}, skin_thickness: {skin_thickness}, insulin: {insulin}, bmi: {bmi}, diabetes_pedigree_function: {diabetes_pedigree_function}, age: {age}')
            st.write('---')
            st.write(f'Prediction Result: {result}')
            st.write('Doctor Suggestions:')
            for suggestion in doctor_suggestions:
                st.write(suggestion)


if __name__ == '__main__':
    main()
