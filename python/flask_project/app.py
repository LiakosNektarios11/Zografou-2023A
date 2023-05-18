from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!!!</p>"

@app.route("/about")
def about():
    return """<h1>About page!</h1>
    
              <p>This page is about us</p>"""
    



if __name__ == '__main__':
    app.run(debug=True)

