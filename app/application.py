"""import the flask library and the functions needed from it"""
from flask import Flask
from flask import render_template, request

app = Flask(__name__)


@app.route('/')
def world():
    """This function returns the w.html page"""
    return render_template('w.html')


@app.route('/hello/',methods=['GET', 'POST'])
def hello():
    """This function returns the home.html page"""
    return render_template('home.html')


@app.route('/hello/shortenurl',methods=['GET', 'POST'])
def shortenurl():
    """This function returns the shortenurl.html page"""
    if request.method == 'POST':
        return render_template('shortenurl.html', shortcode =request.form['shortcode'])
    return None

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)