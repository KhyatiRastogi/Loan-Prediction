#  Loan Prediction using Decision Tree Classifier

A Machine Learning project that predicts whether a loan application will be **Approved** or **Rejected** using a **Decision Tree Classifier**.

---

##  Objective

The objective of this project is to build a loan prediction system that helps determine loan approval based on applicant details.

---

##  Dataset

 `loan_data.csv`

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

##  How to Run the Project

### `Using the ZIP file`

1. Download and extract the ZIP file.
2. Open the extracted project folder in VS code or any python IDE.

### `Using the GitHub Repository`
 
#### Clone the Repository

```bash
git clone <repository-link>
```

### `Train the Model`

```bash
python train_model.py
```

### `Run the Flask Application`

```bash
python app.py
```


### Home Page

- Enter Applicant Details
- Click **Predict Loan Status**

### Result Page

Displays

-  Loan Approved
-  Loan Rejected

---

##  Author

**Khyati Rastogi**

B.Tech CSE (Data Science)

Ajay Kumar Garg Engineering College
