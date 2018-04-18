import csv
import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

class toMap:

    def setMap(self):
        # --- Save Countries,users---------
        filename = 'location.csv'
        counties = []

        with open(filename) as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                counties.append((str(row[0]), int(row[1])))

        most_popular = countries[0][1]

        # --- Build Map ---
        cmap = mpl.cm.Blues

        # --- Using the shapereader ---
        test = 0
        shapename = 'admin_0_countries'
        countries_shp = shpreader.natural_earth(resolution='110m',
                                                category='cultural', name=shapename)

        ax = plt.axes(projection=ccrs.Robinson())
        for country in shpreader.Reader(countries_shp).records():
            name = country.attributes['name_long']
            if name in counties[0]:
                index = counties[0].index(name)
                num = counties[index]
                ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                                  facecolor=cmap(num / float(most_popular), 1),
                                  label=name)
                test =+ 1

            else:
                ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                                  facecolor='#FAFAFA',
                                  label=nome)

        if test != len(counties):
            print("check the way you are writing your country names!")

        plt.show()


def main():
    m = toMap()
    m.setMap()
