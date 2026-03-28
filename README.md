# 🧠 Customer Churn Prediction using Artificial Neural Network (ANN)

Predicting whether a bank customer will leave the bank (churn) or stay using an Artificial Neural Network built with TensorFlow/Keras.  
This project includes data analysis, model training, and a Streamlit web application for real-time predictions.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Dataset](#dataset)
- [Tools & Technologies](#tools--technologies)
- [Project Structure](#project-structure)
- [Data Analysis & EDA](#data-analysis--eda)
- [Feature Engineering](#feature-engineering)
- [Model Building](#model-building-ann)
- [Model Evaluation](#model-evaluation)
- [Streamlit Application](#streamlit-application)
- [How to Run This Project](#how-to-run-this-project)
- [Future Improvements](#future-improvements)
- [Author & Contact](#author--contact)

---

# Overview

Customer churn is a major challenge in industries like banking and telecommunications. Losing existing customers directly affects business revenue.

This project builds a **machine learning model using an Artificial Neural Network (ANN)** to predict whether a customer will **exit the bank or remain**.

The project includes:

- Data cleaning and preprocessing  
- Exploratory Data Analysis (EDA)  
- Feature engineering and scaling  
- Artificial Neural Network model  
- Model evaluation  
- Streamlit web interface for predictions  

---

# Problem Statement

Banks want to **identify customers likely to leave (churn)** so they can take preventive actions such as:

- Offering incentives  
- Improving customer service  
- Targeted marketing campaigns  

The goal of this project is to:

- Analyze customer data  
- Identify patterns related to churn  
- Build a predictive model that estimates churn probability  

---

# Dataset

Dataset used:

```
Churn_Modelling.csv
```

Dataset location:

```
dataset/raw/Churn_Modelling.csv
```

The dataset contains **10,000 bank customer records** with information about customer demographics, financial activity, and whether the customer exited the bank.

### Dataset Features

| Feature | Description |
|-------|-------------|
| RowNumber | Row index |
| CustomerId | Unique customer identifier |
| Surname | Customer last name |
| CreditScore | Customer credit score |
| Geography | Country of the customer |
| Gender | Customer gender |
| Age | Customer age |
| Tenure | Number of years with the bank |
| Balance | Account balance |
| NumOfProducts | Number of bank products used |
| HasCrCard | Whether customer has a credit card |
| IsActiveMember | Whether customer is an active member |
| EstimatedSalary | Estimated annual salary |
| Exited | Target variable (1 = churn, 0 = stay) |

Dataset Source: Kaggle – Bank Customer Churn Dataset

---

# Tools & Technologies

### Programming Language
- Python

### Development Environment
- Visual Studio Code

### Notebook Environment
- Jupyter Notebook (VS Code)

### Data Analysis
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  

### Machine Learning
- Scikit-learn  
- TensorFlow / Keras  

### Model Techniques
- Artificial Neural Network (ANN)  
- Early Stopping  
- Class Weight Balancing  
- Feature Scaling (StandardScaler)  

### Deployment
- Streamlit  

### Version Control
- Git  
- GitHub  

---

# Project Structure


```
churn_modelling_by_ANN/
│
├── app/
│   └── app.py                # Streamlit web application
│
├── dataset/
│   └── raw/                  # Original dataset files
│
├── notebook/
│   └── churn.ipynb           # Data analysis and model development
│
├── output/
│   ├── churn_model.keras     # Trained ANN model
│   └── scaler.pkl            # Saved StandardScaler
│
├── requirements.txt          # Project dependencies
├── .gitignore                # Files ignored by Git
│
└── README.md
```

---

# Data Analysis & EDA

Exploratory Data Analysis was performed to understand customer behavior and identify patterns related to churn.

### Key Observations

**Churn Distribution**
- The dataset is imbalanced
- More customers stay compared to those who leave

**Age vs Churn**
- Older customers show a higher probability of churn

**Balance vs Churn**
- Customers with higher balances tend to churn more

**Geography Analysis**
- Germany shows the highest churn rate
- France has the largest number of customers

**Gender Analysis**
- Female customers churn slightly more compared to male customers

**Product Usage**
- Customers with **2 products churn the least**

**Active Membership**
- Customers who are not active members have a higher churn rate

---

# Feature Engineering

Several preprocessing steps were performed before training the model.

### Removed Columns

The following columns were removed because they do not contribute to prediction:

```
RowNumber
CustomerId
Surname
```

### Encoding

Categorical features were converted into numeric format:

```
Geography → One-Hot Encoding
Gender → Binary Encoding
```

### Feature Scaling

All numerical features were normalized using:

```
StandardScaler
```

This ensures that all features contribute equally during model training.

---

# Model Building (ANN)

The model was built using the **TensorFlow Keras Sequential API**.

### Architecture

```
Input Layer
   ↓
Dense Layer (16 neurons, ReLU)
   ↓
Dropout (0.2)
   ↓
Dense Layer (8 neurons, ReLU)
   ↓
Dropout (0.2)
   ↓
Dense Layer (4 neurons, ReLU)
   ↓
Output Layer (1 neuron, Sigmoid)
```

### Loss Function

```
Binary Crossentropy
```

### Optimizer

```
Adam
```

---

# Model Training Improvements

Two techniques were used to improve model performance.

### Early Stopping

Stops training when validation loss stops improving.

```
patience = 5
restore_best_weights = True
```

### Class Weight Balancing

Since the dataset is imbalanced, **class weights** were applied to balance the training process.

---

# Model Evaluation

The model was evaluated using:

- Accuracy
- Confusion Matrix
- Classification Report

Example accuracy achieved:

```
~85% accuracy (depends on training run)
```

Evaluation tools used:

```
accuracy_score
confusion_matrix
classification_report
```

---

# Streamlit Application

A **Streamlit web application** was developed to allow users to test the trained model interactively.

Users can input customer information such as:

- Credit score  
- Age  
- Balance  
- Estimated salary  
- Geography  
- Gender  
- Active membership  

The model then predicts whether the customer will:

```
Stay with the bank
or
Exit (Churn)
```

Run the Streamlit application using:

```
streamlit run app/app.py
```

---

# How to Run This Project

### 1 Clone the Repository

```
git clone https://github.com/yourusername/churn_modelling_by_ANN.git
```

Move into the project folder:

```
cd churn_modelling_by_ANN
```

---

### 2 Install Project Dependencies

All required Python libraries are listed in the **requirements.txt** file.

Install them using:

```
pip install -r requirements.txt
```

This will install libraries such as:

- TensorFlow
- Scikit-learn
- Pandas
- NumPy
- Streamlit
- Matplotlib
- Seaborn

---

### 3 Train the Model (Optional)

Open and run the notebook:

```
notebook/churn.ipynb
```

This notebook performs:

- Data cleaning
- Exploratory Data Analysis
- Feature engineering
- ANN model training
- Model evaluation

After training, the following files will be saved:

```
output/churn_model.keras
output/scaler.pkl
```

These files are used by the Streamlit application for predictions.

---

### 4 Run the Streamlit Application

Start the web app using:

```
streamlit run app/app.py
```

The application will open in your browser where you can input customer information and predict whether the customer will **stay or churn**.

---

### 5 About `.gitignore`

The `.gitignore` file ensures that unnecessary files are not pushed to GitHub, such as:

```
__pycache__/
*.pyc
.ipynb_checkpoints
venv/
.env
```

This keeps the repository clean and prevents uploading temporary or environment-specific files.

---

# Future Improvements

Possible improvements for this project include:

- Hyperparameter tuning  
- Cross-validation  
- Feature importance analysis  
- Trying additional models (Random Forest, XGBoost)  
- Deploying the application on Streamlit Cloud or AWS   

---

# Author & Contact

**Ritresh Kumar**

BCA Student | Aspiring Data Scientist | Machine Learning Enthusiast  

Skills:

- Python  
- Machine Learning  
- Deep Learning  
- Data Analysis  
- Neural Networks  
📧 Email: ritresh273@gmail.com
🔗 [LinkedIn](https://www.linkedin.com/feed/)  
🔗 [GitHub](https://github.com/Ritresh/Ritresh)
