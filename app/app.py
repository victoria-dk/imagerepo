from typing import List, Dict
from flask import Flask, request
import mysql.connector
import json

app = Flask(__name__)

DB_conf = {
    'user': 'root',
    'password': 'root',
    'host': 'db',
    'port': '3306',
    'database': 'animals'
}

def test_table():
    connection = mysql.connector.connect(**DB_conf)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM images')
    results = [c for c in cursor]
    cursor.close()
    connection.close()
    return results

def add_item(title, link, descript):
    connection = mysql.connector.connect(**DB_conf)
    cursor = connection.cursor()
    request = f"INSERT INTO images (title, link, descript) VALUES ('{title}', '{link}', '{descript}');"
    cursor.execute(request)
    connection.commit()
    cursor.close()
    connection.close()
    return request

@app.route('/add')
def add():
    title = request.args.get("title", "", str)
    link = request.args.get("link", "", str)
    descript = request.args.get("descript", "", str)
    S  = "<!DOCTYPE html>\n"
    S += "<html>\n"
    S += "  <head>\n"
    S += "      <title>Added a link</title>\n"
    S += "  </head>\n"
    S += "  <body>\n"
    S += "      <h1>Added a link</h1>\n"
    if title != "" and link != "" and descript !="":
        S += add_item(title, link, descript)
    S += "      <p><a href='/'>Back!</a></p>\n"
    S += "  </body>\n"
    S += "</html>\n"
    return S

@app.route('/')
def index():
    S  = "<!DOCTYPE html>\n"
    S += "<html>\n"
    S += "  <head>\n"
    S += "      <title>Images of dogs</title>\n"
    S += "  </head>\n"
    S += "  <body>\n"
    S += "      <h1>Images of dogs </h1>\n"
    S += "      <ul>\n"
    for (title, link, descript) in test_table():
        S += f"        <li>{title}: {link}: {descript}</li>\n"
    S += "      </ul>\n"
    S += "  </body>\n"
    S += "</html>\n"
    return S

if __name__ == '__main__':
    app.run(host='0.0.0.0')