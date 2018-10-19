from flask import Flask, request, json
from os import getenv
import boto3
import pickle

BUCKET_NAME = 'helpo-ml'
MODEL_FILE_NAME = 'model.pkl'
app = Flask(__name__)
S3 = boto3.client('s3', 
    region_name='us-west-2', 
    aws_access_key_id=getenv('aws_access_key_id'),
    aws_secret_access_key=getenv('aws_secret_access_key')
)

@app.route('/', methods=['POST'])
def index():    
    # Parse request body for model input 
    body_dict = request.get_json(silent=True)    
    data = body_dict['data']     
    
    # Load model
    model = load_model(MODEL_FILE_NAME)
    # Make prediction 
    prediction = model.predict(data).tolist()
    # Respond with prediction result
    result = {'prediction': prediction}    
   
    return json.dumps(result)

@app.route('/hello-world')
def hello_world():
    return json.dumps('Hello world!')

def load_model(key):    
    # Load model from S3 bucket
    response = S3.get_object(Bucket=BUCKET_NAME, Key=key)
    # Load pickle model
    model_str = response['Body'].read()     
    model = pickle.loads(model_str)     
    
    return model

if __name__ == '__main__':    
    # listen on all IPs 
    app.run(debug=getenv('debug', False), host='0.0.0.0')