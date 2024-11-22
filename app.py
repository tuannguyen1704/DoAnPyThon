from flask import Flask, render_template
from model import select_data

app = Flask(__name__)

@app.route('/')
def index():
    data = select_data()  
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)
