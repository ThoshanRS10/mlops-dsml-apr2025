#pip install flask

from flask import Flask, jsonify, request

#create the name of the app
pancakes = Flask(__name__)

# create a simple hello route
# pancakes.route is a decorator that tells Flask what the URL ( /hello) should call the function below it ( {"message":"Hello, World!"} ).
# when ever we get a traffic on the URL /hello, it will call the function hello() below it.
# the function hello() will return a JSON response with the message "Hello, World!".
# the function hello() is a view function that handles the request and returns a response.
@pancakes.route('/hello', methods=['GET']) #/hello is the endpoint. Endpoint is the URL inside our API that the client will use.
def hello():
    """"
    A simple hello world endpoint.
    This endpoint returns a JSON response with a message "Hello, World!".
    It is a GET request, meaning it retrieves data from the server.
    """
    return ({"message": "Hello, World!"})

# when we go to the URL /hello, we will get a JSON response with the message "Hello, World!".
# this only has one URL - /hello.
# in cmd,  flask --app hello.py run
# this will run the app on localhost:5000 by default.
# copy the url and paste it in the browser, we get url not found because we haven't created for that url.
# url/hello will give us the hello world message.
#  http://127.0.0.1:5000/hello
# {"message":"Hello, World!"}, notice the structure of the response is JSON. It is neat/easy for a backend dev to work on.
# API will not change because it's running on our local machine.
# in the cmd terminal, we can see the request and response.
# we can also see the request method, which is GET in this case.
# 127.0.0.1 - - [06/May/2025 21:35:32] "GET / HTTP/1.1" 404 -
#127.0.0.1 - - [06/May/2025 21:35:32] "GET /favicon.ico HTTP/1.1" 404 -
#127.0.0.1 - - [06/May/2025 21:35:51] "GET /hello HTTP/1.1" 200 -

# in this URL, we have nothing to serve, no function is serving anything, which is why we get a 404 error.

# @pancakes.route('/', methods=['GET']) # only GET request is allowed on this endpoint.
# # in the GET request, when we access the info, that will be visible in he url but not in POST request, it's visible in the request headers file.
# def index():
#     """
#     A simple index endpoint.
#     This endpoint returns a JSON response with a message "Welcome to the Pancakes API!".
#     It is a GET request, meaning it retrieves data from the server.
#     """
#     return ({"message": "Welcome to the Pancakes API!"})

@pancakes.route('/', methods=['GET'])
def index():
	"""
	A very fancy animated webpage with vibrant colors and beautiful animations.
	"""
	return '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vibrant Animation</title>
  <style>
	body {
	  margin: 0;
	  padding: 0;
	  background: linear-gradient(45deg, #ff0066, #ffcc00, #33cc33, #0099ff);
	  background-size: 600% 600%;
	  animation: gradientAnimation 16s ease infinite;
	  font-family: 'Arial', sans-serif;
	  display: flex;
	  justify-content: center;
	  align-items: center;
	  height: 100vh;
	  color: white;
	}
	@keyframes gradientAnimation {
	  0% { background-position: 0% 50%; }
	  50% { background-position: 100% 50%; }
	  100% { background-position: 0% 50%; }
	}
	.content {
	  text-align: center;
	}
	.title {
	  font-size: 3em;
	  margin-bottom: 20px;
	  animation: fadeIn 2s ease backwards;
	}
	.subtitle {
	  font-size: 1.5em;
	  animation: fadeIn 3s ease backwards;
	}
	@keyframes fadeIn {
	  from { opacity: 0; transform: translateY(20px); }
	  to { opacity: 1; transform: translateY(0px); }
	}
  </style>
</head>
<body>
  <div class="content">
	<div class="title">Welcome to AWS!</div>
	<div class="subtitle">Let's learn how to deploy our application in AWS ECS.</div>
  </div>
</body>
</html>
'''

# @pancakes.route('/', methods=['GET'])
# def home():

# 	return '''
# <html>
# <head>
# 	<title>Save Hello</title>
# 	<style>
# 		body {
# 			background: linear-gradient(45deg, #ff9a9e, #fad0c4);
# 			font-family: Arial, sans-serif;
# 			text-align: center;
# 			padding-top: 100px;
# 			margin: 0;
# 		}
# 		h1 {
# 			font-size: 60px;
# 			color: #ffffff;
# 			animation: glow 2s infinite alternate;
# 			margin-bottom: 20px;
# 		}
# 		p {
# 			font-size: 20px;
# 			color: #333;
# 		}
# 		@keyframes glow {
# 			from {
# 				text-shadow: 0 0 10px #fff;
# 			}
# 			to {
# 				text-shadow: 0 0 20px #ff00ff, 0 0 30px #ff00ff;
# 			}
# 		}
# 	</style>
# </head>
# <body>
# 	<h1>Hello There</h1>
# 	<p>Welcome to the beautifully animated page!</p>
# </body>
# </html>
# 	'''

# now we'll create an endpoint which the backend engineer will come to for getting response from the ML model.
# first, we'll train the model and use that.

import joblib

clf = joblib.load('classifier.pkl') # this will load the model from the file classifier.pkl.
# this is the model we trained in the previous step.

@pancakes.route('/predict', methods=['POST']) # POST request is used to send data to the server.
# this is the endpoint where the client will send the data to the server.
def predict(): # this function will be called when the client sends a POST request to the /predict endpoint.
	loan_req = request.get_json() # this will get the data from the client in JSON format, which we will gather and run a model on it.
    # the data will be in the form of a dictionary. 


	if loan_req['Gender'] == "Male": ## this is the data we are getting from the client.
		Gender = 0
	else:
		Gender = 1

	if loan_req['Married'] == "Unmarried":
		Married = 0
	else:
		Married = 1
 
	if loan_req['Credit_History'] == "Uncleared Debts": # Uncleared Debts is from the dataset, for  the user input.
		Credit_History = 0	
	else:
		Credit_History = 1

	ApplicantIncome = loan_req['ApplicantIncome']

	LoanAmount = loan_req['LoanAmount']

	result = clf.predict([[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]]) # this will call the predict method of the classifier and pass the data to it.
    # the predict method will return the result of the prediction.

	if result == 0: # this is the result we are getting from the model.
		result = "Loan Rejected"
	else:
		result = "Loan Approved"
# predict function will take some info and run our ML model on that info and return the result.
	return {"loan_approval_status": result} # this will return the result in JSON format.	 

#how do we send this info to the server? ecause it's a POST request, we need to send the data in the body of the request and not in the URL.
#http://127.0.0.1:5000/predict - The method is not allowed for the requested URL.
# we can use Postman or curl to send the data to the server.
# Postman allows us to create request for all GET and POST and talk to URL


#curl --location 'http://127.0.0.1:5000/predict' \
#--header 'Content-Type: application/json' \
#--data '{
#    "Gender": "Male",
#    "Married": "Unmarried",
#    "Credit_History": "Cleared Debts",
#    "ApplicantIncome": 50000, 
#    "LoanAmount": 500000000