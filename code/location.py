from collections import Counter
import json
import pandas as pd
import re
import sys
import getopt
import urllib

# API request to Google Maps
#Gets locations from the "results" column of the data set
def getLocationsOfUsers(df, key):
    apiURL = "https://maps.googleapis.com/maps/api/geocode/json?key=" + key + "&latlng=%s&sensor=true/false"

    countries = []
    for coords in df["geo_coordinates"]:
        if pd.notnull(coords) and coords != "loc: 0,0":
            latlong = coords[5:]
            lat, lng = latlong.split(",")
            resp = urllib.request.urlopen(apiURL % latlong)
            data = json.loads(resp.read().decode())
            if len(data["results"]) > 0:
                for location in data["results"][0]["address_components"]:
                    if location["types"][0] == "country":
                        countries.append(location["long_name"])
                        break
    counter = Counter(countries)
    popular = counter.most_common()
    return popular

# This function takes a file name that contains the api key
# It will load the refined data
# It will retrieve the number of users per location
# This data wil lbe written to a new csv to be used @draw_map
def main(keyfile):
    with open("/cs/home/js321/Documents/google_api_key.txt") as f:
        content = f.read()
    df = pd.read_csv("../data/CometLanding_ref.csv")
    popular = getLocationsOfUsers(df, content.strip())
    c, n = zip(*popular)

    loc = pd.DataFrame(data={"location": c, "num_users": n})
    loc.to_csv("../data/locations.csv", sep=',', index= False)

# The handles command line arguements
if __name__ == "__main__":
    keyfile = None
    try:
        opts, args = getopt.getopt(sys.argv[1:], "k:", ["keyfile="])
    except getopt.GetoptError:
        print(err)
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-k", "--keyfile"):
            keyfile = arg
        else:
            usage()
            sys.exit(2)
    main(keyfile)
