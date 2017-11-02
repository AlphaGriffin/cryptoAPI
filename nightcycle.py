import os, sys, subprocess
from decimal import Decimal
import datetime, time
import printer, options
import poloniex, nicehash

import urllib.request
import urllib.parse
import json

config = options.Options()
NH = nicehash.Nicehash(config)
P = printer.Printer(config)
POLO = poloniex.Trader(config)

class XMRAPI(object):
    def __init__(self, options):
        self.options = options
        self.API_CALL = 'https://api.nanopool.org/v1/xmr/'

    def user(self):
        api_local = 'user/'
        api_url_ = self.API_CALL + api_local + self.options.xmr_nanopool_address
        """
        with urllib.request.urlopen(
            # 'https://api.nanopool.org/v1/xmr/balance/41dLNKQ4LnZgjVm1NLMhooNffeWRJ7RXyTFMnzhdpBL55Yq7eDceJ5HgViRRERHUsKHNNT5PVaFAmYRXJdZEAyHoS2X8gpz'
                        ) as url:
            print("test1")
            data = json.loads(url.read().decode('UTF-8'))
            print("test2")
        """
        data = subprocess.check_output(['curl', api_url_])
        return json.loads(data.decode('UTF-8'))
XMR = XMRAPI(config)

# Startup Operations
os.system('clear')
P()
P("Start Time: {}".format(datetime.datetime.now()))
P("AlphaGriffin | Nightcycle 2017")
P()
# Starting Balances All around:
# starting polo balances
polo_start_balances = POLO.balances()
P("Starting Poloniex XMR Balance: " + str(polo_start_balances['XMR']))
P("Starting Poloniex BTC Balance: " + str(polo_start_balances['BTC']))
P()
# starting nicehash balances
nicehash_start_balance = NH.my_balance()
NH_curr_pending_balance_btc = Decimal(nicehash_start_balance['result']['balance_pending'])
NH_curr_confirmed_balance_btc = Decimal(nicehash_start_balance['result']['balance_confirmed'])
P("Nicehash Starting Balance BTC: " + str(NH_curr_confirmed_balance_btc))
P()
# Starting nanopool xmr balance
xmr_user_data = XMR.user()
P()
XMR_current_hashrate = xmr_user_data['data']['hashrate']
XMR_current_balance = xmr_user_data['data']['balance']
# print(xmr_user_data)
P("XMR Nanopool Starting Balance: " + str(xmr_user_data['data']['balance']))
P("XMR Nanopool Current Hashrate: " + str(xmr_user_data['data']['hashrate']))
P()
current_xmr_orders_nicehash = NH.my_orders(22)
IS_ORDER_RUNNING = current_xmr_orders_nicehash['result']['orders']
if len(IS_ORDER_RUNNING) > 0:
    while len(IS_ORDER_RUNNING) > 0:
        current_xmr_orders_nicehash = NH.my_orders(22)
        IS_ORDER_RUNNING = current_xmr_orders_nicehash['result']['orders']
        P("CURRENT {} ORDERS RUNNING ON NICEHASH".format(len(IS_ORDER_RUNNING)))
        for index, order in enumerate(IS_ORDER_RUNNING):
            # print(order, end='\r')
            P("|{}| Checking Nicehash XMR order: {}".format(datetime.datetime.now(), index + 1))
            btc_left_in_order = IS_ORDER_RUNNING[index]['btc_avail']
            btc_spent_on_order = IS_ORDER_RUNNING[index]['btc_paid']
            NH_current_hashrate = IS_ORDER_RUNNING[index]['accepted_speed']
            NH_current_price = IS_ORDER_RUNNING[index]['price']
            NH_order_end_time = IS_ORDER_RUNNING[index]['end']
            P("BTC Left in order: {}".format(btc_left_in_order))
            P("BTC Spent on order: {}".format(btc_spent_on_order))
            P("Current Hashrate: {}".format(NH_current_hashrate))
            P("Current Pay rate: {}".format(NH_current_price))
            P("Current End Time: {}".format(datetime.datetime.fromtimestamp(NH_order_end_time + time.time())))
        P()
        # end of run countdown timer...
        mins_left = 2
        for mins in range(mins_left):
            print("", end='\r')
            P("STILL RUNNING NICEHASH ORDER. CHECKING AGAIN IN {}mins.".format(mins_left))
            mins_left -= 1
            time.sleep(60)
        P()

print(   "test" )
