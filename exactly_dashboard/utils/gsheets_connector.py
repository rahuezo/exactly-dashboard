from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import os


try: 
    CLIENT_SECRET_PATH = os.environ['SHEETS_CLIENT_SECRET_PATH'] 
except: 
    print "You must first set the SHEETS_CLIENT_SECRET_PATH environment variable"
    CLIENT_SECRET_PATH = r'C:\Users\Mark\programming_projects\web_dev\exactly-dashboard\exactly_dashboard\resources'

# Setup the Sheets API

SCOPES = 'https://www.googleapis.com/auth/spreadsheets'

store = file.Storage('credentials.json')
creds = store.get()

if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets(os.path.join(CLIENT_SECRET_PATH, 'client_secret.json'), SCOPES)
    creds = tools.run_flow(flow, store)


class SheetsConnector: 
    @staticmethod
    def fill_empty(row): 
        return [element if len(element) > 0 else 0 for element in row[:]]

    def __init__(self, credentials): 
        self.credentials = credentials
        self.service = self.connect()
    
    def connect(self): 
        return build('sheets', 'v4', http=self.credentials.authorize(Http()))

    def get_rows(self, sheet_id, range_name): 
        result = self.service.spreadsheets().values().get(spreadsheetId=sheet_id, range=range_name).execute()
        return result.get('values', [])

# SPREADSHEET_ID = '1zY9rsgQxIwEw0vluZ1kx0V5QnH3Nc5Cw631uVJhRJjQ'
# RANGE_NAME = 'operations!A:H'

# sheets = SheetsConnector(creds)

# rows = sheets.get_rows(SPREADSHEET_ID, RANGE_NAME)

# for row in rows: 
#     print row