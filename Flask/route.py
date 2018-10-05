from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/upload/', methods=['POST'])
def upload():
    if not request.json:
        return 'NOT A FUCKING POST'
    return 'Hello, World!'

@app.route('/upload/snapshot/<filename>', methods=['POST'])
def snapshot(filename):
    if request.method == 'POST':
        f = request.files['files']
        f_name = filename   
        print('\n[+ POST REQ]  /upload/snapshot/ : filename => ' + f_name + '\n')       
        dir_path = os.path.dirname(os.path.realpath(__file__)) + '/uploaded/' + f_name
        f.save(dir_path)
        return '200'
    else:
        return '100'
    return 'SNAPSHOT!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

