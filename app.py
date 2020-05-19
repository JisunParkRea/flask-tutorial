from flask import Flask, render_template

# Flask 인스턴스 생성
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True) # app.run(host="127.0.0.1", port="5000", debug=True)
