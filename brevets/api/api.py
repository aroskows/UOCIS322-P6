import os
from flask import Flask
from flask_restful import Resource, Api
from pymongo import MongoClient
import json


app = Flask(__name__)
api = Api(app)


client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
db = client.tododb

mydata = list(db.tododb.find())
#print(mydata)
open_times_list = []
close_times_list = []
all_times_list = []
for i in mydata:
    # i is an dictionary with km, open times, and close times
    open_times_list.append(str(i['open_time'])) 
    close_times_list.append(str(i['close_time']))
    temp = [str(i['open_time']), str(i['close_time'])]
    all_times_list.append(temp) 


   # print("km =", i['km'])
#mykeys = mydata.keys()
#print(mykeys)

class listAll(Resource):
    def get(self, dtype):
        topnum = request.args.get('top', default=-1)
        app.logger("ALL")
        if dtype == "CSV":
            #return in CSV form?
            csv_all = ""
            for i in all_times_list:
                csv_all += ", ".join(i)
                csv_all += "  "



            pass
        else:
            #return in json form
            pass
    

class listOpen(Resource):
    def get(self, dtype):
        app.logger("OPEN")
        topnum = request.args.get('top', default=-1)

        if dtype == "CSV":
            csv_close = ", ".join(open_times_list)
            pass
        else:
            #return in json form
            pass


class listClose(Resource):
    def get(self, topk, dtype):
        #print("hello")
        app.logger.debug("CLOSE")
        topnum = request.args.get('top', default=-1)
        if dtype == "CSV":
            csv_close = ", ".join(close_times_list)
            return 
        else:
            #return in json form
            return [1, 2, 3]

'''@app.route('/listClose'):
    def listClose(topk, dtype):
        app.logger.debug("CLOSE W/ ROUTE")
        if dtype == "JSON":
            app.logger.debug("json")
        return 1 '''

api.add_resource(listAll, '/listAll/<dtype>')
api.add_resource(listOpen, '/listOpen/<dtype>')
api.add_resource(listClose, '/listClose/<topk><dtype>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

