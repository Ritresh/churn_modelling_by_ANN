<<<<<<< HEAD

# 🧾 Vendor Performance Analysis – Retail Inventory & Sales

_Analyzing vendor efficiency and profitability to support strategic purchasing and inventory decisions using SQL, Python, and Power BI._

---

## 📌 Table of Contents
- <a href="#overview">Overview</a>
- <a href="#business-problem">Business Problem</a>
- <a href="#dataset">Dataset</a>
- <a href="#tools--technologies">Tools & Technologies</a>
- <a href="#project-structure">Project Structure</a>
- <a href="#data-cleaning--preparation">Data Cleaning & Preparation</a>
- <a href="#exploratory-data-analysis-eda">Exploratory Data Analysis (EDA)</a>
- <a href="#research-questions--key-findings">Research Questions & Key Findings</a>
- <a href="#dashboard">Dashboard</a>
- <a href="#how-to-run-this-project">How to Run This Project</a>
- <a href="#final-recommendations">Final Recommendations</a>
- <a href="#author--contact">Author & Contact</a>

---
<h2><a class="anchor" id="overview"></a>Overview</h2>

This project evaluates vendor performance and retail inventory dynamics to drive strategic insights for purchasing, pricing, and inventory optimization. A complete data pipeline was built using SQL for ETL, Python for analysis and hypothesis testing, and Power BI for visualization.

---
<h2><a class="anchor" id="business-problem"></a>Business Problem</h2>

Effective inventory and sales management are critical in the retail sector. This project aims to:
- Identify underperforming brands needing pricing or promotional adjustments
- Determine vendor contributions to sales and profits
- Analyze the cost-benefit of bulk purchasing
- Investigate inventory turnover inefficiencies
- Statistically validate differences in vendor profitability

---
<h2><a class="anchor" id="dataset"></a>Dataset</h2>

- Multiple CSV files located in `/data/` folder (sales, vendors, inventory)
- Summary table created from ingested data and used for analysis

---

<h2><a class="anchor" id="tools--technologies"></a>Tools & Technologies</h2>

- SQL (Common Table Expressions, Joins, Filtering)
- Python (Pandas, Matplotlib, Seaborn, SciPy)
- Power BI (Interactive Visualizations)
- GitHub

---
<h2><a class="anchor" id="project-structure"></a>Project Structure</h2>

```
vendor-performance-analysis/
│
├── README.md
├── .gitignore
├── requirements.txt
├── Vendor Performance Report.pdf
│
├── notebooks/                  # Jupyter notebooks
│   ├── exploratory_data_analysis.ipynb
│   ├── vendor_performance_analysis.ipynb
│
├── scripts/                    # Python scripts for ingestion and processing
│   ├── ingestion_db.py
│   └── get_vendor_summary.py
│
├── dashboard/                  # Power BI dashboard file
│   └── vendor_performance_dashboard.pbix
```

---
<h2><a class="anchor" id="data-cleaning--preparation"></a>Data Cleaning & Preparation</h2>

- Removed transactions with:
  - Gross Profit ≤ 0
  - Profit Margin ≤ 0
  - Sales Quantity = 0
- Created summary tables with vendor-level metrics
- Converted data types, handled outliers, merged lookup tables

---
<h2><a class="anchor" id="exploratory-data-analysis-eda"></a>Exploratory Data Analysis (EDA)</h2>

**Negative or Zero Values Detected:**
- Gross Profit: Min -52,002.78 (loss-making sales)
- Profit Margin: Min -∞ (sales at zero or below cost)
- Unsold Inventory: Indicating slow-moving stock

**Outliers Identified:**
- High Freight Costs (up to 257K)
- Large Purchase/Actual Prices

**Correlation Analysis:**
- Weak between Purchase Price & Profit
- Strong between Purchase Qty & Sales Qty (0.999)
- Negative between Profit Margin & Sales Price (-0.179)

---
<h2><a class="anchor" id="research-questions--key-findings"></a>Research Questions & Key Findings</h2>

1. **Brands for Promotions**: 198 brands with low sales but high profit margins
2. **Top Vendors**: Top 10 vendors = 65.69% of purchases → risk of over-reliance
3. **Bulk Purchasing Impact**: 72% cost savings per unit in large orders
4. **Inventory Turnover**: $2.71M worth of unsold inventory
5. **Vendor Profitability**:
   - High Vendors: Mean Margin = 31.17%
   - Low Vendors: Mean Margin = 41.55%
6. **Hypothesis Testing**: Statistically significant difference in profit margins → distinct vendor strategies

---
<h2><a class="anchor" id="dashboard"></a>Dashboard</h2>

- Power BI Dashboard shows:
  - Vendor-wise Sales and Margins
  - Inventory Turnover
  - Bulk Purchase Savings
  - Performance Heatmaps

![Vendor Performance Dashboard](images/dashboard.png)

---
<h2><a class="anchor" id="how-to-run-this-project"></a>How to Run This Project</h2>

1. Clone the repository:
```bash
git clone https://github.com/yourusername/vendor-performance-analysis.git
```
3. Load the CSVs and ingest into database:
```bash
python scripts/ingestion_db.py
```
4. Create vendor summary table:
```bash
python scripts/get_vendor_summary.py
```
5. Open and run notebooks:
   - `notebooks/exploratory_data_analysis.ipynb`
   - `notebooks/vendor_performance_analysis.ipynb`
6. Open Power BI Dashboard:
   - `dashboard/vendor_performance_dashboard.pbix`

---
<h2><a class="anchor" id="final-recommendations"></a>Final Recommendations</h2>

- Diversify vendor base to reduce risk
- Optimize bulk order strategies
- Reprice slow-moving, high-margin brands
- Clear unsold inventory strategically
- Improve marketing for underperforming vendors

---
<h2><a class="anchor" id="author--contact"></a>Author & Contact</h2>

**Ayushi Mishra**  
Data Analyst  
📧 Email: techclasses0810@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/ayushi-mishra-30813b174/)  
🔗 [Portfolio](https://www.youtube.com/@techclasses0810/)
=======
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
>>>>>>> 5337eb571b4fded0cc91472fc922875323c0810f
