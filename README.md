#  Loan Prediction using Decision Tree Classifier

A Machine Learning project that predicts whether a loan application will be **Approved** or **Rejected** using a **Decision Tree Classifier**. The project includes data preprocessing, model training, evaluation, and deployment using Flask.

---

##  Project Overview

The objective of this project is to build a loan prediction system that helps determine loan approval based on applicant details.

The application takes the following inputs:
- Age
- Annual Income
- Loan Amount
- Credit Score

Based on these inputs, the trained Decision Tree model predicts whether the loan will be **Approved** or **Rejected**.

---

##  Dataset

**Dataset Name:** `loan_data.csv`

### Features

- Age
- Income
- Loan Amount
- Credi Score
- Target (0 -> Rejected, 1 -> Approved)

---

##  Technologies Used

- Python
- Pandas
- Scikit-learn
- Flask
- Joblib
- HTML
- CSS

---

##  Project Workflow

### Step 1: Data Preprocessing
- Loaded dataset using Pandas
- Selected input and output features
- Split dataset into training and testing sets

### Step 2: Model Training
- Used Decision Tree Classifier

### Step 3: Model Evaluation
- Accuracy Score
- Classification Report

### Step 4: Model Deployment
- Saved the trained model using Joblib
- Created a Flask web application
- Designed a user-friendly interface using HTML & CSS

---

##  Model Performance

**Algorithm Used:** Decision Tree Classifier

**Accuracy:** **83%**

---

##  Project Structure

```
Loan_Prediction/

│── app.py
│── train_model.py
│── loan_data.csv
│── loan_prediction_model.pkl
│── README.md
│── requirements.txt

└── templates
      ├── index.html
      └── result.html
```

---

##  How to Run the Project

### 1. Clone the Repository

```bash
git clone <repository-link>
```

### 2. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 3. Train the Model

```bash
python train_model.py
```

### 4. Run the Flask Application

```bash
python app.py
```

### 5. Open in Browser

```
http://127.0.0.1:5000
```

---

## Application Preview

### Home Page

- Enter Applicant Details
- Click **Predict Loan Status**

### Result Page

Displays

- ✅ Loan Approved

or

- ❌ Loan Rejected

---

##  Author

**Khyati Rastogi**

B.Tech CSE (Data Science)

Ajay Kumar Garg Engineering College
