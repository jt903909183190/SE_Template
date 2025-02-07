import sqlite3
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def catalogue():
    con = sqlite3.connect('database/data.db')
    cur = con.cursor()
    cur.execute("SELECT name, image, description FROM catalogue")
    data = cur.fetchall()
    print(data)
    con.close()
    return data

@app.route('/index.html', methods=['GET'])
@app.route('/', methods=['POST', 'GET'])
def index():
    data = catalogue()
    return render_template('index.html', cataloguedata=data)

if __name__ == '__main__':
    app.run(debug=True)