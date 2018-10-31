from utils.gsheets_connector import SheetsConnector
from datetime import datetime 


OPERATIONS_FIELDS = ['date', 'db_size_profiles_archive', 'db_size_profiles_frontend', 'db_size_individual',
    'db_size_location_raw', 'db_size_location_parsed', 'db_size_emails', 'db_size_search_engine', 'db_size_corporations',
    'db_size_technology', 'db_size_websites_processed', 'db_size_appended', 'db_size_email_campaign', 'db_size_email_campaign_marketing',
    'db_size_email_campaign_csuite'
]


def clean_number(n): 
    return int(n.replace(',', ''))


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
                for i, field in enumerate(OPERATIONS_FIELDS): 
                    record.__dict__[field] = columns[i]

                print record
                record.save()

            # If record exists, update it if needed
            else:                 
                record = model.objects.get(date=date_object)
                for i, field in enumerate(OPERATIONS_FIELDS[1:]): 
                    old_field_value = record.__dict__[field]
                    new_field_value = columns[1:][i]

                    if old_field_value != new_field_value: 
                        setattr(record, field, new_field_value)
                record.save()
