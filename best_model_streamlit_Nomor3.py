import streamlit as st
import joblib
import pandas as pd

# Load the machine learning model
model = joblib.load('best_model.pkl')

def main():
    st.title('Churn Prediction App')

    # User input components using slider widgets
    st.subheader('Customer Information:')
    col1, col2 = st.columns(2)
    with col1:
        credit_score = st.slider('Credit Score', min_value=300, max_value=850, value=650, step=1)
        age = st.slider('Age', min_value=18, max_value=100, value=35, step=1)
        tenure = st.slider('Tenure (years)', min_value=0, max_value=20, value=5, step=1)
    with col2:
        balance = st.slider('Account Balance', min_value=0, max_value=250000, value=50000, step=1000)
        num_of_products = st.slider('Number of Products', min_value=1, max_value=4, value=2, step=1)
        estimated_salary = st.slider('Estimated Salary', min_value=0, max_value=200000, value=100000, step=1000)

    # Binary features with radio buttons
    has_cr_card = st.radio('Has Credit Card', ['Yes', 'No'])
    is_active_member = st.radio('Is Active Member', ['Yes', 'No'])
    gender = st.radio('Gender', ['Female', 'Male'])

    # Categorical features with selectbox
    geography = st.selectbox('Geography', ['France', 'Germany', 'Spain'])

    # Convert binary features to numerical
    has_cr_card = 1 if has_cr_card == 'Yes' else 0
    is_active_member = 1 if is_active_member == 'Yes' else 0
    gender_male = 1 if gender == 'Male' else 0
    gender_female = 1 if gender == 'Female' else 0

    # Prepare data for prediction
    input_data = pd.DataFrame({
        'CreditScore': [credit_score],
        'Age': [age],
        'Tenure': [tenure],
        'Balance': [balance],
        'NumOfProducts': [num_of_products],
        'HasCrCard': [has_cr_card],
        'IsActiveMember': [is_active_member],
        'EstimatedSalary': [estimated_salary],
        # One-hot encoding for geography
        'Geo_France': [1 if geography == 'France' else 0],
        'Geo_Germany': [1 if geography == 'Germany' else 0],
        'Geo_Spain': [1 if geography == 'Spain' else 0],
        # One-hot encoding for gender
        'Gender_Female': [gender_female],
        'Gender_Male': [gender_male]
    })

    # Predict button
    if st.button('Predict'):
        # Make prediction
        prediction = model.predict(input_data)

        # Display the result
        st.subheader('Prediction Result:')
        if prediction[0] == 1:
            st.error('The customer is predicted to churn.')
        else:
            st.success('The customer is predicted not to churn.')

if __name__ == '__main__':
    main()
