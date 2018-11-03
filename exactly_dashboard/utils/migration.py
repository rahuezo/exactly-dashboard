from utils.gsheets_connector import SheetsConnector
from django.conf import settings
from modulars import Module

from datetime import datetime 

import json, pandas






def clean_number(n): 
    return int(n.replace(',', ''))


# def sheet_to_json(sheet_rows, model=0, sheet_id=0, sheet_range=0, row_wise=True): 
#     # sheet = SheetsConnector()
#     # sheet_rows = sheet.get_rows(sheet_id, sheet_range)

#     rtn_json = []

#     if row_wise:
#         header = sheet_rows.pop(0) # get the first row from sheet_rows

#         df = pandas.DataFrame(sheet_rows, columns=header) # create DataFrame with header




#         # column_names = sheet_rows[0]

#         # for row in sheet_rows[1:]:
#         #     row_json = {}
#         #     for column_index, column_value in enumerate(row): 
#         #         row_json[column_names[column_index]] = column_value
#         #     rtn_json.append(row_json)

#     else: 
#         header = [row.pop(0) for row in sheet_rows] # get the first column from sheet_rows
#         df = pandas.DataFrame(data=sheet_rows).transpose() # create DataFrame and transpose it

#         int len = 0
#         items = []

#         foreach (string[] row in rows){
#             if (len == 0) {
#                 len = # determine number of items
#                 for(int i = 1; i < len; i++)
#                     items[i] = new LeadProjectCard()
#             }
#             for(int i = 1; i < len; i++)
#                 items[i].add(row[0], row[i])
#         }


#         transposed_sheet_rows = pandas.DataFrame(data=sheet_rows).transpose()



        
        




    return json.dumps(rtn_json)

# data = [["one", "two", "three", "four"], [0, 1, 0, 1], [1, 0, 1, 1], [0, 1, 1, 1]]

# data = [["one", 0, 1, 0], ["two", 1, 0, 1], ["three", 1, 1, 1]]

# sheet_to_json(data)















def operations_sheets_to_model(model, sheets_id, range_name, columns=None): 
    sheets = SheetsConnector()
    rows = sheets.get_rows(sheets_id, range_name)

    for row in rows[1:]: 
        if len(row) > 1: 
            date_object = datetime.strptime(row[0], '%m/%d/%Y')
            columns = [date_object] + [clean_number(i) for i in row[1:]]

            # If record doesn't exist, create it
            if not model.objects.filter(date=date_object).exists(): 
                print "Record doesn't exist"

                record = model()
                for i, field in enumerate(settings.DB_STATS_FIELDS): 
                    record.__dict__[field] = columns[i]

                print record
                record.save()

            # If record exists, update it if needed
            else:                 
                record = model.objects.get(date=date_object)
                for i, field in enumerate(settings.DB_STATS_FIELDS[1:]): 
                    old_field_value = record.__dict__[field]
                    new_field_value = columns[1:][i]

                    if old_field_value != new_field_value: 
                        setattr(record, field, new_field_value)
                record.save()
