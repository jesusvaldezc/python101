# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask, jsonify

app = Flask(__name__, static_url_path="")

@app.route('/json', methods=['GET'])
def ejemplo_json():
    contenido= {"id": 1, "name" : "Jesus", "apellido": "algun apellido"}
    segundo= {"id": 2, "name" : "Jesus", "apellido": "algun apellido"}
    lista = [contenido, segundo]

    return jsonify(lista)

@app.route('/', methods=['GET'])
def helloFlask():
    return 'Hello World!'

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
