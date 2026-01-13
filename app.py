import pickle
from flask import Flask,request,app,jsonify,url_for,render_template

import numpy as np
import pandas as pd


app = Flask(__name__)

#load the model
regmodel = pickle.load(open("regression.pkl", "rb"))
scalar = pickle.load(open("Scalling.pkl", "rb"))
##
@app.route('/')
def home():
    return render_template("home.html")

from flask import request, jsonify
import numpy as np

@app.route("/predict_api", methods=['POST'])
def predict_api():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No input data provided"}), 400

        features = ["CRIM","ZN","INDUS","CHAS","NOX","RM","AGE",
                    "DIS","RAD","TAX","PTRATIO","B","LSTAT"]

        try:
            input_list = [float(data[feature]) for feature in features]
        except KeyError as e:
            return jsonify({"error": f"Missing feature: {str(e)}"}), 400
        except ValueError:
            return jsonify({"error": "All inputs must be numeric"}), 400

        input_data = np.array(input_list).reshape(1, -1)
        scaled_data = scalar.transform(input_data)

        prediction = regmodel.predict(scaled_data)

        # 4. Return as a clear JSON object
        return jsonify({
            "prediction": float(prediction[0]),
            "status": "success"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/predict', methods = ['post'])
def predict():
    data = [float(x) for x in request.form.values()]
    final_input = scalar.transform(np.array(data).reshape(1,-1))
    print(final_input)
    output = regmodel.predict(final_input)[0]
    return render_template("home.html", prediction_text = "The predicted house price  is {}.".format(output))




if __name__ == "__main__":
    app.run(debug=True)







