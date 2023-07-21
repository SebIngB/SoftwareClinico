import gspread
from oauth2client.service_account import ServiceAccountCredentials

def sheet(filename):

    scope = ['https://www.googleapis.com/auth/spreadsheets','https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    credenciales = ServiceAccountCredentials.from_json_keyfile_name('Procesamiento/proyecto-imbanaco-39015942cbb0.json', scope) # type: ignore

    cliente = gspread.authorize(credenciales)

    archivo = cliente.open(filename)

    return archivo



