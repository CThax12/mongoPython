from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
print('test')
uri = "mongodb+srv://cthax12:connor13@clustect.dqeuqt9.mongodb.net/?retryWrites=true&w=majority&appName=ClusteCT"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Ping!")
except Exception as e:
    print(e)

db = client['ClusteCT']['grades']
db.insert_many(
[
    {
        "student_id": 546789,
        "products": [
            {
                "type": "quiz",
                "score": 50
            },
            {
                "type": "homework",
                "score": 70
            },
            {
                "type": "quiz",
                "score": 66
            },
            {
                "type": "exam",
                "score": 70
            }
        ],
        "class_id": 551
    },
    {
        "student_id": 777777,
        "products": [
            {
                "type": "exam",
                "score": 83
            },
            {
                "type": "quiz",
                "score": 59
            },
            {
                "type": "quiz",
                "score": 72
            },
            {
                "type": "quiz",
                "score": 67
            }
        ],
        "class_id": 550
    },
    {
        "student_id": 223344,
        "products": [
            {
                "type": "exam",
                "score": 45
            },
            {
                "type": "homework",
                "score": 39
            },
            {
                "type": "quiz",
                "score": 40
            },
            {
                "type": "homework",
                "score": 88
            }
        ],
        "class_id": 551
    }
]

)