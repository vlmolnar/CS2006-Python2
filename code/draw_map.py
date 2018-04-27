import csv
import os
import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

class toMap:

    def setMap(self):
        # --- get the countires and number of users---------
        filename = '../data/locations.csv'
        num_users = []
        country_names = []

        with open(filename, "r") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if (str(row[0]) == "Russia") :
                    country_names.append("Russian Federation")
                else:
                    country_names.append(str(row[0]))
                num_users.append(int(row[1]))

        most_popular = num_users[0]

        # --- Build Map ---
        cmap = mpl.cm.Blues

        # --- Using the shapereader ---
        shapename = 'admin_0_countries'
        countries_shp = shpreader.natural_earth(resolution='110m',
                                                category='cultural', name=shapename)

        # --- Fill Map ---
        ax = plt.axes(projection=ccrs.Robinson())
        for country in shpreader.Reader(countries_shp).records():
            name = country.attributes['NAME_LONG']
            if name in country_names:
                index = country_names.index(name)
                num = num_users[index]
                ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                                  facecolor=cmap(num / float(most_popular), 1),
                                  label=name)

            else:
                ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                                  facecolor='#FAFAFA',
                                  label=name)

        plt.show()


def main():
    m = toMap()
    m.setMap()

# For if this module is ran from the command line
if __name__ == "__main__":
    print("If locations.csv does not exist, run location.py -k <apikey_filename>")
    main()
