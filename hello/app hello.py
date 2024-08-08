from flask import Flask, render_template

app = Flask(__name__) #referencing this file

@app.route('/') #passing the url string, this is the default

def index(): #defining a function for the route
    return 'hello world'

@app.route('/<name>') #takes the name as an input from the route

def print_name(name):
    return 'Hi, {}'.format(name)


if __name__ == "__main__":
    app.run(debug= True)