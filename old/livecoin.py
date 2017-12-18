#!/usr/bin/env python

"""
A Test poloniex trader.
@Ruckusist<ruckusist@alphagriffin.com>
"""

import os, sys          # system
import time, datetime   # time
import yaml, json       # cross format parser
import urllib.request, urllib.parse  # web functions
import hmac, hashlib    # crypto functions
import options, printer # AG libraries

__author__ = "Eric Petersen @Ruckusist"
__copyright__ = "Copyright 2017, The Alpha Griffin Project"
__credits__ = ["Eric Petersen", "Shawn Wilson", "@alphagriffin"]
__license__ = "***"
__version__ = "0.0.2"
__maintainer__ = "Eric Petersen"
__email__ = "ruckusist@alphagriffin.com"
__status__ = "Beta"


class Livecoin(object):
    """A controller for Livecoin."""

    def __init__(self, options=None, database=None):
        """Setup the instrument."""
        self.options = options

    def __call__(self):
        """Should be entry level here. Make it easy."""
        with urllib.request.urlopen('https://poloniex.com/public?command=returnTicker') as url:
            data = json.loads(url.read().decode('UTF-8'))
            for coin in sorted(data):
                print("{}".format(coin))
                for i in data[coin]:
                    x = data[coin][i]
                    print("\t{}: {}".format(i, x))
        return data

    def balances(self):
        """Print Personal Balances."""
        api_url = self.options.livecoin_api_url
        method = '/payment/balances'
        req = {}
        balances = dict()
        # req['command'] = '/payment/balances'
        post_data = urllib.parse.urlencode(req).encode('ASCII')

        sign = hmac.new(self.options.livecoin_secret.encode('ASCII'),
                        post_data,
                        hashlib.sha256).hexdigest()
        headers = {
            'Key': self.options.livecoin_api_key,
            'Sign': sign,
            'Content-type': "application/x-www-form-urlencoded"
        }
        with urllib.request.urlopen(urllib.request.Request(
                api_url + method,
                post_data,
                headers)
                ) as url:
            data = json.loads(url.read().decode('UTF-8'))
            for i in data:
                j = data[i]
                balances[i] = j
        return balances


    def main(self):
        """Sanity Check."""
        return True


def main():
    """Launcher for the app."""
    config = options.Options()
    app = Livecoin(config)

    if app.main():
        # app.my_balance()
        # app.my_orders()
        print(app.balances())
        sys.exit('Alphagriffin.com | 2017')
    return True

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("and thats okay too.")
        sys.exit(e)
