# import necessary libraries
from flask import Flask, render_template, request
import pickle
import numpy as np




# variables
data =[]
brent_data = []


# create instance of Flask app
app = Flask(__name__)

# prediction function 
def ValuePredictor(to_predict_list): 
    print("Hello")
    to_predict = np.array([to_predict_list])
    with open("pickel2_Economic_web_model_2_inputs.pickle", "rb") as f:
        loaded_model = pickle.load(f)
    result = loaded_model.predict(to_predict) 
    return result




def BrentPredictor(to_predict_list): 
    to_predict_brent = np.array([to_predict_list])
    with open("pickel3_Economic_web_model_3_inputs.pickle", "rb") as g:
        loaded_model_brent = pickle.load(g) 
    result_brent = loaded_model_brent.predict(to_predict_brent) 
    return result_brent
     

# create route that renders index.html template
@app.route("/")
def echo():
    return render_template("index_maybe.html", text="Economic Model For Predicting Global Retail Price")



@app.route('/', methods = ['POST', 'GET']) 
def data_year(): 
    if request.method == 'POST':
        input_year = request.form['year']
        input_ICO = request.form['ico_cost']
        data = [input_year, input_ICO]
        prediction = ValuePredictor(data)
        return render_template("index_maybe.html", prediction = prediction) 

@app.route('/brent', methods = ['POST', 'GET']) 
def Brent(): 
    if request.method == 'POST':
        input_brent_year = request.form['year']
        input_brent_ICO = request.form['ico_cost']
        brent = request.form['brent']
        brent_data = [input_brent_year, input_brent_ICO, brent ]
        brent_prediction = BrentPredictor(brent_data)
        return render_template("index_maybe.html", Brent_predict = brent_prediction) 




if __name__ == "__main__":
    app.run(debug=True)