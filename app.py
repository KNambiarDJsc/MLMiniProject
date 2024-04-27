from flask import Flask, render_template, request, redirect, url_for
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load(r'C:\Users\Karthik\Desktop\CKD\kidney2.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get user input from the form
    blood_pressure = float(request.form['blood_pressure'])
    albumin = float(request.form['albumin'])
    sugar = float(request.form['sugar'])
    blood_urea = float(request.form['blood_urea'])
    serum_creatinine = float(request.form['serum_creatinine'])
    potassium = float(request.form['potassium'])
    haemoglobin = float(request.form['haemoglobin'])
    red_blood_cell_count = float(request.form['red_blood_cell_count'])
    age = float(request.form['age'])

    # Create a DataFrame with user input
    input_data = pd.DataFrame([[blood_pressure, albumin, sugar, blood_urea, serum_creatinine,
                                potassium, haemoglobin, red_blood_cell_count, age]],
                              columns=['blood_pressure', 'albumin', 'sugar', 'blood_urea', 'serum_creatinine',
                                       'potassium', 'haemoglobin', 'red_blood_cell_count', 'age'])

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Redirect based on prediction
    if prediction == 1:
        return redirect(url_for('negative_result'))
    else:
        return redirect(url_for('positive_result'))

@app.route('/positive_result')
def positive_result():
    return render_template('positive__result.html')

@app.route('/negative_result')
def negative_result():
    return render_template('negative_result.html')

if __name__ == '__main__':
    app.run(debug=True)
