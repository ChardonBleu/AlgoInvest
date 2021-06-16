from constant import MAX_CLIENT_WALLET
from market import TWENTY_ACTIONS

from action import Action
from wallet import Wallet

import time


if __name__ == '__main__':

    current_market = Wallet()

    for action in TWENTY_ACTIONS:
        current_market.actions.append(Action(action['name'], action['cost'], action['income']))

    client_wallet = Wallet()

    print()
    print("*****************Algorithme glouton******************")
    print()
    tps1 = time.time()
    
    current_market.sort_actions_by_rentability(True)
    for action in current_market.actions:
        if client_wallet.value + action.cost <= MAX_CLIENT_WALLET:
            client_wallet.value += action.cost
            client_wallet.actions.append(action)    

    client_wallet.update_income_wallet()

    client_wallet.view_wallet()
    print(client_wallet)

    tps2 = time.time()
    print()
    print("***************** ", round(tps2 - tps1, 2), " s ******************")
    print()
