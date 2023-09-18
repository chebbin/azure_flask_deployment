from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')


df = pd.read_csv('https://raw.githubusercontent.com/chebbin/azure_flask_deployment/main/ComprehensiveJR.csv')
@app.route('/data')
def data(data=df):
    data = data.sample(15)
    return render_template('data.html', data=data)

@app.route('/chart')
def chartpage():
    df = pd.read_csv ('https://raw.githubusercontent.com/chebbin/azure_flask_deployment/main/ComprehensiveJR.csv')
    return render_template('chart.html', chart = df)



if __name__ == '__main__':
    app.run(
        debug=True,
        port=8080
    )