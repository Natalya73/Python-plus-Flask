import os
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import mimetypes


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'mp3', 'ogg', 'wav'}

def is_sound_file(file_path): #  look once more
    mime_type, _ = mimetypes.guess_type(file_path)
    return mime_type and mime_type.startswith('audio/')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def base():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('base.html', files=files)

@app.route('/list')
def list_files():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    # return files
    return jsonify(files)


@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']

    if file and is_sound_file(file.filename):  #!!! look once more
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        message = 'SUCCESS!'
        return render_template('results.html', the_results=message,)
        # return jsonify({'message': 'File uploaded successfully.'})
    elif not file:
        message = 'NO FILE CHOSEN'
        return render_template('results.html', the_results=message,)
        
    else:
        message = 'NON-AUDIO FILE DETECTED!!!'
        return render_template('results.html', the_results=message,)
        # return jsonify({'error': 'Non-audio file detected.'}), 400



if __name__ == '__main__':
    app.run(debug=True, port=8888)

