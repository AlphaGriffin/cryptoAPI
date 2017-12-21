"""
Processes for Properly gathering and displaying
Crypto assets.
"""

__author__ = "Eric Petersen @Ruckusist"
__copyright__ = "Copyright 2017, The Alpha Griffin Project"
__credits__ = ["Eric Petersen", "Shawn Wilson", "@alphagriffin"]
__license__ = "***"
__version__ = "0.0.2"
__maintainer__ = "Eric Petersen"
__email__ = "ruckusist@alphagriffin.com"
__status__ = "Beta"

import os, sys, datetime, time, collections

import src.options
import src.sheets
import src.manager
import src.printer


def program():
    # setup globals assets
    config = src.options.Options("../../access/access_codes.yaml")
    P = src.printer.Printer(config)  # .no_size_printer
    # start program
    P("| Cryptosheets | {}".format(datetime.datetime.now()))
    man = src.manager.AssetManager(config)
    P("Logging into google.")
    C = src.sheets.gHooks(config).spreadsheet

    # setup placeholders
    dataset         = collections.defaultdict(dict)


    exchanges = []
    P("Setting up exchanges.")
    for exchange in man.my_exchanges:
        x, bals = man.setup_exchange(exchange, dataset)
        exchanges.append(x)
        P("THIS EXCHANGE: {}".format(exchange))
        for coin in bals:
            bal = bals[coin]['bal']
            #last = bals[coin]['last']
            #high = bals[coin]['high']
            #low = bals[coin]['low']
            #pair = bals[coin]['pair']
            #change = bals[coin]['change']
            #P("{}: {}: {}: {}: {}".format(coin, bal, last, high, low))
            P("{}: {}".format(coin, bal))
        sys.exit()

    P("Got exchanges.")
    P("Getting balances")
    my_balances = man.get_balances(dataset)
    print(my_balances)
    print(dataset)

    #//////////////////////////////////////////////////////////////////////////
    """
    found_coins = []
    for exchange in reversed(exchanges):
        if exchange is not None:
            # P("Checking coins against exchange: {}".format(exchange.id))
            for coin in my_balances:
                if coin is not None:
                    if 'BTC' not in coin:
                        betterset[coin]['bal'] = my_balances[coin]
                        try:
                            # if we have good data on this coin... just move on for now...
                            if coin in found_coins:
                                # P("already have coin: {}".format(coin))
                                pass;
                        except:
                            if not 'BTC' in coin:
                                pair = '{}/BTC'.format(coin)
                            else:
                                pair = '{}/USDT'.format(coin)
                            # Search the Local Directory First then search invidually
                            try:
                                for pairs in _dataset[exchange]['ticker']:
                                    if pair in pairs:
                                        subset = _dataset[exchange]['ticker']

                            except:
                                # Not Found in Local Directory
                                P("Looking up coin: {}, for pair {} on exchange {}".format(coin, pair, exchange.id))
                                try:
                                    time.sleep(2)
                                    subset = exchange.fetchTicker(pair)
                                except:
                                    pass;
                            #//////////////////////////////////////////////////////
                            try:
                                if subset:
                                    betterset[coin]['pair'] = pair
                                    betterset[coin]['high'] = subset['high']
                                    betterset[coin]['low'] = subset['low']
                                    betterset[coin]['last'] = subset['last']
                                    betterset[coin]['change'] = subset['change']
                                    betterset[coin]['ex_id'] = exchange.id
                                    found_coins.append(coin)
                                    P("{} Found!".format(coin))
                                    subset = None
                            except Exception as e:
                                exc_type, exc_obj, exc_tb = sys.exc_info()
                                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                                print(exc_type, fname, exc_tb.tb_lineno)
                                pass;
    #//////////////////////////////////////////////////////////////////////////
    btc_price = betterset['BTC']['last']
    total_btc_val = 0
    total_usd_val = 0
    for i in sorted(betterset):
        if 'BTC' not in i:
            try:
                P(i)
                P('Balance: {:.8f}'.format(betterset[i]['bal']))
                P('Current BTC Price: {:.8f}'.format(betterset[i]['last']))
                cur_btc_val = float(betterset[i]['bal']) * float(betterset[i]['last'])
                total_btc_val += cur_btc_val
                P('Current {} Balance Value: {:.8f}'.format(betterset[i]['pair'][-3:], cur_btc_val))
            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                pass
    P()
    P('Total BTC Value: {:.8f}'.format(total_btc_val))
    total_usd_val = float(btc_price) * total_btc_val
    P('Total USD Value: {:.2f} $'.format(total_usd_val))
    """
    P()
    P("Finished Run.")
    return True

if __name__ == '__main__':
    # try:
    program()
    """
    except Exception as e:
        print("and thats okay too.")
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        sys.exit()
    """
