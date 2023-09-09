import gspread
from google.oauth2.service_account import Credentials

def Load_Credentials():
    # Load credentials from client_secret.json
    credentials = Credentials.from_service_account_file('backend/nectaria-webstore.json', scopes=['https://spreadsheets.google.com/feeds'])
    print('Credentials successfully loaded!')
    # Authenticate with Google Sheets
    gc = gspread.authorize(credentials)
    print('Successfully authenticated!')
    return gc

def Get_Worksheet_Data(sheet_number):
    gc = Load_Credentials()
    sheet_url = 'https://docs.google.com/spreadsheets/d/1f1u7phzgUbeMSBju6CasuxPhJ6DKZjnK6wTMxu2Ayzc'
    worksheet = gc.open_by_url(sheet_url).get_worksheet(sheet_number)
    return worksheet

def Add_Raw_Order_Data(data):
    worksheet = Get_Worksheet_Data(0)
    worksheet.append_row(data)
    print('Entry added to Google Sheet!')

def Read_Product_Data():
    worksheet = Get_Worksheet_Data(1)
    data = worksheet.get_all_values()
    print('Data successfully retrieved!\n')
    return data
    

if __name__ == '__main__': 
    # Data to add
    Read_Product_Data()
