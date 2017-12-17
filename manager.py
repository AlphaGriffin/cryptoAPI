"""
Processes for Properly gathering and displaying
Crypto assets.
"""

__author__ = "Eric Petersen @Ruckusist"
__copyright__ = "Copyright 2017, The Alpha Griffin Project"
__credits__ = ["Eric Petersen", "Shawn Wilson", "@alphagriffin"]
__license__ = "***"
__version__ = "0.0.1"
__maintainer__ = "Eric Petersen"
__email__ = "ruckusist@alphagriffin.com"
__status__ = "Beta"

import os, sys, datetime, time, collections
import ccxt
import options


class AssetManager(object):
    """Functions for getting at crypto Assets"""

    def __init__(self, options=None):
        self.options = options
        self.my_exchanges = [
                 'binance',
                 'poloniex',
                 'cryptopia',
                 'hitbtc',
                 'bitmex',
                 'ccex',
                 'bittrex']

    def __call__(self):
        return True

    def __str__(self):
        return str("CryptoManager V: {}".format(__version__))

    def main(self):
        """Sanity Checker."""
        return True

    def setup_exchange(self, this_exchange="binance", dataset=None):
        """
        This should go through each exchange available all at once and
        assign the everything to the data structure properly.
        """
        config = self.options
        dataset[this_exchange]['ex_id'] = this_exchange
        exchange_connect = eval("ccxt.{}()".format(this_exchange))
        dataset[this_exchange]['app'] = exchange_connect
        exchange_connect.apiKey = eval("config.{}_api".format(this_exchange))
        exchange_connect.secret = eval("config.{}_secret".format(this_exchange))
        balances = {}
        try:
            balance = exchange_connect.fetch_balance()
        except:
            # print("{} is Offline".format(this_exchange))
            return
        for x in balance['total']:
            if float(balance['total'][x]) > 0:
                balances[x] = balance['total'][x]
                try:
                    dataset['coins'][x] += '{}, '.format(this_exchange)
                except:
                    dataset['coins'][x] = '{}, '.format(this_exchange)
        dataset[this_exchange]['balances'] = balances
        # get the ticker
        try:
            ticker = exchange_connect.fetch_tickers()
            dataset[this_exchange]['ticker'] = ticker
        except Exception as e:
            dataset[this_exchange]['ticker'] = None
        return exchange_connect

    def get_balances(self, dataset):
        """Create Subset of Master Balance."""
        balances = {}
        for x in dataset:
            if 'coins' not in x:
                # print("Checking Balance on {}".format(str(x).upper()))
                try:
                    for i in dataset[x]['balances']:
                        try:
                            balances[i] += float(dataset[x]['balances'][i])
                        except:
                            balances[i] = float(dataset[x]['balances'][i])
                except:
                    # print("Exchange: {} shows no balance!".format(x))
                    pass
        return balances

def main():
    """Launcher for the app."""
    config = options.Options()
    app = AssetManager(config)

    if app.main():
        sys.exit('Alphagriffin.com | 2017')
    return True

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("and thats okay too.")
        sys.exit(e)
