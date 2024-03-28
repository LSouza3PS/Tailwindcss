from flask import Flask, render_template

meu_app = Flask(__name__)

@meu_app.route('/')
def index():
    return render_template('home.html')
    
@meu_app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    meu_app.run(debug=True)