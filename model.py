import requests




def getShelter():
    shelter_request_link = "https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Public_Service_WebMercator/MapServer/25/query?where=1%3D1&outFields=*&outSR=4326&f=json"
    response = requests.get(shelter_request_link).json()
    return "https://www.google.com/maps?q=" + response['features'][0]['attributes']['ADDRESS']


def formResult(users):
    if users.find({"reside" : "NO"}):
        return "Unfortunately, our resource is focused on DC, but here are some resources: "


def womenShelter(users):
    shelter_request_link = "https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Public_Service_WebMercator/MapServer/25/query?where=1%3D1&outFields=*&outSR=4326&f=json"
    women = requests.get(shelter_request_link).json()
    women_list = []
    
    if users.find({"gender": "Women"}) :
        women_list.append(women['features'][0]['attributes']['ADDRESS'])
        women_list.append(women['features'][7]['attributes']['ADDRESS'])
        women_list.append( women['features'][9]['attributes']['ADDRESS'])
        women_list.append(women['features'][12]['attributes']['ADDRESS'])
        women_list.append( women['features'][14]['attributes']['ADDRESS'])
        return women_list

# def womenShelter():
#     women_user = list(users.find({"gender": women})) 
#     for number in women_user:
#         print ((number))