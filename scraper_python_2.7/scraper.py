
""" PYTHON 2.7 """


from datetime import datetime
import re
import math
from time import sleep
import os

import requests

import psycopg2


import lxml.html
from lxml.cssselect import CSSSelector
from lxml import etree

bartStations = {
    "12th St. Oakland City Center" : (37.803768, -122.271450),
    "16th St. Mission" : (37.765062, -122.419694),
    "19th St. Oakland" : (37.808350, -122.268602),
    "24th St. Mission" : (37.752470, -122.418143),
    "Fruitvale" : (37.774836, -122.224175),
    "Lake Merritt" : (37.797027, -122.265180),
    #"MacArthur" : (37.829065, -122.267040),
    "West Oakland" : (37.804872, -122.295140)
}

sfBox = [
    (37.797605, -122.457160),
    (37.797605, -122.389955),
    (37.747739, -122.389955),
    (37.747739, -122.451753)
]





dtPat = re.compile("(?P<yr>\d\d\d\d)-(?P<mth>\d\d)-(?P<day>\d\d) (?P<hour>\d+):(?P<min>\d+)")

def getProjectRootDir():
    fileName = os.path.realpath(__file__)
    return fileName[0: fileName.rfind(os.sep) + 1]


def setupDb(db):

    cur = db.cursor()
    print cur

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Listing(
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            href TEXT NOT NULL,
            price INTEGER NOT NULL,
            latitude REAL,
            longitude REAL,
            br INTEGER,
            ts TIMESTAMP WITHOUT TIME ZONE NOT NULL,
            neighborhood TEXT NOT NULL
        );
      """)

    db.commit()
    return db


def parseDt(craigDt):
    dtMatch = dtPat.match(craigDt)

    if (dtMatch is None):
        return None
    return {
        "yr" : int(dtMatch.group("yr")),
        "mth" : int(dtMatch.group("mth")),
        "day" : int(dtMatch.group("day")),
        "hour" : int(dtMatch.group("hour")),
        "min" : int(dtMatch.group("min"))
    }

# use distance formula to calculate miles between 2 latitude/longitude coordinates
def simpleDist(lat1, lon1, lat2, lon2):
    if (lat1 is None or lon1 is None or lat2 is None or lon2 is None):
        print "(" + str(lat1) + "," + str(lon1) + "," + str(lat2) + "," + str(lon2) + ")"

    earthRad = 3958.8 # miles
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    return math.sqrt(math.pow(earthRad * math.cos(math.radians(lat1)) * dLon, 2) + math.pow(earthRad * dLat, 2))

# Filter for listings retrieved by Craigslist: modify with your own metrics to return True for favorable listings.
def highPriority(info):
    if (info["hood"] is not "tenderloin" and isInSfBox(info) and info["br"] >= 3):
        print info["hood"] + "  --  " + info["br"]
        return True
    else:
        return False

def isInSfBox(info):
    ret = info["lat"] > sfBox[2][0] and \
            info["lat"] < sfBox[1][0] and \
            info["lon"] < sfBox[1][1] and \
            info["lon"] > sfBox[0][1]
    if (ret):
        print "\t\t\t\tin Sf (" + info["hood"] + ")"
    return ret

def isCloseToBart(info):
    for coords in bartStations.values():
        if (simpleDist(coords[0], coords[1], info["lat"], info["lon"]) < 1):
            print "\t\t\t\tnear Bart (" + info["hood"] + ")"
            return True

# compare 2 different datetime objects/dictionaries
# if first is later than the second, return 1
# if first is earlier than the second, return -1
# if the two datetimes are equal (to the minute), return 0
def compDt(first, second):
    if (first["yr"] > second["yr"]):
        return 1
    elif (first["yr"] < second["yr"]):
        return -1

    if (first["mth"] > second["mth"]):
        return 1
    elif (first["mth"] < second["mth"]):
        return -1

    if (first["day"] > second["day"]):
        return 1
    elif (first["day"] < second["day"]):
        return -1

    if (first["hour"] > second["hour"]):
        return 1
    elif (first["hour"] < second["hour"]):
        return -1

    if (first["min"] > second["min"]):
        return 1
    elif (first["min"] < second["min"]):
        return -1

    return 0

def getLastSeenDb(db):

    cur = db.cursor()
    res = cur.execute("""
        SELECT
          LastSeen.yr,
          LastSeen.mth,
          LastSeen.day,
          LastSeen.hour,
          LastSeen.min
        FROM LastSeen
    """)

    if (res is None):
        return None
    else:
        return {
            "yr" : res[0],
            "mth" : res[1],
            "day" : res[2],
            "hour" : res[3],
            "min" : res[4],
        }

def newestOnPage(parsedPage, db):
    rawDt = parsedPage.find(".//time").attrib["datetime"]
    return parseDt(rawDt)

def makeReq(url, qParams):
    if (len(qParams) > 0):
        res = requests.get(url, params=qParams)
    else:
        res = requests.get(url)

    if (res.status_code is 403):
        print("Ip is banned; response status code is 403.")
        return None
    elif (res.status_code is not 200):
        print("Status code is " + str(res.status_code) + ".")
        return None
    else:
        return lxml.html.fromstring(res.text)

def extractHeaderInfo(listing):

    ret = {}

    selTitle = CSSSelector(".result-title")
    selPrice = CSSSelector(".result-price")
    selHood = CSSSelector(".result-hood")
    selMaptag = CSSSelector('.maptag')
    selHousing = CSSSelector('.housing')

    try:
        ret["id"] = int(listing.attrib["data-pid"])
    except ValueError as e:
        print "Invalid id for posting"
        return

    ret["title"] = selTitle(listing)[0].text
    ret["href"] = selTitle(listing)[0].attrib["href"]
    if (len(selHousing(listing)) > 0):
        try:
            ret["br"] = int(selHousing(listing)[0].text.strip()[0])
        except ValueError as e:
            print "Could not parse bedroom # for https://sfbay.craigslist.org" + ret["href"]
            return None
    else:
        print "No bedroom # for https://sfbay.craigslist.org" + ret["href"]
        return None

    postDt = parseDt(listing.find(".//time").attrib["datetime"])
    if (postDt is None):
        return None
    else:
        ret["dt"] = postDt

    try:
        ret["price"] = int(selPrice(listing)[0].text[1:])
    except ValueError as e:
        print "Could not parse price for https://sfbay.craigslist.org" + ret["href"]
        return None

    hoodList = selHood(listing)
    if (len(hoodList) > 0):
        ret["hood"] = hoodList[0].text.strip(" ()")
    else:
        print "https://sfbay.craigslist.org" + ret["href"] + " does not have a neighborhood: skipping"
        return None

    if(len(selMaptag(listing)) > 0):
        i = 1
        latLon = getLatLon(ret["href"])
        if (len(latLon) > 0):
            ret["lat"] = latLon[0]
            ret["lon"] = latLon[1]
        else:
            print "https://sfbay.craigslist.org" + ret["href"] + " does not have location: skipping"
            return None
    else:
        print "https://sfbay.craigslist.org" + ret["href"] + " does not have location: skipping"
        return None

    return ret

def getLatLon(href):
    page = makeReq("https://sfbay.craigslist.org" + href, {})
    sleep(.4)

    selMap = CSSSelector("#map")

    mapItems = selMap(page)

    if (len(mapItems) > 0):
        map = mapItems[0]
        return [float(map.attrib["data-latitude"]), float(map.attrib["data-longitude"])]
    return []


"""
def hasSeen(db, info):
    dbCursor = db.cursor()
    dbCursor.execute("SELECT Listing.id from Listing WHERE Listing.id=?", (info["id"],))
    if (dbCursor.fetchone()):
        return True
    else:
        return False
