from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route('/')
def mainpage():
    return render_template('base.html')


@app.route('/chart')
def chartpage():
    df = pd.read_csv ('/home/chevi_ebbin/azure_flask_deployment/ComprehensiveJR.csv')
    return render_template('chart.html', chart = df)



if __name__ == '__main__':
    app.run(
        debug=True,
        port=8080
    )