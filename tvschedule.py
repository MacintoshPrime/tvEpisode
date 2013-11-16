import urllib2
import json
import datetime
from dateutil import parser

def check(show):
    seasons = "http://api.trakt.tv/show/seasons.json/78b010f9a0d6e4aae891e8cebbc80fd9/%s" %(show)
    season = urllib2.urlopen(seasons).read()
    y = json.loads(season)
    count = len(y)
    if count == y[0]['season']:
        episodes = "http://api.trakt.tv/show/season.json/78b010f9a0d6e4aae891e8cebbc80fd9/%s/%s" %(show, count)
    else:
        episodes = "http://api.trakt.tv/show/season.json/78b010f9a0d6e4aae891e8cebbc80fd9/%s/%s" %(show, count-1)
    x = urllib2.urlopen(episodes).read()
    pretty = json.loads(x)

    return y[0]['season'], len(y)
    
def isepisode(show):
    show = show.replace(' ', '-')
    currentseason = getSeason(show)
    
    if currentseason:
    
        for episode in currentseason:
            if iscurrentweek(episode):
                return str(episode['first_aired_iso']) + '<br />' + episode['title'] + '<br />' + episode['overview']

    else:
        return "Show not found"
        
        
def getSeason(show):
    try:
        seasons = "http://api.trakt.tv/show/seasons.json/78b010f9a0d6e4aae891e8cebbc80fd9/%s" %(show)
        season = urllib2.urlopen(seasons).read()
        y = json.loads(season)
        count = len(y)
        
        if count == y[0]['season']:
            episodes = "http://api.trakt.tv/show/season.json/78b010f9a0d6e4aae891e8cebbc80fd9/%s/%s" %(show, count)
        else:
            episodes = "http://api.trakt.tv/show/season.json/78b010f9a0d6e4aae891e8cebbc80fd9/%s/%s" %(show, count-1)
        
        x = urllib2.urlopen(episodes).read()
    
        pretty = json.loads(x)
    except:
        return False
    else:
        
        return pretty
	
def getairDate(iso):
    iso = iso['first_aired_iso']
    if iso:
        date = parser.parse(iso)
        return date.date()
    else:
        return None
    
def iscurrentweek(date):
    
    date = getairDate(date)
    if not date:
        return False
    currentweek = datetime.datetime.now().date().isocalendar()[1]
    currentyear = datetime.datetime.now().year
    
    if date.isocalendar()[1] == currentweek and currentyear == date.year:
        return True
    else:
        return False