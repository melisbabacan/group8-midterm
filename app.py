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

import psycopg2
 
def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="cities",
        user="postgres",
        password="password"
    )
    return conn

@app.route("/cities", methods=["GET"])
def get_cities():
 
    conn = get_db_connection()
    cur = conn.cursor()
 
    cur.execute("SELECT name FROM cities")
    rows = cur.fetchall()
 
    cur.close()
    conn.close()
 
    cities = [row[0] for row in rows]
 
    return jsonify(cities)