from datetime import datetime
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

    def getMonthEventsList(self, year, month):
        last_day = calendar.monthrange(year, month)[1]
        start = datetime(year, month, 1, 0, 0, 0).isoformat() + "Z"
        end = datetime(year, month, last_day, 11, 59, 59).isoformat() + "Z"
        
        eventsResult = self.service.events().list(
            calendarId=CALENDAR_ID,
            timeMin=start,
            timeMax=end,
            singleEvents=True,
            orderBy='startTime').execute()
        events = eventsResult.get('items', [])
    
        #if events:
        #    for event in events:
        #        #print json.dumps(event)
        #        start = event['start'].get('dateTime')
        #        print start, event['summary']
        
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