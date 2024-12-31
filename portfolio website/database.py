from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlite3
import tkinter as tk
from tkinter import messagebox

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contactus')
def redirect():
    return render_template('contact.html')

@app.route('/home')
def redirect1():
    return render_template('index.html')

@app.route('/services')
def redirect3():
    return render_template('services.html')

@app.route('/about')
def redirect4():
    return render_template('about.html')

# @app.route('/sample')
# def redirect5():
#     return render_template('../images/team.jpeg')



"""
# Image
@app.route('/img')
def redirect2():
    return render_template('../images/Hal-removebg-preview.png')"""

database = 'Dataset.db'
conn = sqlite3.connect(database)
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS contactdata (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT, email TEXT, message TEXT)''')

conn.commit()
conn.close()


@app.route('/contact_form', methods=['POST'])
def contact_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO contactdata (name, email, message) VALUES (?, ?, ?)", (name, email, message))
        conn.commit()
        conn.close()
        return render_template('contact.html', success=True)
        messagebox.showinfo("Success", "Message sent successfully!")
    return render_template('contact.html')
    messagebox.showerror("Error", "An error occurred while sending the message.")


if __name__ == '__main__':
    app.run(port=1000)