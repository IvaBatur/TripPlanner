from flask import Flask, request, jsonify, render_template
from models import db, Destination

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///destinations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/destinations')
def get_destinations():
    destinations = Destination.query.all()
    return render_template('destinations.html', destinations=destinations)

@app.route('/interesting')
def interesting():
    return render_template('interesting.html')

@app.route('/add_destination', methods=['POST'])
def add_destination():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No input data provided'}), 400
    
    destination_name = data.get('name')
    description = data.get('description')
    location = data.get('location')
    date = data.get('date')
    
    if not Destination.query.filter_by(name=destination_name).first():
        new_destination = Destination(
            name=destination_name,
            description=description,
            location=location,
            date=date
        )
        db.session.add(new_destination)
        db.session.commit()
    
    destinations = Destination.query.all()
    return jsonify([{
        'name': d.name,
        'description': d.description,
        'location': d.location,
        'date': d.date
    } for d in destinations])

@app.route('/remove_destination', methods=['POST'])
def remove_destination():
    data = request.get_json()
    destination_name = data.get('name')
    destination = Destination.query.filter_by(name=destination_name).first()
    if destination:
        db.session.delete(destination)
        db.session.commit()
    
    destinations = Destination.query.all()
    return jsonify([{
        'name': d.name,
        'description': d.description,
        'location': d.location,
        'date': d.date
    } for d in destinations])

@app.route('/search_destination', methods=['GET'])
def search_destination():
    query = request.args.get('query', '')
    results = Destination.query.filter(Destination.name.ilike(f'%{query}%')).all()
    return jsonify([{
        'name': d.name,
        'description': d.description,
        'location': d.location,
        'date': d.date
    } for d in results])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
