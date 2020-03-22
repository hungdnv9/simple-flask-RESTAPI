from flask import Flask, jsonify, request, abort, make_response
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Roles(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20), nullable=False)
	group = db.Column(db.String(20), nullable=False)

	def __repr__(self):
		return f"Roles('{self.name}', '{self.group}')"


@app.route('/', methods=['GET'])
def home():
	return 'Hello Flask API'

@app.route('/api/v1/resources/roles', methods=['GET'])
def roles():
	result = []
	roles = Roles.query.all()
	for role in roles:
		result.append(
			{
				'id': role.id,
				'name': role.name,
				'group': role.group
			}
		)
		
	return jsonify(result)

#curl -X GET http://127.0.0.1:5000/api/v1/resources/roles/1
@app.route('/api/v1/resources/roles/<int:id>', methods=['GET'])	
def roles_get(id):
	role = Roles.query.get(id)
	if not role:
		abort(404)
	return jsonify(
		{
			'id': role.id,
			'name': role.name,
			'group': role.group
		}
	)			

# curl -i -H "Content-Type: application/json" -X POST -d '{"name":"Project Manager", "group": "PM"}' http://127.0.0.1:5000/api/v1/resources/roles
@app.route('/api/v1/resources/roles', methods=['POST'])	
def roles_add():
	if not request.json:
		abort(400)
	role = Roles(name=request.json.get('name'), group=request.json.get('group'))
	db.session.add(role)
	db.session.commit()

	role = {		
		'name': request.json.get('name'),
		'group': request.json.get('group')
	}

	return jsonify({'role': role, 'status': 'susccess'}), 201

# curl -i -H "Content-Type: application/json" -X POST -d '{"name":"Project Manager", "group": "PM"}' http://127.0.0.1:5000/api/v1/resources/roles/1
@app.route('/api/v1/resources/roles/<int:id>', methods=['PUT'])	
def roles_update(id):
	role = Roles.query.get(id)
	if not request.json:
		abort(400)
	if not role:
		abort(404)

	role.name = request.json.get('name', role.name)
	role.group = request.json.get('group', role.group)
	db.session.commit()
	
	role = {		
		'name': request.json.get('name', role.name),
		'group': request.json.get('group', role.group)
	}	
	
	return jsonify({'role': role, 'status': 'susccess'})	


# curl -X DELETE http://127.0.0.1:5000/api/v1/resources/roles/0
@app.route('/api/v1/resources/roles/<int:id>', methods=['DELETE'])	
def roles_delete(id):
	msg = [
		{
			'action': 'delete',
			'id': id,
			'status': 'susccess'
		}
	]
	role = Roles.query.get(id)
	if not role:
		abort(404)
	db.session.delete(role)
	db.session.commit()

	return jsonify(msg)			
	

@app.errorhandler(404)
def retrun_404(error):
	return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
	app.run()