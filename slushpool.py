#!/usr/bin/env python
"""An interface for the slushpool mining program."""

import os
import sys
#import time
#import datetime
# import yaml
import urllib.request
# import urllib.parse
import json
# import hmac
# import hashlib

# from config.__options__ import Options

__author__ = "Eric Petersen @Ruckusist"
__copyright__ = "Copyright 2017, The Alpha Griffin Project"
__credits__ = ["Eric Petersen", "Shawn Wilson", "@alphagriffin"]
__license__ = "***"
__version__ = "0.0.1"
__maintainer__ = "Eric Petersen"
__email__ = "ruckusist@alphagriffin.com"
__status__ = "Alpha"


class Slushpool(object):
    """Should be entry level here. Make it easy."""

    def __init__(self, options=None):
        """Should be entry level here. Make it easy."""
        self.options = options
        self.api = '1658580-9e3b5c9f69f3d4be9343a0b6182e81fc'

    def main(self):
        """Should be entry level here. Make it easy."""
        return True

    ## Private Methods ##
    def my_balance(self):
        """Should be entry level here. Make it easy."""
        msg = "https://slushpool.com/stats/json/{}".format(self.api)
        print("Requesting this URL: {}".format(msg))
        with urllib.request.urlopen(msg) as url:
            data = json.loads(url.read().decode('UTF-8'))
        for results in data:
            try:
                for block in data[results]:
                    reward = float(data[results][block]['reward'])
                    hash_ = data[results][block]['hash']
                    nmc_reward = float(data[results][block]['nmc_reward'])
                    if reward > 0:
                        print("{}: {} | reward: {} | nmc_reward: {}".format(
                            results, block, reward, nmc_reward))
                    print(block)
                    for heading in data[results][block]:
                        print(heading, data[results][block][heading])
                        pass
            except Exception as e:
                pass

        print("Completed Api request")
        return data


    def my_account(self):
        """Should be entry level here. Make it easy."""
        msg = "https://slushpool.com/accounts/profile/json/{}".format(self.api)
        print("Requesting this URL: {}".format(msg))
        with urllib.request.urlopen(msg) as url:
            data = json.loads(url.read().decode('UTF-8'))
        print(data)
        for results in data:
            try:
                print(results, data[results])
                pass
            except Exception as e:
                pass
        print("Completed Api request")
        return data



def main():
    """Launcher for the app."""
    app = Slushpool()

    if app.main():

        x = app.my_balance()
        y = app.my_account()
        sys.exit('Alphagriffin.com | 2017')
    return True


if __name__ == '__main__':
    main()
