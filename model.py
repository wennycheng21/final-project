import requests


def getShelter():
    shelter_request_link = "https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Public_Service_WebMercator/MapServer/25/query?where=1%3D1&outFields=*&outSR=4326&f=json"
    response = requests.get(shelter_request_link).json()
    return "https://www.google.com/maps?q=" +response['features'][0]['attributes']['ADDRESS']
    

