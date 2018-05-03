from utils.gsheets_connector import SheetsConnector, creds
from datetime import datetime 


def clean_number(n): 
    return int(n.replace(',', ''))


def operations_sheets_to_model(model, sheets_id, range_name, columns=None): 
    sheets = SheetsConnector(creds)
    rows = sheets.get_rows(sheets_id, range_name)

    for row in rows[1:]: 
        date_object = datetime.strptime(row[0], '%m/%d/%Y')

        if not model.objects.filter(date=date_object).exists(): 
            record = model(
                date=date_object,
                db_size_profiles_archive=clean_number(row[1]),
                db_size_profiles_frontend=clean_number(row[2]),
                db_size_individual=clean_number(row[3]),
                db_size_location_raw=clean_number(row[4]),
                db_size_location_parsed=clean_number(row[5]),
                db_size_emails=clean_number(row[6]),
                db_size_search_engine=clean_number(row[7]),
                db_size_corporations=clean_number(row[8]),
                db_size_technology=clean_number(row[9]),
                db_size_websites_processed=clean_number(row[10]),
                db_size_appended=clean_number(row[11]),
                db_size_email_campaign=clean_number(row[12]),
                db_size_email_campaign_marketing=clean_number(row[13]),
                db_size_email_campaign_csuite=clean_number(row[14]),
            )
            record.save()

