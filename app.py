from flask import Flask
from flask import render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/personagem', methods=['POST'])
def personagem():
    personagem=request.form
    return render_template('personagem.html', personagem=personagem)
if __name__ == '__main__':
    app.run(host='0.0.0.0')
