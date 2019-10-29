import string
from datetime import datetime
from random import choices
from .extensions import db 

class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(512))
    shorten_url = db.Column(db.String(14), unique=True)
    visits = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.now)

    #  inheritance
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.shorten_url = self.create_short_link()

    def create_short_link(self):
        characters = string.digits + string.ascii_letters 
        shorten_url = ''.join(choices(characters, k=14))

        link = self.query.filter_by(shorten_url=shorten_url).first()

        if link: 
           return self.create_short_link

        return shorten_url


