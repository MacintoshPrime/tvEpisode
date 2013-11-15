import urllib2
import json
import datetime
from dateutil import parser

def isepisode(show):
    show = show.replace(' ', '-')
    currentseason = getSeason(show)
    
    if currentseason:
    
        for episode in currentseason:
            if iscurrentweek(episode):
                return episode['overview']

    else:
        return "Show not found"
        
        
def getSeason(show):
    try:
        seasons = "http://api.trakt.tv/show/seasons.json/78b010f9a0d6e4aae891e8cebbc80fd9/%s" %(show)
        season = len(json.loads(urllib2.urlopen(seasons).read()))
        episodes = "http://api.trakt.tv/show/season.json/78b010f9a0d6e4aae891e8cebbc80fd9/%s/%s" %(show, season)
        x = urllib2.urlopen(episodes).read()
    
        pretty = json.loads(x)
    except:
        return False
    else:
        
        return pretty
	
def getairDate(iso):
    iso = iso['first_aired_iso']
    date = parser.parse(iso)
    
    return date.date()
    
def iscurrentweek(date):
    
    date = getairDate(date)
    currentweek = datetime.datetime.now().date().isocalendar()[1]
    currentyear = datetime.datetime.now().year
    
    if date.isocalendar()[1] ==  currentweek and currentyear == date.year:
        return True
    else:
        return False