import requests
from pymongo import MongoClient



def getShelter():
    shelter_request_link = "https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Public_Service_WebMercator/MapServer/25/query?where=1%3D1&outFields=*&outSR=4326&f=json"
    response = requests.get(shelter_request_link).json()
    return "https://www.google.com/maps?q=" + response['features'][0]['attributes']['ADDRESS']

# def womenShelter():
#     shelter_request_link = "https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Public_Service_WebMercator/MapServer/25/query?where=1%3D1&outFields=*&outSR=4326&f=json"
#     women = requests.get(shelter_request_link).json()
#     if users.find({"gender": "Women"}) :
#         return women['features'][0]['attributes']['ADDRESS']
#         return women['features'][7]['attributes']['ADDRESS']
#         return women['features'][9]['attributes']['ADDRESS']
#         return women['features'][12]['attributes']['ADDDRESS']
#         return women['features'][14]['attributes']['ADDRESS']

def womenShelter():
    women_user = list(users.find({"gender": women})) 
    for number in women_user:
        print ((number))