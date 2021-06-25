from constant import MAX_CLIENT_WALLET
import market

from action import Action
from wallet import Wallet

import time


def search_glouton_wallet(market):
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
        if client_wallet.value + action.price <= MAX_CLIENT_WALLET:
            client_wallet.value += action.price
            client_wallet.actions.append(action)
    client_wallet.update_income_wallet()
    return client_wallet


if __name__ == "__main__":

    current_market = Wallet()    
    CHOICE, title_market = current_market.choice_market()
    
    for action in CHOICE:
            if float(action["price"]) != 0.00:
                current_market.actions.append(
                    Action(
                        action["name"], abs(float(action["price"])), float(action["profit"])
                    )
                )
            else:
                continue

    print()
    print("*****************Algorithme glouton******************")
    print(title_market, ":")
    print()
    tps1 = time.time()

    glouton_client_wallet = search_glouton_wallet(current_market)
    glouton_client_wallet.view_wallet()

    tps2 = time.time()
    print()
    print("***************** ", round(tps2 - tps1, 2), " s ******************")
    print()
