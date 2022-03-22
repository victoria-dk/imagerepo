from typing import List, Dict
from flask import Flask, request, render_template
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

def delete_item(title):
    connection = mysql.connector.connect(**DB_conf)
    cursor = connection.cursor()
    request = f"DELETE FROM images WHERE title = '{title}';"
    cursor.execute(request)
    connection.commit()
    cursor.close()
    connection.close()
    return request

def style():
    S  = "<style>\n"
    S += " body {background-color: rgb(189, 160, 216);} table {width: 50%; height:50%; background-color: white; border-radius: 2%; width: 70%; padding: 30px; margin: 20px;} table, th, td {border-collapse: collapse; padding: 10px; border: 5px solid yellowg}\n"
    S += "</style>\n"
    return S

@app.route('/add')
def add():
    title = request.args.get("title", "", str)
    link = request.args.get("link", "", str)
    descript = request.args.get("descript", "", str)
    S  = "<!DOCTYPE html>\n"
    S += "<html>\n"
    S += "  <head>\n"
    S += "      <title>Added a link</title>\n"
    S += style()
    S += "  </head>\n"
    S += "  <body>\n"
    S += "      <h1>Added a link</h1>\n"
    if title != "" and link != "" and descript !="":
        S += add_item(title, link, descript)
    S += "      <p><a href='/'>Back!</a></p>\n"
    S += "  </body>\n"
    S += "</html>\n"
    return S

@app.route('/delete')
def delete():
    title = request.args.get("title", "", str)
    S  = "<!DOCTYPE html>\n"
    S += "<html>\n"
    S += "  <head>\n"
    S += "      <title>Deleted a link</title>\n"
    S += style()
    S += "  </head>\n"
    S += "  <body>\n"
    S += "      <h1>Deleted a link</h1>\n"
    if title != "":
        S += delete_item(title)
    S += "      <p><a href='/'>Back!</a></p>\n"
    S += "  </body>\n"
    S += "</html>\n"
    return S

@app.route('/addform')
def addform():
    S  = "<!DOCTYPE html>\n"
    S += "<html>\n"
    S += "  <head>\n"
    S += "      <title>Entering a value</title>\n"
    S += style()
    S += "  </head>\n"
    S += "  <body>\n"
    S += "      <h1>Entering a value</h1>\n"
    S += "      <form action='/add'>\n"
    S += "          <input type='text' name='title' value='Affenpinscher'/>\n"
    S += "          <input type='text' name='link' value='https://upload.wikimedia.org/wikipedia/commons/2/25/Affenpinscher_dog.jpg'/>\n"
    S += "          <input type='text' name='descript' value='Affenpinscher dog'/>\n"
    S += "          <input type='submit' value='Submit'/>\n"
    S += "      </form>\n"
    S += "  </body>\n"
    S += "</html>\n"
    return S

@app.route('/deleteform')
def deleteform():
    S  = "<!DOCTYPE html>\n"
    S += "<html>\n"
    S += "  <head>\n"
    S += "      <title>Entering a value</title>\n"
    S += style()
    S += "  </head>\n"
    S += "  <body>\n"
    S += "      <h1>Entering a value</h1>\n"
    S += "      <form action='/delete'>\n"
    S += "          <input type='text' name='title' value='Affenpinscher'/>\n"
    S += "          <input type='text' name='link' value='https://commons.wikimedia.org/wiki/File:Affenpinscher_dog.jpg'/>\n"
    S += "          <input type='text' name='descript' value='Affenpinscher dog'/>\n"
    S += "          <input type='submit' value='Submit'/>\n"
    S += "      </form>\n"
    S += "  </body>\n"
    S += "</html>\n"
    return S

@app.route('/')
def index():
    S = "<!DOCTYPE html>\n"
    S += "<html>\n"
    S += "  <head>\n"
    S += "      <title>Images of dogs</title>\n"
    S += style()
    S += "  </head>\n"
    S += "  <body>\n"
    S += "      <h1>Images of dogs</h1>\n"
    S += "          <form action='/delete'>\n"
    S += "              <table>\n"
    for (title, link, descript) in test_table():
        S += f"             <tr><th>Title</th>\n"
        S += f"                 <th>Link (click on image)</th>\n"
        S += f"                 <th>Description</th>\n" 
        S += f"             </tr>\n"
        S += f"             <tr><td>{title}</td>\n"
        S += f"                 <td><a target='blank' href='{link}'><img src='{link}' style='width:150px'></a></td>\n"
        S += f"                 <td>{descript}</td>\n" 
        S += f"                 <td><input type='radio' value='{title}' name='title'/></td>\n" 
        S += f"             </tr>\n"
    #S += "         <tr><td><input type='submit' name='action' value='Delete'></td>\n"
    S += "         </tr>\n"
    S += "              </table>\n"
    S += "         <input type='submit' name='action' value='Delete'>\n"
    S += "        </form>\n"

    S += "      <form action='/add'>\n"
    S += "          <input type='text' name='title' placeholder='Title of the image'/>\n"
    S += "          <input type='text' name='link' placeholder='Place image link'/>\n"
    S += "          <input type='text' name='descript' placeholder='Write description'/>\n"
    S += "          <input type='submit' value='Submit'/>\n"
    S += "      </form>\n"
    S += "  </body>\n"
    S += "</html>\n"
    return S

@app.route('/index')
def index_old():
    S  = "<!DOCTYPE html>\n"
    S += "<html>\n"
    S += "  <head>\n"
    S += "      <title>Images of dogs</title>\n"
    S += style()
    S += "  </head>\n"
    S += "  <body>\n"
    S += "      <h1>Images of dogs </h1>\n"
    S += "      <ul>\n"
    for (title, link, descript) in test_table():
        S += f"        <li>{title}: {link}: {descript}</li>\n"
    S += "      </ul>\n"
    S += "      <p><a href='/addform'>Form!</a></p>\n"
    S += "      <p><a href='/deleteform'>Delete Form!</a></p>\n"
    S += "  </body>\n"
    S += "</html>\n"
    return S

if __name__ == '__main__':
    app.run(host='0.0.0.0')