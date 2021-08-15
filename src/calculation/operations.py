import requests
from decouple import config
from .destinations import each_km # IMPORT ARRAY OF EACH KM

# GET THE SECRET API KEY FROM .env
API_KEY = config('API_KEY')

# GET COORDINATIS FROM AN ADDRESS
def getCoordinates(address):
    API_URL = f"https://api.openrouteservice.org/geocode/search?api_key={API_KEY}&text={address}"

    reponse = requests.get(API_URL)
    json_reponse = reponse.json()

    coordinates = json_reponse["features"][0]["geometry"]["coordinates"]

    # RETURN RESULT OF COORDINATES
    return coordinates

# GET THE LOWER DISTANCE FROM ADDRESS TO THE MKAD
def getDistanceInKM(address):

    # GET COORDINATES FROM ADDRESS
    coordinates = getCoordinates(address)

    # KNOW IF THE ADDRESS IS ON THE MKAD
    if coordinates in each_km:
        return 0
        
    # ADD COORDINATES TO ARRAY
    each_km.append(coordinates)

   

    # CREATE BODY
    body = {
        "locations" : each_km,
        "destinations" : [len(each_km)-1],
        "metrics":["distance"],
        "units":"km"
        }
    headers = {
        'Content-Type' : 'application/json',
        'Authorization' : API_KEY,
        'Accept' : 'application/json'
    }

    API_URL = f"https://api.openrouteservice.org/v2/matrix/driving-car"

    # MAKE POST
    reponse = requests.post(API_URL, json=body, headers=headers)
    # GET LOWER DISTANCE AND RETURN IT
    distances = reponse.json()["distances"]
    distances.pop(len(distances)-1)
    lower_distance = min(distances)
    
    return lower_distance[0]