from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Recetas(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(80), unique=True, nullable=False)
     label = db.Column(db.String(120), unique=True, nullable=False)


     def __repr__(self):
         return '<Recetas %r>' % self.name

     def serialize(self):
         return {
             "name": self.name,
             "label": self.label
         }

class Contacts(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        full_name= db.Column(db.String(80), unique=True, nullable=False)
        email= db.Column(db.String(80), unique=True, nullable=False)
        agenda_slug= db.Column(db.String(80), unique=False, nullable=False)
        address= db.Column(db.String(80), unique=False, nullable=False)
        phone= db.Column(db.String(80), unique=False, nullable=False)

        def __repr__(self):
            return '<Contacts %r>' % self.full_name

        def serializeContact(self):
            return {
             "id": self.id,
             "full_name": self.full_name,
             "email": self.email,
             "agenda_slug": self.agenda_slug,
             "address": self.address,
             "phone": self.phone
         }
