from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
  return "Hello Usman!!"

if __name__ == '__main__': # Makes sure this is the main process by python app.py 
  app.run(host='0.0.0.0', debug=True)