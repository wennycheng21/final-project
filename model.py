import requests


def getShelter():
    shelter_request_link = "https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Public_Service_WebMercator/MapServer/25/query?where=1%3D1&outFields=*&outSR=4326&f=json"
    response = requests.get(shelter_request_link).json()
    return "https://www.google.com/maps?q=" + response['features'][0]['attributes']['ADDRESS']


def formResult(users):
    if users.find({"reside": "NO"}):
        return "Unfortunately, our resource is focused on DC, but here are some resources: "


def womenShelter(users):
    shelter_request_link = "https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Public_Service_WebMercator/MapServer/25/query?where=1%3D1&outFields=*&outSR=4326&f=json"
    women = requests.get(shelter_request_link).json()
    women_list = []

    if users.find({"gender": "Women"}):
        women_list.append(women['features'][0]['attributes']['ADDRESS'])
        women_list.append(women['features'][7]['attributes']['ADDRESS'])
        women_list.append(women['features'][9]['attributes']['ADDRESS'])
        women_list.append(women['features'][12]['attributes']['ADDRESS'])
        women_list.append(women['features'][13]['attributes']['ADDRESS'])
        return women_list


def menShelter(users):
    shelter_request_link = "https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Public_Service_WebMercator/MapServer/25/query?where=1%3D1&outFields=*&outSR=4326&f=json"
    men = requests.get(shelter_request_link).json()
    men_list = []
    if users.find({"gender": "Men"}):
        men_list.append(men['features'][1]['attributes']['ADDRESS'])
        men_list.append(men['features'][2]['attributes']['ADDRESS'])
        men_list.append(men['features'][4]['attributes']['ADDRESS'])
        men_list.append(men['features'][5]['attributes']['ADDRESS'])
        men_list.append(men['features'][6]['attributes']['ADDRESS'])
        men_list.append(men['features'][8]['attributes']['ADDRESS'])
        men_list.append(men['features'][10]['attributes']['ADDRESS'])
        men_list.append(men['features'][12]['attributes']['ADDRESS'])
        men_list.append(men['features'][14]['attributes']['ADDRESS'])
        men_list.append(men['features'][16]['attributes']['ADDRESS'])
        men_list.append(men['features'][17]['attributes']['ADDRESS'])
        return men_list


def youthShelter(users):
    shelter_request_link = "https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Public_Service_WebMercator/MapServer/25/query?where=1%3D1&outFields=*&outSR=4326&f=json"
    youth = requests.get(shelter_request_link).json()
    youth_list = []
    if users.find({"gender": "Youth"}):
        youth_list.append(youth['features'][11]['attributes']['ADDRESS'])
        return youth_list


def lgbtqShelter(users):
    shelter_request_link = "https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Public_Service_WebMercator/MapServer/25/query?where=1%3D1&outFields=*&outSR=4326&f=json"
    lgbtq = requests.get(shelter_request_link).json()
    lgbtq_list = []
    if users.find({"gender": "LGBTQ"}):
        lgbtq_list.append(lgbtq['features'][3]['attributes']['ADDRESS'])
        lgbtq_list.append(lgbtq['features'][12]['attributes']['ADDRESS'])
        return lgbtq_list



def touplet(n):
    touplet1 = mapTableCategories("Women", "18+")
    return touplet1[n]

def mapTableCategories(gender, age):
    shelter_request_link = "https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Public_Service_WebMercator/MapServer/25/query?where=1%3D1&outFields=*&outSR=4326&f=json"
    attributes = requests.get(shelter_request_link).json()
    number = len(attributes['features'])  # number of shelters in list
    filterShelterList = []
    for num in range(number):
        gender1 = attributes['features'][num]['attributes']['SUBTYPE']
        age1 = attributes['features'][num]['attributes']['AGES_SERVED']
        name1 = attributes['features'][num]['attributes']['NAME']
        address1 = attributes['features'][num]['attributes']['ADDRESS']
        numberofbeds1 = attributes['features'][num]['attributes']['NUMBER_OF_BEDS']
        if gender1 == gender:
            if age1 == age:
                temDictionary = {"number": num + 1, "hyperlink": ('https://www.google.com/maps?q=' + address1.replace(" ", "+")),
                                    "name": name1, 'address': address1, 'numberof_beds': numberofbeds1}
                filterShelterList.append(temDictionary)
            else:
                continue
        else:
            continue
    return filterShelterList
