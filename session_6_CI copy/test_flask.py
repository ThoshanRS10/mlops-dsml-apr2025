import pytest

from hello import pancakes
# pancakes is the name of the flask app in hello.py file.

# this is for deployment, we need to create a test client for the flask app.
# this is a test client that we can use to test the flask app.
@pytest.fixture #this is a decorator that tells pytest that this function is a fixture.
# this is a function that will be run before each test function to set up the test environment.
def client(): #this function client will deploy our flask app.
	return pancakes.test_client()
    # this is like a url(endpoint) which we can use to test the flask app.
#pytest.texture is a special decorater which we need to attach it to the client function so that it can use this as an URL/ endpoint which we can then use to test our endpoints
#here, we're creating a resource and
#we're using the test_client() method to create a test client for the flask app , /hello is the endpoint with GET request.


#testing "hello" function
def test_put_any_name_here(client):
	response = client.get('/hello')# GET request to the /hello endpoint.
	assert response.status_code == 200 #check status code of the response.
    # 200 is the status code for success.
	#assert response.data == {"message": "Hello, World!"}
	assert response.json == {"message": "Hello, World!"}
	


def test_predict(client):
    #copy the payload from POSTMAN 
	payload1 = { "Gender": "Male", "Married": "Unmarried", "Credit_History": "Cleared Debts", "ApplicantIncome": 50000, "LoanAmount": 500000000 }

	response = client.post('/predict', json=payload1) #POST request

	assert response.status_code == 200  
	assert response.json == {"loan_approval_status": "Loan Rejected"}, "payload1 failed"
	# this "loan_approval_status": "Loan Rejected" is also copied from POSTMAN.
	
# when we deploy any model, our pytest can execute a series of this payload and make sure that all of them work good.

	payload2 = { "Gender": "Male", "Married": "Unmarried", "Credit_History": "Cleared Debts", "ApplicantIncome": 50000, "LoanAmount": 5 }

	response = client.post('/predict', json=payload2)
	assert response.status_code == 200
	assert response.json == {"loan_approval_status": "Loan Approved"}, "payload2 failed"


# Why this issue?? UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names
#  Issue is in the way the model was trained and the way the data is being passed to the model for prediction.
# this is a warning and not an error.