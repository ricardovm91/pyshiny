from flask import Flask
from flask import request
import env
import psycopg2
app = Flask(__name__)
env.init()

def validateToken():
	answer = ""
	serverToken = env.token

	try:
		requestToken = request.headers['token']
	except:
		requestToken = "Deny"
	
	if requestToken == serverToken:
		answer = "Allow"
	else:
		answer = "Deny"

	return(answer)

@app.route("/")
def isAlive():
    return "Server is alive!"

@app.route("/myroute", methods=['GET', 'POST'])
def myRouteFunction():
	auth = validateToken()
	if auth == "Deny":
		return str("Access Denied")
	else:
		# Run the necessary code for you shiny app to consume, then return.
		# conn_string = f"host='{env.host}' dbname='{env.db}' user='{env.usr}' password='{env.pwd}'"
		# conn = psycopg2.connect(conn_string)
		# cursor = conn.cursor()
		# cursor.execute("SELECT * FROM my_table")
		# records = cursor.fetchall()
		return str(auth)

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
