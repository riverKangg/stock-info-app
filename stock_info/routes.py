from flask import render_template
from stock_info import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return 'About Us'

# 더 많은 라우트 및 뷰 함수 추가 가능
