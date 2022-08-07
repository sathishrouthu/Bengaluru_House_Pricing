from flask import Flask,redirect,jsonify,request,render_template
import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None

app = Flask(__name__)

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index=-1
    
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0],2)


def get_locations_for_ui():
    return __locations

def load_saved_artifats():
    print("Loading... saved artifacts.....")
    global __data_columns
    global __locations
    global __model
    with open("./artifacts/data_columns.pkl","rb") as f:
        __data_columns = pickle.load(f)["data_columns"]
        __locations = __data_columns[3:]
    with open("./artifacts/LR_model.pkl","rb") as f:
        __model = pickle.load(f)
    print("Loaded Artifacts done...")


@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations':get_locations_for_ui()
    })
    response.headers.add("Access-Control-Allow-Origin",'*')
    return response

@app.route('/predict_home_price',methods=["GET","POST"])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    response = jsonify({
        'estimated_price':get_estimated_price(location,total_sqft,bhk,bath)
    })
    response.headers.add("Access-Control-Allow-Origin",'*')
    return response

if __name__=="__main__":
    load_saved_artifats()
    print("Starting Flask server....")
    app.run(debug=True)
    
