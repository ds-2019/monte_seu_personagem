from flask import Flask
from flask import render_template, request
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
import numpy as np
import json
import ast


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/personagem', methods=['POST'])
def personagem():
    personagem = request.form
    personagem = personagem.copy()
    train = trainning(personagem)
    personagem['salario'] = train
    return render_template('/personagem.html', personagem=personagem)
if __name__ == '__main__':
    app.run(host='0.0.0.0')

def trainning(personagens):
    personagem = personagens.copy()

    data = {}
    for i in personagem:
        data[i] = personagem[i] if not personagem[i].isdigit() else float(personagem[i])

    df = pd.read_csv('./static/all.csv')
    df.fillna(0, inplace=True)
    neigh = KNeighborsRegressor(n_neighbors=2)

    X = df.iloc[:,:-1]
    y = df.iloc[:,-1]    
    xn = np.array(X)
    yn = nc = np.array(y)

    neigh.fit(xn,yn)
    race_gender = data["personagem"].split(" ")

    if(race_gender[0] == "Homem"):
        if(race_gender[1] == "Branco"):
            race = 1
        gender = 1
    elif(race_gender[0] == "Mulher"):
        if(race_gender[1] == "Branca"):
            race = 16
        gender = 2

    if(race_gender[0] == "Homem"):
        if(race_gender[1] == "Negro"):
            race = 2
        gender = 1
    elif(race_gender[0] == "Mulher"):
        if(race_gender[1] == "Negra"):
            race = 4
        gender = 2

    valorPersonagem = pd.DataFrame({
        "education": [data['escolaridade']],
        "race": [race],
        "gender": [gender],
        "age": [data['idade']]
    })

    nc = np.array(valorPersonagem)
    result = neigh.predict(nc)

    print('\n\n\n', result, '\n\n\n')

    return result[0]
