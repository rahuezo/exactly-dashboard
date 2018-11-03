from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from modulars import Module

import os


# Setup the Sheets API
# DEVELOPER_KEY = "AIzaSyCRzYVdACevnFHUgHdA_acOGFY6kuMq9MM"


DEVELOPER_KEY = "AIzaSyCtqTmhTQ--_-9YxgDz4QVf7zSahg6JeKQ"

SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'

class SheetsConnector: 
    @staticmethod
    def fill_empty(row): 
        return [element if len(element) > 0 else 0 for element in row[:]]

    def __init__(self): 
        self.service = self.connect()
    
    def connect(self): 
        return build('sheets', 'v4', http=Http(), developerKey=DEVELOPER_KEY) 

    def get_rows(self, sheet_id, range_name): 
        result = self.service.spreadsheets().values().get(spreadsheetId=sheet_id, range=range_name).execute()
        self.rows = result.get('values', [])
        # return self.rows

    def rows_to_modules(self): 
        modules = []
        
        for row_index, row in enumerate(self.rows): 
            if len(row[0]) == 0:
                continue

            if row_index == 0:
                for i in xrange(1, len(row)): 
                    modules.insert(i - 1, Module( {'name': row[i] }))
            else: 
                for i in xrange(1, len(row)): 
                    if len(row[i]) == 0:
                        continue
                    modules[i - 1].fields[row[0].lower()] = row[i]
        return modules