from constant import MAX_CLIENT_WALLET
from market import TWENTY_ACTIONS

from action import Action
from wallet import Wallet

import time


def glouton_wallet(market):
    """Fonction permettant d'obtenir le portefeuille d'actions le plus rentable
    en utilisant l'algorithme glouton:
    On trie les actions par rentabilité décroissante. On choisi succesivement
    chaque action dans l'ordre jusqu'à ne
    plus pouvoir investir.

    Arguments:
        market {objet Wallet} -- portefeuille correspondant à toutes les
                                 actions du marché

    Returns:
        [objet Wallet] -- portefeuille "glouton" le plus rentable
    """
    client_wallet = Wallet()
    market.sort_actions_by_rentability(True)
    for action in market.actions:
        if client_wallet.value + action.cost <= MAX_CLIENT_WALLET:
            client_wallet.value += action.cost
            client_wallet.actions.append(action)
    client_wallet.update_income_wallet()
    return client_wallet


if __name__ == '__main__':

    current_market = Wallet()
    for action in TWENTY_ACTIONS:
        current_market.actions.append(Action(action['name'],
                                             action['cost'],
                                             action['income']))

    print()
    print("*****************Algorithme glouton******************")
    print()
    tps1 = time.time()

    glouton_client_wallet = glouton_wallet(current_market)
    glouton_client_wallet.view_wallet()

    tps2 = time.time()
    print()
    print("***************** ", round(tps2 - tps1, 2), " s ******************")
    print()
