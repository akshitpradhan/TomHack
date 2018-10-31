import configparser
import requests
import json
import sys
import time
import datetime
import urllib.request


def CalculateRoute(sourceLat,sourceLon,destLat,destLon):
    # URL to the tomtom api
    apiCalculateRoute      = "https://api.tomtom.com/routing/1/calculateRoute/"
    # apiKey
    apiKey      = "XgTfO704XqyOtvnzS3jtT5YikyAIxcyM"

    #[coordinates]
    sourceLat   = 51.5560241
    sourceLon   = -0.2817075
    destLat     = 53.4630621
    destLon     = -2.2935288

    tomtomURL = "%s/%s,%s:%s,%s/json?key=%s" % (apiURL,sourceLat,sourceLon,destLat,destLon,apiKey)

    getData = urllib.request.urlopen(tomtomURL).read()
    jsonTomTomString = json.loads(getData)

    totalTime = jsonTomTomString['routes'][0]['summary']['travelTimeInSeconds']

    print ("time to destination is: ", totalTime)

def ReachableRange(fuel):
    # URL to the tomtom api
    apiURL      = "https://api.tomtom.com/routing/1/calculateReachableRange/"
    apiGeoCode = "https://api.tomtom.com/search/2/reverseGeocode/"
    # apiKey
    apiKey      = "XgTfO704XqyOtvnzS3jtT5YikyAIxcyM"

    fuel = 43
    tomtomURL = "%s/%s/json?energyBudgetInkWh=%s&avoid=unpavedRoads&vehicleEngineType=electric&constantSpeedConsumptionInkWhPerHundredkm=50%%2C8.2%%3A130%%2C21.3&key=%s" % (apiURL,data['loc'],fuel,apiKey)
    getData = urllib.request.urlopen(tomtomURL).read()
    jsonTomTomString = json.loads(getData)

    longitude = jsonTomTomString['reachableRange']['boundary'][0]['longitude']
    latitude = jsonTomTomString['reachableRange']['boundary'][0]['latitude']

    tomtomURL2 = "%s%s,%s.json?key=%s" % (apiGeoCode,latitude,longitude,apiKey)
    getData = urllib.request.urlopen(tomtomURL2).read()
    jsonTomTomString = json.loads(getData)
    subd = jsonTomTomString['addresses'][0]["address"]['countrySubdivision']
    secsubd = jsonTomTomString['addresses'][0]["address"]["countrySecondarySubdivision"]
    print("With ",fuel,"L you can reach upto ",secsubd,subd)

def Nearby(sourceLat,sourceLon):
    # URL to the tomtom api
    apiURL      = "https://api.tomtom.com/search/2/nearbySearch/"
    # apiKey
    apiKey      = "XgTfO704XqyOtvnzS3jtT5YikyAIxcyM"

    long = 28.5494
    lat = 77.2001

    tomtomURL = "%s.json?lat=%s&lon=%s&countrySet=IN&key=%s" % (apiURL,long,lat,apiKey)
    #print(tomtomURL)

    getData = urllib.request.urlopen(tomtomURL).read()
    jsonTomTomString = json.loads(getData)
    return(testing1['results'][6]['address'])

def reverseGeocode(sourceLat,sourceLong):
    apiGeoCode = "https://api.tomtom.com/search/2/reverseGeocode/"
    apiKey      = "XgTfO704XqyOtvnzS3jtT5YikyAIxcyM"
    tomtomURL2 = "%s%s,%s.json?key=%s" % (apiGeoCode,sourceLat,sourceLong,apiKey)
    getData = urllib.request.urlopen(tomtomURL2).read()
    jsonTomTomString = json.loads(getData)
    subd = jsonTomTomString['addresses'][0]["address"]['countrySubdivision']
    secsubd = jsonTomTomString['addresses'][0]["address"]["countrySecondarySubdivision"]
    print("With ",fuel,"L you can reach upto ",secsubd,subd)