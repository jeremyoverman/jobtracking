from flask import Flask
from flask import request
import gdata.gauth

import atom.data
import gdata.data
import gdata.contacts.client
import gdata.contacts.data
import webbrowser

from apiclient.discovery import build

from httplib2 import Http
import oauth2client
from oauth2client.client import OAuth2WebServerFlow

import os

import datetime, calendar

from bs4 import BeautifulSoup as soup

CALENDAR_ID = "us7s95mde08sqbnmt0i7jgdd74@group.calendar.google.com"

#===============================================================================
# Google Calendar
#===============================================================================

class Calendar():
    def __init__(self, api):
        self.api = api
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
        
        eventsResult = self.api.calendar.events().list(
            calendarId=CALENDAR_ID,
            timeMin=start.isoformat() + "Z",
            timeMax=end.isoformat() + "Z",
            singleEvents=True,
            orderBy='startTime').execute()
        events = eventsResult.get('items', [])
        
        if month:
            self.cache[month] = events
            
        return events
    
    def addJob(self, date, contactatomid, frequency, count):
        if frequency.lower() == "weekly":
            frequency = "WEEKLY"
        else:
            frequency = "MONTHLY"
        
        rrule = "RRULE:FREQ=%s;INTERVAL=%d" % (frequency, count)
        contact_name = contacts.getFullName(contactatomid)
        summary = "%s (%s)" % contacts.getCompany(contactatomid), contact_name
        location = contacts.getAddress(contactatomid)
        
        event = {
                 'summary': contact_name,
                 'start': {'date': date.isoformat()},
                 'end': {'date': date.isoformat()},
                 'recurrence': [rrule],
                 'extendedProperties': {'contact': contactatomid},
                 'location': location
                 }
        
        result = self.api.calendar.events().insert(calendarId=CALENDAR_ID, body=event).execute()
        self.cache[date.month] = result
        print result
        return result

#===============================================================================
# Google Contacts
#===============================================================================

class Contacts():
    def __init__(self, api):
        self.api = api
        self.cache = {}
    
    def getFullName(self, atomid):
        return self.cache[atomid].name.full_name.text
    
    def getPhoneNumber(self, atomid):
        for i, entry in enumerate(self.cache[atomid].phone_number):
            return entry.uri[7:]
    
    def getAddress(self, atomid):
        for i, entry in enumerate(self.cache[atomid].structured_postal_address):
            xml = soup(entry.ToString())
            formatted_address = xml.find("ns0:formattedaddress")
            if not formatted_address:
                return None
            else:
                address = formatted_address.text.replace("\n", " ")
                return address
    
    def getCompany(self, atomid):
        organization = self.cache[atomid].organization
        if organization:
            xml = soup(organization.ToString())
            return xml.find("ns0:orgname").text
        else:
            return None
    
    def getGroupsAtomId(self, name):
        self.groups = {}
        feed = self.api.contacts.GetGroups()
        for i, entry in enumerate(feed.entry):
            self.groups[entry.GetId()] = entry
        
        for group in self.groups:
            atomid = self.groups[group].id.text
            title = self.groups[group].title.text
            if title == name:
                return atomid
    
    def getAllContactsInGroup(self, title):
        if len(self.cache.keys()) == 0:
            groupid = self.getGroupsAtomId("Clients")
            query = gdata.contacts.client.ContactsQuery()
            query.max_results = 1000
            query.group = groupid
            feed = self.api.contacts.GetContacts(q=query)
            for i, entry in enumerate(feed.entry):
                contactid = entry.GetId()
                self.cache[contactid] = entry
        return self.cache

#===============================================================================
# Google API and Authentication scheme
#===============================================================================

app = Flask(__name__)

@app.route('/callback')
def callback():
    #Handle the redirect URI request
    error = request.args.get('error', '')
    if error:
        return "Error: " + error
    
    #Get the code
    code = request.args.get('code')
    
    #Pass it along to the api call to be used later
    api.code = code
    
    #Kill the HTTP server
    request.environ.get('werkzeug.server.shutdown')()
    return "You may close this window."
    
class API():
    def __init__(self):
        self.client_id = '392272749394-i7e8cju0f6a607miqgmlubhfv9cgje4j.apps.googleusercontent.com'
        self.client_secret = 'b5ZFW_pL3tK3bs-pHsZu0SIh'
        self.scopes = ['https://www.google.com/m8/feeds', 'https://www.googleapis.com/auth/calendar']
        self.user_agent = 'Job Tracking'
        self.redirect_uri = 'http://localhost:8000/callback'
        self.code = None
        
#         import logging
#         ch = logging.StreamHandler()
#         ch.setLevel(logging.DEBUG)
#         oauth2client.client.logger.setLevel(logging.DEBUG)
#         oauth2client.client.logger.setLevel(logging.DEBUG)
#         oauth2client.client.logger.addHandler(ch)
#     
    def getOAuthStoragePath(self):
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir, 'jobtracking.json')
        
        return credential_path
    
    def getAuthenticationFromStore(self, store):
        credentials = store.get()
        if not credentials or credentials.invalid:
            return None
        else:
            return credentials
    
    def runFlow(self, store):
        flow = OAuth2WebServerFlow(client_id=self.client_id,
                           client_secret=self.client_secret,
                           scope=' '.join(self.scopes),
                           redirect_uri=self.redirect_uri)
        
        url = flow.step1_get_authorize_url(self.redirect_uri)
        
        webbrowser.open_new(url)
        app.run(port=8000)
        
        credentials = flow.step2_exchange(self.code)
        store.put(credentials)
        
        return credentials
                
    def authenticate(self):
        #Try to get stored credentials
        store = oauth2client.file.Storage(self.getOAuthStoragePath())
        credentials = self.getAuthenticationFromStore(store)

        if not credentials:
            credentials = self.runFlow(store)
        
        #Authorize the HTTP object for v3 API's
        httpobj = Http()
        credentials.authorize(httpobj)
        
        #Get an OAuth2Token object for older API's
        token = gdata.gauth.OAuth2TokenFromCredentials(credentials)
        
        #Create the contacts client and authorize it
        self.contacts = gdata.contacts.client.ContactsClient(source=self.user_agent, auth_token=token)
        self.contacts = token.authorize(self.contacts)
        
        #Create the calendar client and authorize it
        self.calendar = build('calendar', 'v3', http=httpobj)

if __name__ == "__main__":
    api = API()
    api.authenticate()
    contacts = Contacts(api)
    gcal = Calendar(api)
    #gcal.addJob(datetime.date.today(), "TEST:)", "monthly", 2)
    