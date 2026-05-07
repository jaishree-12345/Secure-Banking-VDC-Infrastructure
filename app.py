from flask import Flask, render_template, request, session, redirect
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'bank_security_vault'

def init_db():
    conn = sqlite3.connect('bank.db')
    c = conn.cursor()
    c.execute('DROP TABLE IF EXISTS users')
    c.execute('CREATE TABLE users (user TEXT, pass TEXT, bal REAL, acc_no TEXT)')
    c.execute("INSERT INTO users VALUES ('admin', 'password123', 52450.75, 'VDC-BNK-9920')")
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    u, p = request.form.get('u'), request.form.get('p')
    conn = sqlite3.connect('bank.db')
    c = conn.cursor()
    # SQL INJECTION VULNERABILITY (For the IDS demo)
    query = f"SELECT * FROM users WHERE user='{u}' AND pass='{p}'"
    user = c.execute(query).fetchone()
    if user:
        session['user'] = user[0]
        session['bal'] = user[2]
        session['acc'] = user[3]
        return redirect('/dashboard')
    return "<h1>VDC BANK: ACCESS DENIED</h1>"

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/transactions')
def transactions():
    return render_template('transactions.html')

@app.route('/transfer')
def transfer():
    return render_template('transfer.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
