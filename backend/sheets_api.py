import gspread
from google.oauth2.service_account import Credentials


def Add_Data(data):
    # Load credentials from client_secret.json
    credentials = Credentials.from_service_account_file('backend/nectaria-webstore.json', scopes=['https://spreadsheets.google.com/feeds'])
    print('Credentials successfully loaded!')
    # Authenticate with Google Sheets
    gc = gspread.authorize(credentials)
    print('Successfully authenticated!')
    # Open the Google Sheet by its URL
    sheet_url = 'https://docs.google.com/spreadsheets/d/1f1u7phzgUbeMSBju6CasuxPhJ6DKZjnK6wTMxu2Ayzc'
    worksheet = gc.open_by_url(sheet_url).get_worksheet(0)
    worksheet.append_row(data)
    print('Entry added to Google Sheet!')


if __name__ == '__main__': 
    # Data to add
    data = ['Marcaj de timp', 'E-mail', 'Metoda de livrare', 'Metoda plata']
    # Append a new row with the data
    Add_Data(data)
