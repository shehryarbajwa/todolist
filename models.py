from sqlalchemy import Column, String, Integer, create_engine, Boolean, Date
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import datetime 
import json

database_name = 'todolistapp'
database_path = 'postgres://{}@{}/{}'.format('shehryarbajwa', 'localhost:5432', database_name)
db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

def db_drop_and_create_all():
    db.drop_all()
    db.create_all()


class Todo(db.Model):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    completed = Column(Boolean, default=False)
    date = Column(Date)

    def __init__(self, title, completed, description, date):
        self.title = title
        self.description = description
        self.completed = completed
        self.date = date

    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def short(self):
        return {
            'id': self.id,
            'title': self.title
        }

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'completed': self.completed,
            'description': self.description,
            'date': self.date
        }
     

if __name__ == '__main__':
    app.run()