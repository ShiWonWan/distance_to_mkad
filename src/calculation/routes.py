from flask import Blueprint, jsonify, request
from .operations import getDistanceInKM
import logging
import json

# BLUEPRINT CONFIGS
calculation = Blueprint('calculation', __name__, url_prefix='/calculation')

# Logging config for INFO
logging.basicConfig(filename = 'distances.log', format='%(asctime)s - %(message)s', level=logging.INFO)

@calculation.route('/getdistance', methods=['POST'])
def getDistance():

    # CACHING ERRORS
    if not request.json["address"]:
        return jsonify({"ERROR" : "Please enter an address"})

    if not request.is_json:
        return jsonify({"ERROR" : "Please enter a valid JSON"})

    # GET THE LOWER DISTANCE
    reponse = getDistanceInKM(request.json["address"])
    
    distance = f"{reponse} Km"

    # Saving the distance as INFO
    logging.info("Distance to the MKAD: "+distance)
    # RETURN THE LOWER DISTANCE
    return jsonify({"distance" : distance}) if reponse else jsonify({"distance" : "It's inside the MKAD"})