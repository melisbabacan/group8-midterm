from flask import Flask
 
app = Flask(__name__)
 
@app.route("/hello")

def hello():

    return "Hello! Favorite City Counter API"
 
if __name__ == "__main__":

    app.run(port=5000)

 @app.route("/cities")
def cities():
    return "Cities endpoint"