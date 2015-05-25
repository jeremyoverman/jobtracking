import datetime
import os, json, calendar

from apiclient.discovery import build
from httplib2 import Http
import oauth2client
from oauth2client import client
from oauth2client import tools

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Calendar API Quickstart'
CALENDAR_ID = "us7s95mde08sqbnmt0i7jgdd74@group.calendar.google.com"
        
class GoogleCalendar():
    def __init__(self):
        credentials = self.get_credentials()
        self.service = build('calendar', 'v3', http=credentials.authorize(Http()))
        self.cache = {}
    
    def gDatetimeToDatetime(self, gdate):
        date_tuple = gdate.split("T")[0].split("-")
        date = datetime.date(int(date_tuple[0]),
                             int(date_tuple[1]),
                             int(date_tuple[2]))
        
        if len(gdate.split("T")) == 2:
            time_tuple = gdate.split("T")[1].split(":")
            time = datetime.time(int(time_tuple[0]),
                                 int(time_tuple[1]),
                                 int(time_tuple[2].split("-")[0]))
            return datetime.datetime.combine(date, time)
        else:
            return date
    
    def getDayList(self, date):
        days_events = []
        for event in self.getEventsList(date):
            if event["start"].has_key("date"):
                gdate = event["start"].get("date")
                start = self.gDatetimeToDatetime(gdate)
            else:
                gdate = event["start"].get("dateTime")[:10]
                start = self.gDatetimeToDatetime(gdate)
            if start == date:
                days_events.append(event)
                
        return days_events
    
    def getEventsList(self, date, update=False):
        year = date.year
        month = date.month
        
        if self.cache.has_key(date.month):
            return self.cache[date.month]
        else:
            if not update: return None
        
        last_day = calendar.monthrange(year, month)[1]
        start = datetime.datetime(year, month, 1, 0, 0, 0) - datetime.timedelta(days=31)
        end = datetime.datetime(year, month, last_day, 11, 59, 59) + datetime.timedelta(days=31)
        #else:
        #    day_start = datetime.time(0,0,0)
        #    day_end = datetime.time(23,59,59)
        #    
        #    start = datetime.datetime.combine(dt, day_start).isoformat() + "Z"
        #    end = datetime.datetime.combine(dt, day_end).isoformat() + "Z"
        
        eventsResult = self.service.events().list(
            calendarId=CALENDAR_ID,
            timeMin=start.isoformat() + "Z",
            timeMax=end.isoformat() + "Z",
            singleEvents=True,
            orderBy='startTime').execute()
        events = eventsResult.get('items', [])
        
        if month:
            self.cache[month] = events
            
        return events
    
    def get_credentials(self):
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir,
                                       'calendar-api-quickstart.json')
    
        store = oauth2client.file.Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
            flow.user_agent = APPLICATION_NAME
            if flags:
                credentials = tools.run_flow(flow, store, flags)
            else: # Needed only for compatability with Python 2.6
                credentials = tools.run(flow, store)
            print 'Storing credentials to ' + credential_path
        return credentials
    
if __name__ == '__main__':
    google_calendar = GoogleCalendar()
    events = google_calendar.getMonthEventsList(2015, 5)
    for event in events:
        print event["start"].get("date"), event["summary"]