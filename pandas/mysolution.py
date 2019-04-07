import pandas
import geopy

geocoder = geopy.geocoders.ArcGIS()

inputdata = pandas.read_csv("supermarkets.csv")

listOfLats=[]
listOfLongs=[]

for i in inputdata.index.tolist():
    address = ",".join(inputdata.loc[i:i, ["Address", "City", "State", "Country"]].values.tolist()[0])
    gloc = geocoder.geocode(query=address)
    listOfLats.append(gloc.latitude)
    listOfLongs.append(gloc.longitude)

inputdata["lat"] = listOfLats
inputdata["long"] = listOfLongs

inputdata