from qube.src.api import persist_db

class Hello(persist_db.Document):
    name = persist_db.StringField()

    #def __init__(self, helloInfor): # helloInfo is a dictionary
    #	self.name = helloInfor["name"]

