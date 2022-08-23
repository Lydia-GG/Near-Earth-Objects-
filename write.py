import csv
import json

from helpers import datetime_to_str


def write_to_csv(results, filename):

    fieldnames = ('datetime_utc', 'distance_au', 'velocity_km_s',
                  'designation', 'name', 'diameter_km',
                  'potentially_hazardous')

    with open(filename, "w") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(fieldnames)
        for result in results:
            result.neo.name = result.neo.name \
              if result.neo.name is not None else ""
            result.neo.diameter = result.neo.diameter \
                if result.neo.diameter is not None else ""

            data = [result.time, result.distance, result.velocity,
                    result._designation, result.neo.name,
                    result.neo.diameter, result.neo.hazardous]

            writer.writerow(data)


def write_to_json(results, filename):

    with open(filename, "w") as outfile:
        data = []
        for result in results:
            result.neo.name = result.neo.name \
              if result.neo.name is not None else ""
            result.neo.diameter = result.neo.diameter \
                if result.neo.diameter is not None else float("nan")
            result.neo.hazardous = bool(True) \
                if result.neo.hazardous else bool(False)

            result_data = {
                            "datetime_utc": datetime_to_str(result.time),
                            "distance_au": float(result.distance),
                            "velocity_km_s": float(result.velocity),
                            "neo": {
                              "designation": str(result.neo.designation),
                              "name": result.neo.name,
                              "diameter_km": result.neo.diameter,
                              "potentially_hazardous": result.neo.hazardous
                            }
                          }

            data.append(result_data)
        json.dump(data, outfile, indent=2)


