import src.sheets
import src.printer
import src.options

import ccxt

config = src.options.Options("../../access/access_codes.yaml")
P = src.printer.Printer(config)
C = src.sheets.gHooks(config).spreadsheet

print(ccxt.binance().fetch_ticker(str('ZEC/BTC')))

print("workings")
