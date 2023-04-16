from flask import Flask
from flask_restful import Resource,Api

class Modulus(Resource): 
	def get(self, number_1, number_2):
		try:
			res=int(number_1) % int(number_2)
			return {'Output': (res)}
		except ZeroDivisionError:
			return {'Output':"Error: Modulo by Zero"}

app = Flask(__name__)
api = Api(app)
api.add_resource(Modulus, '/<number_1>/<number_2>')

if __name__ =="__main__":
	app.run(
		debug=True,
		port=5057,
		host="0.0.0.0"
	)
