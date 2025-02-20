from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
  return render_template('cmsc.html')


if __name__ == '__main__':  # Makes sure this is the main process by python app.py
  app.run(host='0.0.0.0', debug=True)
