import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv("loan_data.csv")

x = df.drop("Approved",axis = 1)
y = df["Approved"]

X_train,X_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state = 42)


model = DecisionTreeClassifier(random_state = 42,max_depth = 5)

model.fit(X_train,y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test,y_pred))
print(classification_report(y_test,y_pred))

joblib.dump(model,"loan_prediction_model.pkl")

print("Model saved as 'loan_prediction_model.pkl'")

