import csv
import json

from models import CloseApproach, NearEarthObject


def load_neos(neo_csv_path):

    neos = []
    with open(neo_csv_path, "r") as infile:
        reader = csv.DictReader(infile)
        for elem in reader:
            designation = elem["pdes"]
            name = elem["name"]
            diameter = elem["diameter"]
            hazardous = elem["pha"]
            neos.append(NearEarthObject(designation, name,
                                        diameter, hazardous))

    return neos


def load_approaches(cad_json_path):
    approaches = []
    with open(cad_json_path, "r") as infile:
        contents = json.load(infile)
        for data in contents["data"]:
            designation = data[0]
            time = data[3]
            distance = data[4]
            velocity = data[7]
            approaches.append(CloseApproach(designation, time,
                                            distance, velocity))

    return approaches
