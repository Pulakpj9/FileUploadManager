from flask import Flask, request, render_template
import os
from PrintDirec import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']
    if file.filename == '':
        return "No selected file"

    # You can now save the uploaded file or perform any processing you need.
    # For this example, let's save the file in the 'uploads' directory.

    file_extension = file.filename.split('.')[-1]
    print(file_extension)

    destination_directory="C:\\Users\\Rishabh\\Desktop\\projects\\file\\uploads\\"+file_extension

    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    file.save('uploads/'+file_extension+'/' + file.filename)

    data ={
        'filename' : file.filename,
    }
    return render_template('success.html',data=data)

@app.route('/show-structure')
def structure():
    data = list_data()
    return render_template('structure.html',data=data)

if __name__ == '__main__':
    app.run(debug=True)
