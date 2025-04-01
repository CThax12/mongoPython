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

db = client['ClusteCT']['companies']
db.insert_one(
    {
        'test_id' : 123123
    }
)