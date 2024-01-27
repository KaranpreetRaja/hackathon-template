import os
from flask import Flask, send_file
from firebase_admin import credentials, firestore, initialize_app

from flask_cors import CORS, cross_origin
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

cur_path = os.path.dirname(os.path.realpath(__file__))
cred = credentials.Certificate(f"{cur_path}/key.json")
default_app = initialize_app(cred, {'storageBucket': 'vocal-vision.appspot.com'})

app = Flask(__name__)
from userAPI import user_api

# create a route to test the API
@app.route('/test')
def test():
    return 'API is working!'

app.register_blueprint(user_api, url_prefix='/api/user')

if __name__ == '__main__':
    app.run(debug=True)