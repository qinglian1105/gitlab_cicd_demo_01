from flask import Flask, request, redirect, url_for
from collections import defaultdict, OrderedDict
from tensorflow.keras.models import load_model
import numpy as np
import json
import datetime 


app = Flask(__name__)


# Index page
@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('test'))


# Test page to show datetime
@app.route('/test', methods=['GET'])
def test():
    x = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    d = "It is designed to make getting started quick and easy, with the ability to scale up to complex applications." 
    return [{"DateTime": x}, {"Flask": d}]
        

# Predict by Deep learning model 
@app.route('/api/dl_predict/', methods=['GET', 'POST'])
def dl_predict(): 
    if request.method=='POST':
        # receive data
        inputs = request.get_json()               
        for_pred = [inputs['v1'], inputs['v2'], inputs['v3'], inputs['v4'],
                    inputs['v5'], inputs['v6'], inputs['v7'], inputs['v8']]                                                  
        dict_label = {0:"No", 1:"Yes"}            
        ds = OrderedDict() 
        ds['Input_data'] = for_pred                                                
        predictions = [ds]
        # load model
        loaded_model = load_model('model_pima.h5')                                                    
        result = loaded_model.predict(np.array([for_pred]))
        yhat_class = 1 if result[0]>0.5 else 0
        output = dict_label[yhat_class]               
        predictions.append({"Predict": output})                     
        return json.dumps(predictions, ensure_ascii=False)       
    else:
        return "<h5>Please send a POST request with data for prediction.</h5>" 



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9000, debug=True)