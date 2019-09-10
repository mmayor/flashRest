"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from models import db
from models import Recetas, Contacts

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/contact', methods=['GET'])
def handle_person():

    response_body = {
        "ingredients": "tomatte, fish"
    }

    return jsonify(response_body), 200

@app.route('/recetas', methods=['GET'])
def handle_recetas():

    recetasTemp = Recetas()


    ## UPDATE DATA


    receta2 = Recetas.query.get(5)
    if receta2 is None:
        raise APIException('User not found', status_code=404)

    ##if "name" in body:
    receta2.name = 'newName'
    ##if "label" in body:
    receta2.label = 'newLabel'
    db.session.commit()


    ## DELETE DATA
    '''
    receta3 = Recetas.query.get(6)
    if receta3 is None:
        raise APIException('User not found', status_code=404)
    db.session.delete(receta3)
    db.session.commit()
    '''
    ## Inserting data

##    Asuming you have a Person object in your models.py file.

    '''
    receta1 = Recetas(name="colPaella", label="colPaella@email.com")
    db.session.add(receta1)
    db.session.commit()
    '''


    # get all the people
    recetas_query = recetasTemp.query.all()
    # get only the ones named "Joe"
    receta_query = recetasTemp.query.filter_by(name='pollo')
    # map the results and your list of people its now inside all_people variable
    all_recetas = list(map(lambda x: x.serialize(), recetas_query))

    return jsonify(all_recetas), 200

##CONTACTS


#DELETE A CONTACT
@app.route('/delete_contact/<int:contact_id>', methods=['DELETE'])
def delete_person(contact_id):
    user1 = Contacts.query.get(contact_id)
    if user1 is None:
        raise APIException('User not found', status_code=404)
    db.session.delete(user1)
    db.session.commit()
    return "ok", 200


##UPDATE Contacts

#UPDATE A CONTACT
@app.route('/update_contact/<int:contact_id>', methods=['PUT'])
def update_contact(contact_id):
    body = request.get_json(contact_id)
    user1 = Contacts.query.get(contact_id)
    if user1 is None:
        raise APIException('User not found', status_code=404)
    if "full_name" in body:
        user1.full_name = body["full_name"]
    if "email" in body:
        user1.email = body["email"]
    if "agenda_slug" in body:
        user1.agenda_slug = body["agenda_slug"]
    if "address" in body:
        user1.address = body["address"]
    if "phone" in body:
        user1.phone = body["phone"]
    db.session.commit()
    return jsonify(user1.serializeContact()), 200

##ADD Contacts

#ADD A CONTACT
@app.route('/add_contact', methods=['POST'])
def add_contact():
    body = request.get_json()
    user1 = Contacts(full_name=body["full_name"], email=body["email"], agenda_slug=body["agenda_slug"], address=body["address"], phone=body["phone"])
    db.session.add(user1)
    db.session.commit()
    return "ok", 200

## GET CONTACT
@app.route('/contactsNew', methods=['GET'])
def handle_contacts():

        contactsTemp = Contacts()


        ## UPDATE DATA

        '''
        receta2 = Recetas.query.get(5)
        if receta2 is None:
            raise APIException('User not found', status_code=404)

        ##if "name" in body:
        receta2.name = 'newName'
        ##if "label" in body:
        receta2.label = 'newLabel'
        db.session.commit()
            '''

        ## DELETE DATA
        '''
        receta3 = Recetas.query.get(6)
        if receta3 is None:
            raise APIException('User not found', status_code=404)
        db.session.delete(receta3)
        db.session.commit()
        '''
        ## Inserting data

    ##    Asuming you have a Person object in your models.py file.

        '''
        receta1 = Recetas(name="colPaella", label="colPaella@email.com")
        db.session.add(receta1)
        db.session.commit()
        '''


        # get all the people
        contacts_query = contactsTemp.query.all()
        # get only the ones named "Joe"
        # receta_query = recetasTemp.query.filter_by(name='pollo')
        # map the results and your list of people its now inside all_people variable
        all_contacts = list(map(lambda x: x.serializeContact(), contacts_query))

        return jsonify(all_contacts), 200


# this only runs if `$ python src/main.py` is exercuted
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT)
