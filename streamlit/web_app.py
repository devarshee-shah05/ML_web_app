import numpy as np
import pickle
import streamlit as st

# loading saved model
loaded_model = pickle.load(open("/Users/shahd/Desktop/Devarshee/Vs studio/Model_deploy/Streamlit/diabetes website/trained_model.sav",'rb'))

# creating a function for prediction
def diabetes_prediction(input_data):
    input_data = (5,166,72,19,175,25.8,0.587,51)

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'
    
# Building user interface
def main():
    # giving a title
    st.title('Diabetes Prediction Web App')
    
    # creating input database
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure Value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the Person')
    
    # code for Prediction
    # creating a variable named diagnosis and giving it null string 
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
        
    st.success(diagnosis)

# Running in anacondaa command prompt
if __name__ == '__main__':
    main()
    
# Run on anaconda terminal as streamlit run "C:\Users\DEVARSHI SHAH\Desktop\vs code\Streamlit\web_app.py"