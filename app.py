import numpy as np
from flask import Flask, render_template, request
import math
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    final_features = np.array(features).reshape(1, -1)
    prediction = model.predict(final_features)[0]
    output = math.floor(prediction)

    return render_template(
        'index.html',
        prediction_text=f"🏠 Estimated House Price: ₹ {output:,}"
    )

if __name__ == "__main__":
    app.run(debug=True)
