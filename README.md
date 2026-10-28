## REPOSITORY: flask_api_assignment

### 🎯 Requirements

## PROGRAM: app.py
A flask api that uses endpoints to get or post data

## ENDPOINTS:
- hello, greets a traveler using name provided
- coinbal, returns the current coin balance based on name provided
- sum, gives the total sum of the numbers provided

### 🚀 Run Instructions
Open a terminal to run each command with appropriate values

curl "http://127.0.0.1:5000/hello?name=Cassie"   #hello greeting
curl "http://127.0.0.1:5000/coinbal?name=grover"  #coinbal
curl -X POST http://127.0.0.1:5000/sum -H "Content-Type: application/json" -d "{\"numbers\": [1, 2, 3]}"  # sum

### ⚠️ Assumptions 
That users are very unlikely to be under 10 years of age or over 110. 

### 🔬 Testing

5 successful tests and output of 6 confirmed

