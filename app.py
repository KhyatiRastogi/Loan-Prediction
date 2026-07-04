from flask import Flask, render_template, request
import joblib
import webbrowser

app = Flask(__name__)

model = joblib.load("loan_prediction_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods = ["POST"])
def predict():
    age = float(request.form["Age"])
    income= float(request.form["Income"])
    loan = float(request.form["LoanAmount"])
    credit = float(request.form["CreditScore"])
    prediction = model.predict([[age,income,loan,credit]])

    if prediction[0] == 1:
        result = "Loan Approved"
        result_class = "approved"
        emoji = "✅"
       
    else:
        result = "Loan Rejected"
        result_class = "rejected"
        emoji = "❌"

    return render_template("result.html",prediction_text = result,result_class=result_class,emoji=emoji) 

if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5000")
    app.run(debug = True)