# import necessary libraries
from flask import Flask, render_template, request
import numpy as np
import pickle
data =[]
# create instance of Flask app
app = Flask(__name__)

# prediction function 
def ValuePredictor(to_predict_list): 
    to_predict = np.array([[to_predict_list]])
    loaded_model = pickle.load(open("00_2_Econ_model_2features.ipynb", "rb")) 
    result = loaded_model.predict(to_predict) 
    return result

# create route that renders index.html template
@app.route("/")
def echo():
    return render_template("index.html", text="Economic Model For Predicting Global Retail Price")



@app.route('/', methods = ['POST', 'GET']) 
def data_year(): 
    if request.method == 'POST':
        input_year = request.form['year']
        input_ICO = request.form['ico_cost']
        data = [input_year, input_ICO]
        prediction = ValuePredictor(data)
        return render_template("index.html", prediction = prediction) 

@app.route('/', methods = ['POST', 'GET']) 
def data_year(): 
    if request.method == 'POST':
        input_year = request.form['year']
        input_ICO = request.form['ico_cost']
        data = [input_year, input_ICO]
        prediction = ValuePredictor(data)
        return render_template("index.html", prediction = prediction) 




if __name__ == "__main__":
    app.run(debug=True)