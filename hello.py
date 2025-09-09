from flask import Flask, render_template

# テンプレートとCSSのパスを指定（これがあると静的ファイルも読み込める）
TEMPLATE_PATH = 'templates'
STATIC_PATH = 'static'

app = Flask(__name__, template_folder=TEMPLATE_PATH, static_folder=STATIC_PATH)

@app.route("/")
def home():
    return render_template('home.html')

