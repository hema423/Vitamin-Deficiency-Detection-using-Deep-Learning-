from flask import *
import os
from werkzeug.utils import secure_filename
#import label_image
#import image_fuzzy_clustering as fem
import os
import numpy as np
import secrets
from PIL import Image
from flask import url_for, current_app
import cv2
import os
import predict as pred
from PIL import Image, ImageFilter 

UPLOAD_FOLDER = './static/Uploads/'
#SPECIFIC_FOLDER='./staic/input/'
ALLOWED_EXTENSIONS = {'jpg','jpeg','png'}



app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
@app.route('/first')
def first():
    return render_template('first.html')
@app.route('/upload')
def upload():
    return render_template('index.html')
 
  
    
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/chart')
def chart():
    return render_template('chart.html')

@app.route('/logout')
def logout():
    return render_template('login.html')
@app.route('/index')
def index():
    return render_template('index.html')

    return picture_path
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']
        filename = f.filename
        print("Filename==",filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        session['filename']=filename
        f.save(file_path)
        image = Image.open(file_path) 
        image = image.filter(ImageFilter.GaussianBlur)
        image.save("./static/Cleaned/"+filename) 
        predIdxs=pred.process("./static/Cleaned/"+filename)
        print("predIdxs==",predIdxs)
        cleanedpath="./static/Cleaned/"+filename
        return render_template("result.html",predIdxs=predIdxs,img_src=file_path,cleanedpath=cleanedpath)
       

if __name__ == '__main__':
    app.run()