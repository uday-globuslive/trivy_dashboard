from flask import Flask, render_template, request, redirect, url_for, flash
import os
import json
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def get_reports():
    reports = []
    for filename in os.listdir(UPLOAD_FOLDER):
        if filename.endswith('.json'):
            path = os.path.join(UPLOAD_FOLDER, filename)
            with open(path) as f:
                data = json.load(f)
            reports.append({
                'filename': filename,
                'data': data,
                'uploaded': datetime.fromtimestamp(os.path.getctime(path))
            })
    reports.sort(key=lambda x: x['uploaded'], reverse=True)
    return reports

@app.route('/', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        if 'report' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['report']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and file.filename.endswith('.json'):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            flash('Report uploaded successfully!')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid file type. Please upload a JSON file.')
            return redirect(request.url)
    reports = get_reports()
    return render_template('dashboard.html', reports=reports)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
