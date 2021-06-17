import flask
from flask import request, url_for, render_template
app = flask.Flask(__name__)
app.config["DEBUG"] = True

from flask_cors import CORS
CORS(app)
cors = CORS(app, resources  = {
    r"/*" : {
        "origins" : "*"
    }
}

)

# main index page route
@app.route('/')
def home():
    return render_template('/home/abdoulaye/Desktop/ML_APP/index.html')


@app.route('/predict',methods=['GET'])
def predict():
    import joblib as jb
    import pickle
    model = pickle.load(open('/home/abdoulaye/Desktop/ML_APP/model_rand_f.pkl', 'rb'))
    
    print(model)
    predict_weather = model.predict([[float(request.args['Airtight']),
                            float(request.args['Relative_Humidity']),
                            float(request.args['Vapor_pressure_deficit']),
                            float(request.args['Specific_humidity']),
                            float(request.args['Water_vapor_concentration']),
                            float(request.args['Vapor_pressure']),
                            float(request.args['Temperature_dew_point']),
                            float(request.args['Saturation_vapor_pressure']),
                            float(request.args['Temperature_in_Kelvin']),
                            
                           ]])
    output = str(round(predict_weather[0],2))
    return render_template('/home/abdoulaye/Desktop/ML_APP/index.html', prediction_text='Le modele predit  :{}'.format(output))



if __name__ == "__main__":
    app.run(debug=True)
