#Gdata imports
import atom.data
import gdata.data
import gdata.contacts.client
import gdata.contacts.data

#Authentication imports
from httplib2 import Http
import oauth2client
from oauth2client import client
from oauth2client import tools

#various imports
import os

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/calendar.readonly https://www.google.com/m8/feeds'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Calendar API Quickstart'
CALENDAR_ID = "us7s95mde08sqbnmt0i7jgdd74@group.calendar.google.com"

class Contacts():
    def __init__(self):
        pass
    
    def getAllContacts(self):
        feed = api.contacts.GetContacts()
        for i, entry in enumerate(feed.entry):
            print type(entry) 

class API():
    def __init__(self, email, password):
        self.contacts = gdata.contacts.client.ContactsClient(source='<var>Job Tracking</var>')
        self.contacts.ClientLogin(email, password, self.contacts)
    
    def get_credentials(self):
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir, 'calendar-api-quickstart.json')
    
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

if __name__ == "__main__":
    api = API("jeremyoverman@gmail.com", "1067815194")
    contacts = Contacts()
    contacts.getAllContacts()