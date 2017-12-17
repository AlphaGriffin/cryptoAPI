#!/usr/bin/python3
"""
CryptoSheets.
"""
import os, sys, time, datetime, collections

import httplib2
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import gspread
import ccxt

import options
import printer

#Globals - outside class
SCOPES = ['https://spreadsheets.google.com/feeds',
          'https://www.googleapis.com/auth/drive']
          #'https://www.googleapis.com/auth/spreadsheets'] # 'https://www.googleapis.com/spreadsheets' # change to .edit? #FIXME
CLIENT_SECRET_FILE = 'client_secret_new.json' # this should not be default should it?
APPLICATION_NAME = 'reporter'


class gHooks(object):
    """My interface to google."""

    #Globals - inside class
    #SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
    #CLIENT_SECRET_FILE = 'client_secret.json'
    #APPLICATION_NAME = 'Google Sheets API Python Quickstart'

    def __init__(self, options):
        self.options = options

    def get_credentials(self):
        """Gets valid user credentials from storage.

        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.
        source: https://developers.google.com/sheets/api/quickstart/python
        Returns:
            Credentials, the obtained credential.
        """
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir,
                                       'reporter_creds.json')

        store = Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
            flow.user_agent = APPLICATION_NAME
            credentials = tools.run_flow(flow, store)
        return credentials

def main():
    """Sheets updater Program."""
    start_time = datetime.datetime.now().strftime("%m-%d %H:%M:%S")
    #//////| Build Objects
    config = options.Options()
    P = printer.Printer(config)
    G = gHooks(config)
    P("AlphaGriffin.com | {}".format(start_time))

    #//////| Start Sequence
    P("Getting Google Creds.")
    creds = G.get_credentials()
    P("Authorizing Google Creds.")
    gc = gspread.authorize(creds)
    #//////| Get Spreadsheet
    try:
        P("Starting A new Spreadsheet.")
        sheet = gc.create('SUPERTEST')
        P("passed")
    except Exception as e:
        print(e)
        P("Opening Spreadsheet.")
        sheet = gc.open('test4')
        P("test4 worked")
    #//////| Notify on Changes
    """
    try:
        necessary_paries = ['eric.alphagriffin@gmail.com',
                            'magilla422@gmail.com']
        for user in necessary_paries:
            P("Sharing Sheet to Necessary Parties: {}".format(user))
            sheet.share(user, perm_type='user', role='writer')
    except:
        P("Insufficient Permission to share Spreadsheet. Fix this.")
    #//////| Open Worksheets
    P("Adding Worksheet Info to the Spreadsheet.")
    try:
        worksheet = sheet.add_worksheet(title="Info", rows="15", cols="10")
    except:
        worksheet = sheet.worksheet('Info')
    #//////| Start writing data to this worksheet.
    P("Populating this worksheet.")
    test1 = 'KinetechConcepts Info'
    worksheet.update_acell('A1', test1)
    worksheet.update_acell('B1', 'Last Updated: {}'.format(start_time))

    # DO MORE STUFF HERE.
    """
    #//////| Finished |\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
    P("Finished Tests.")


if __name__ == '__main__':
    #try:
    main()
    """
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("File: {1}\nError: {0}\nLine: {2}".format(
            exc_type, fname, exc_tb.tb_lineno
            ))
    """
