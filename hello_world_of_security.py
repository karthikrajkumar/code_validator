from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# Vulnerable to SQL Injection
def get_user_data(username):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    user_data = cursor.fetchall()
    conn.close()
    return user_data

# Vulnerable to Cross-Site Scripting (XSS)
@app.route('/greet', methods=['GET'])
def greet_user():
    username = request.args.get('username')
    return render_template_string(f"<h1>Hello, {username}!</h1>")

# Vulnerable to Insecure Direct Object References (IDOR)
@app.route('/view_file', methods=['GET'])
def view_file():
    file_path = request.args.get('file')
    with open(file_path, 'r') as file:
        content = file.read()
    return content

if __name__ == '__main__':
    app.run(debug=True)
