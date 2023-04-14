from flask import Flask
from flask_restful import Resource,Api

class Division(Resource):
    def get(self,number_1,number_2):
        return {'Output':(int(number_1)/int(number_2))}
    
app=Flask(__name__)
api=Api(app)
api.add_resource(Division, '/<number_1>/<number_2>')

if __name__ =="__main__":
	app.run(
		debug=True,
		port=5055,
		host="0.0.0.0"
	)
