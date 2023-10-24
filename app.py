from flask import Flask, render_template

app = Flask(__name__)

# 루트 URL에 대한 뷰 함수
@app.route('/')
def index():
    return render_template('index.html', message="Welcome to the Stock Info App")

# "about" URL에 대한 뷰 함수
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
