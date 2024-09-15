from django.http import HttpResponse
import pymongo
from bson.json_util import dumps

client = pymongo.MongoClient('mongodb+srv://matveevanataskype:yfnfif9797@cluster0.700pg.mongodb.net/')

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello and welcome to my <u>Django App</u> project!</h1>")

def get_users(request):
    dbname = client['mongodatabase'] 
    collection = dbname['auth_user']
    users = collection.find({})
    json_data = dumps(list(users))
    return HttpResponse(json_data)
    