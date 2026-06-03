import json
from load_jason import load_json

class person:
    def __init__(self, name, phone_number, email, location="", linkedin=""):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.location = location
        self.linkedin = linkedin

class attributes:
    def __init__(self, type, start_date, end_date, city, location, skills=""):
        self.type = type
        self.start_date = start_date
        self.end_date = end_date
        self.city = city
        self.location = location
        self.skills = skills

def start():
    load_json("data.json")