# Churn Prediction
# Project Overview
This project was completed as part of a midterm exam for the Model Deployment course in the fourth semester. 
The primary objective of the project is to develop a machine learning model to predict customer churn and deploy the model using Streamlit, a web application framework. 
Churn prediction is a critical task for many industries, and this project compares multiple models to identify the best one for deployment. 
After selecting the best-performing model, it is deployed as an interactive web app using Streamlit for user accessibility and model inference.

# Case Description
The problem tackled in this project is the prediction of customer churn, i.e., 
identifying whether a customer will leave a service or continue to use it. 
The dataset includes customer data such as:
  - Credit Score
  - Age
  - Tenure (the number of years the customer has been with the company)
  - Balance (customer's account balance)
  - Number of Products (products held by the customer)
  - Estimated Salary
  - Has Credit Card (binary: Yes/No)
  - Is Active Member (binary: Yes/No)
  - Gender (Male/Female)
  - Geography (France, Germany, Spain)
The goal is to classify customers into two categories: Churn or No Churn, based on these features,
allowing companies to take proactive steps to reduce churn rates.

# Objectives
- Develop machine learning models to predict customer churn using features from customer data.
- Compare multiple models to identify the best-performing algorithm.
- Deploy the best model using Streamlit to make the predictions accessible via a web interface.
- Evaluate model performance using metrics like accuracy, precision, recall, and F1-score.

# Project Steps and Features
1. Data Collection and Preprocessing
- The dataset was cleaned, and any missing values were handled appropriately.
- Feature scaling and encoding of categorical variables were performed to ensure the dataset is suitable for machine learning models.

2. Model Construction
- Several machine learning algorithms were applied, including:
  - Random Forest
  - XGBoost
- The models were trained on a subset of the data and evaluated based on multiple classification metrics to determine the most effective model for churn prediction.

3. Model Evaluation
- Each model was evaluated using the following metrics:
  - Accuracy: Overall correctness of the predictions.
  - Precision, Recall, and F1-Score: To measure how well the models performed on each class (churn vs. no churn), especially in handling class imbalance.
  - Confusion Matrix: For a visual representation of correct and incorrect predictions across classes.
- Cross-validation was used to ensure the robustness of the models and avoid overfitting.

4. Best Model Selection
- Based on the performance metrics, the XGBoost model was selected as the best-performing model due to its high accuracy and balanced precision-recall scores.
- This model was saved as a .pkl file for deployment.

5. Deployment Using Streamlit
- The best model was deployed using Streamlit, allowing users to interact with the model through a web interface. Users can input customer data,
and the model will predict whether the customer is likely to churn or not.
- The app was designed with a simple interface for ease of use, including features for users to visualize prediction results and model insights.

# Tools Used
- Python: For data preprocessing, model development, and deployment.
- Libraries:
  - Pandas: For tabular data manipulation and cleaning.
  - NumPy: For array manipulation and mathematical operations.
  - Scikit-learn: For building and evaluating machine learning models, including RandomForestClassifier and GridSearchCV for hyperparameter tuning.
  - XGBoost: For implementing advanced machine learning models such as XGBoostClassifier.
  - Matplotlib & Seaborn: For data visualization and exploratory data analysis (EDA).
  - Pickle: For saving and loading trained models.
  - Shutil: For handling file and directory operations.
  - IPython.display: For creating download links within notebooks for easy model sharing.

# Challenges
- Model Selection: Choosing the best model required careful tuning and evaluation of multiple algorithms. 
- Class Imbalance: The dataset exhibited class imbalance, with fewer customers churning than remaining.
Techniques like adjusting class weights and focusing on precision-recall balance helped address this issue.
- Deployment: Deploying the model using Streamlit involved handling both model performance and user interface design, ensuring the app was user-friendly and accurate.

# Conclusion
This project successfully applied machine learning techniques to predict customer churn and deployed the best-performing model using Streamlit. 
After comparing multiple models, XGBoost was selected for deployment due to its superior performance on the evaluation metrics. 
The Streamlit app allows users to interact with the model, input customer data, and receive predictions on whether the customer is likely to churn.

Further improvements could include refining the user interface, adding more customer features, 
or testing more advanced machine learning algorithms to improve predictive performance.
