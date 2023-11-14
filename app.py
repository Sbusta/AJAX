from flask import Flask, jsonify, request, render_template
import requests
from flask_cors import CORS
from flask import send_file
import Analizador
import PostAnalizador
import os
app = Flask(__name__, template_folder='templates',static_folder='statics')
UPLOAD_FOLDER = 'upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
DEFAULT_IP = '0.0.0.0:3000'
CORS(app)
@app.route('/analisis',methods =['GET'])
def analisis():
    return render_template('analisis.html', title = 'Ajax')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    try:
        os.remove("log")
    except:
        pass 
    if request.method == 'POST':
        f = request.files['file']
        f.save("log")
        js = Analizador.main()
        datosCluster = PostAnalizador.main()
        return render_template('muestraAnalisis.html', title = 'Analisis', datos = datosCluster)

@app.route('/downloader', methods = ['GET'])
def downloader():
    return send_file('result.json', as_attachment=True, attachment_filename="datos.json")

app.run("0.0.0.0",port=3000, debug=True)