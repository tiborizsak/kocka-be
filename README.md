# Kocka project backend
## Data - Response sent from backend
```json
[{
"playerName" : "Elso jatekos",
"roundScore" : 10,
"totalScore" : 23,
"isActive" : true,
"roll": 1
},
{
"playerName" : "Masodik jatekos",
"roundScore" : 6,
"totalScore" : 32,
"isActive" : false,
"roll": 1
}]
```
## Data - Request sent from backend
```json
{
"command" : "dice",
}
```
```json
{
"command" : "hold",
}
```
## flask-cors
```python
from flask_cors import CORS, cross_origin

CORS(app)

CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@cross_origin()

@app.after_request
def after_request(response):
     response.headers.add('Access-Control-Allow-Origin', 'http://localhost:8080')
     response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
     response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
     response.headers.add('Access-Control-Allow-Credentials', 'true')
     return response
```
