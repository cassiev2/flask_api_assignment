from app import app  # bring in your Flask app from app.py

client = app.test_client()  # a pretend browser that talks to your app directly


def test_hello_without_name():
    response = client.get("/hello")  # call the route
    assert response.status_code == 200  # check the status code
    assert "message" in response.get_json()  # check the JSON has a message


def test_hello_nameCassie():
    response = client.get("/hello?name=Cassie")  # call the route
    assert response.status_code == 200  # check the status code
    assert (
        "Cassie" in response.get_json()["message"]
    )  # check the greeting includes the name


def test_coinbal_grover():
    response = client.get("/coinbal?name=Grover")  # call the route
    assert response.status_code == 200  # check the status code
    assert response.get_json()["coinbal"] == 150  # check the JSON has a message


def test_sum_test123_6():
    response = client.post("/sum", json={"numbers": [1, 2, 3]})  # call the route
    assert response.status_code == 200  # check the status code
    assert response.get_json()["sum"] == 6  # check the total is 6


def test_sum_nonumberskey():
    response = client.post("/sum", json={"num": [1, 2, 3]})  # call the route
    assert response.status_code == 400  # check the status code
    assert (
        "expected dataset not provided" in response.get_json()["error"]
    )  # check the error for dataset not provided
