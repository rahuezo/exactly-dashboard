from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import os


# Setup the Sheets API
DEVELOPER_KEY = "AIzaSyCRzYVdACevnFHUgHdA_acOGFY6kuMq9MM"

SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'

class SheetsConnector: 
    @staticmethod
    def fill_empty(row): 
        return [element if len(element) > 0 else 0 for element in row[:]]

    def __init__(self): 
        self.service = self.connect()
    
    def connect(self): 
        return build('sheets', 'v4', http=Http(), developerKey=DEVELOPER_KEY)#http=self.credentials.authorize(Http()))

    def get_rows(self, sheet_id, range_name): 
        result = self.service.spreadsheets().values().get(spreadsheetId=sheet_id, range=range_name).execute()
        return result.get('values', [])