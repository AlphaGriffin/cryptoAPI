#!/usr/bin/env python
"""An interface for the nicehash buying program."""

import sys
import urllib.request
import json

__author__ = "Eric Petersen @Ruckusist"
__copyright__ = "Copyright 2017, The Alpha Griffin Project"
__credits__ = ["Eric Petersen", "Shawn Wilson", "@alphagriffin"]
__license__ = "***"
__version__ = "0.0.2"
__maintainer__ = "Eric Petersen"
__email__ = "ruckusist@alphagriffin.com"
__status__ = "Beta"


class Nicehash(object):
    """A Wrapper for nicehash Api functionality."""
    Scrypt = 0
    SHA256 = 1
    ScryptNf = 2
    X11 = 3
    X13 = 4
    Keccak = 5
    X15 = 6
    Nist5 = 7
    NeoScrypt = 8
    Lyra2RE = 9
    WhirlpoolX = 10
    Qubit = 11
    Quark = 12
    Axiom = 13
    Lyra2REv2 = 14
    ScryptJaneNf16 = 15
    Blake256r8 = 16
    Blake256r14 = 17
    Blake256r8vnl = 18
    Hodl = 19
    DaggerHashimoto = 20
    Decred = 21
    CryptoNight = 22
    Lbry = 23
    Equihash = 24
    Pascal = 25
    X11Gost = 26
    Sia = 27
    Blake2s = 28
    Skunk = 29

    def __init__(self, options=None):
        """Make sure the options are properly set."""
        self.options = options
        self.api_id = self.options.nicehash_api_id
        self.api_key = self.options.nicehash_api
        self.my_btc = self.options.nicehash_btc_addr

    def __call__(self, options=None):
        """Calling the nicehash api will return the current api version."""
        data = None
        with urllib.request.urlopen('https://api.nicehash.com/api') as url:
            data = json.loads(url.read().decode('UTF-8'))
        print(data)


    def main(self):
        """Sanity check with your api keys and info."""
        print(self.options)
        return True

    # Sellers Info
    def stats_provider(self, btcaddr=None):
        """If you are a seller on nicehash this will tell you about your workers."""
        if btcaddr is None:
            btcaddr = self.my_btc
        data = None
        with urllib.request.urlopen('https://api.nicehash.com/api?method=stats.provider&addr={}'.format(btcaddr)) as url:
            data = json.loads(url.read().decode('UTF-8'))
        # print("Completed Api request")
        return data

    # Buyers INfo
    def get_orders(self, algo=1):
        """This is used to see current orders in place by the community."""
        data = None
        with urllib.request.urlopen('https://api.nicehash.com/api?method=orders.get&location=0&algo={}'.format(algo)) as url:
            data = json.loads(url.read().decode('UTF-8'))
        # print(data)
        # print("Completed Api request")
        return data

    def buy_info(self):
        """This is provided from them to help their autobot buy."""
        with urllib.request.urlopen('https://api.nicehash.com/api?method=buy.info'.format(' ')) as url:
            data = json.loads(url.read().decode('UTF-8'))
        # print(data)
        # print("Completed Api request")
        return data

    ## Private Methods ##
    def my_balance(self):
        """Returns nicehash balance."""
        msg = "https://api.nicehash.com/api?method=balance&id={}&key={}".format(self.api_id, self.api_key)
        # print("Requesting this URL: {}".format(msg))
        with urllib.request.urlopen(msg) as url:
            data = json.loads(url.read().decode('UTF-8'))
        # print(data)
        # print("Completed Api request")
        return data

    def my_orders(self, algo = 1):
        """Use Api to gather SHA-256 orders and info."""
        msg = "https://api.nicehash.com/api?method=orders.get&my&id={}&key={}&location=1&algo={}".format(self.api_id, self.api_key, algo)
        # print("Requesting this URL: {}".format(msg))
        with urllib.request.urlopen(msg) as url:
            data = json.loads(url.read().decode('UTF-8'))
        # print(data)
        return data

    # https://api.nicehash.com/api?method=orders.create&id=8&key=3583b1df-5e93-4ba0-96d7-7d621fe15a17&location=0&algo=0&amount=0.01&price=2.9&limit=0&pool_host=testpool.com&pool_port=3333&pool_user=worker&pool_pass=x
    def place_order(self, amount, price, limit, pool, port, user, passwd):
        """Use Api to place a SHA-256 order."""
        msg = "https://api.nicehash.com/api?method=orders.create&id={}&key={}&location=1&algo=1&amount={}&price={}&limit={}&pool_host={}&pool_port={}&pool_user={}&pool_pass={}".format(
            self.api_id, self.api_key, algo, amount, price, limit, pool, port, user, passwd)
        # print("Requesting this URL: {}".format(msg))
        with urllib.request.urlopen(msg) as url:
            data = json.loads(url.read().decode('UTF-8'))
        # print(data)
        return data




def main():
    """Launcher for the app."""
    app = Nicehash()

    if app.main():
        # app.my_balance()
        # app.my_orders()
        app.stats_provider()
        sys.exit('Alphagriffin.com | 2017')
    return True


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("and thats okay too.")
        sys.exit(e)