"""

def updateLastSeenDb(newDt, db):
    db.execute("""
                INSERT OR REPLACE INTO LastSeen(id, yr, mth, day, hour, min)
                    VALUES(1, ?, ?, ?, ?, ?);
            """, (
        newDt["yr"],
        newDt["mth"],
        newDt["day"],
        newDt["hour"],
        newDt["min"]
    ))
    db.commit()
    return

def computePrefs(input):

    # get desired locations from database
    # put each location into prefs


    res = {

        "dbParams": {
            "dbname" : "craig_app",
            "user" : "craig_user",
            "password" : "asdf",
            "host" : "localhost"
        },
        "qParams": {
            "max_price" : 5450,
            "min_price" : 3000,
            "sort" : "date"
        }
    }

    # for key in input, replace key in res if it is an official key

    return res

def start(inputPrefs):
    print "Running scraper."

    scraperPrefs = computePrefs(inputPrefs)
    db = psycopg2.connect(dbname=scraperPrefs["dbParams"]["dbname"], user=scraperPrefs["dbParams"]["user"],
                          password=scraperPrefs["dbParams"]["password"], host=scraperPrefs["dbParams"]["host"])
    setupDb(db)
    maxToSee = total = 1080


    lastSeenDb = getLastSeenDb(db)

    try:
        s = 0
        parseErrors = 0
        seenDuplicate = False
        updateSeenDt = None
        saved = []
        while (s < maxToSee and s < total and not seenDuplicate):

            qParams = scraperPrefs["qParams"]
            qParams["s"] = s
            parsed = makeReq("https://sfbay.craigslist.org/search/apa", qParams)

            selRows = CSSSelector('.result-row')
            selTotal = CSSSelector('.totalcount')
            selStart = CSSSelector('.rangeFrom')
            selEnd = CSSSelector('.rangeTo')

            empty = CSSSelector('#moon')

            if (len(empty(parsed)) > 0):
                print "No listings for query with parameters: " + str(qParams)
                break
            else:
                total = int(selTotal(parsed)[0].text)
                start = selStart(parsed)[0].text
                end = selEnd(parsed)[0].text
                print "Retrieved " + str(start) + " to " + str(end) + " of " + str(total) + " listings."
                listings = selRows(parsed)

                if (len(listings) > 0 and len(listings) == int(end) - int(start) + 1):
                    if (s is 0):
                        updateSeenDt = newestOnPage(parsed, db)
                        if (updateSeenDt is None):
                            raise Exception("Could not retrieve most recent post.")
                        print "newest listing is " + str(updateSeenDt) + "\n\n"

                    numLeft = maxToSee - s
                    for i in range(min(numLeft, len(listings))):
                        s += 1
                        info = extractHeaderInfo(listings[i])
                        if (info is not None):
                            if (lastSeenDb is not None and compDt(lastSeenDb, info["dt"]) > -1):
                                print "post dt is " + str(info["dt"])
                                print "last seen dt is " + str(lastSeenDb)
                                seenDuplicate = True
                                break
                            elif (highPriority(info)):
                                print str(s) + ": https://sfbay.craigslist.org" + str(info["href"])
                                saved.append(info)
                        else:
                            parseErrors += 1
                else:
                    "Error: mentioned number of listings doesn't equal actual number of listings."
            sleep(2)
        if (updateSeenDt is not None):
            updateLastSeenDb(updateSeenDt, db)
        for entry in saved:
            db.execute("""INSERT OR REPLACE INTO Listing(
                                id,
                                title,
                                href,
                                price,
                                yr,
                                mth,
                                day,
                                hour,
                                min,
                                latitude,
                                longitude,
                                neighborhood)
                            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""", (
                        entry["id"], entry["title"], "https://sfbay.craigslist.org" + entry["href"],
                        entry["price"], entry["dt"]["yr"], entry["dt"]["mth"],
                        entry["dt"]["day"], entry["dt"]["hour"], entry["dt"]["min"],
                        entry["lat"], entry["lon"], entry["hood"]
            ))
            db.commit()
        print str(s) + " listings retrieved."
        print str(len(saved)) + " listings saved."
        print str(parseErrors) + " listings could not be parsed."
    except Exception as e:
        print("Exception parsing listing statistics")
        print e
    db.close()


start({})