from constant import MAX_CLIENT_WALLET
import market

from action import Action
from wallet import Wallet

import time


class DynamicArray:
    """Classe modélisant un tableau dynamique"""

    def __init__(self, max_invest):
        """Une branche de l'arbre binaire correspond à un portefeuille possible
        en terme d'investissement. L'arbre est une liste de portefeuilles.
        Le tableau contient autant de lignes que d'actions dans le marché.
        Le tableau contient autant de colonnes que d'entiers entre 0 et la
        somme maximale à investir. Les prix des actions du marché étant donnés
        au centième prés on multipliera par 100 ces prix pour les rendre
        entiers et on multiplie par 100 également la sommme disponible pour les
        achants.

        Arguments:
            max_invest{int} -- somme maximale à investir
        """
        self.array = [[0 for i in range(max_invest * 100 + 1)]]

    def build_dynamic_array(self, market, max_invest):
        """Fonction permettant d'obtenir le portefeuille d'actions le plus rentable
        en utilisant l'algorithme dynamique:
        On construit pas à pas un tableau des choix les plus rentables à partir de
        la solution la plus rentable déjà trouvée.

        Arguments:

        """
        for index_action in range(1, len(market.actions) + 1):
            self.array.append([0])
            for invest in range(1, max_invest * 100 + 1):
                if invest < market.actions[index_action - 1].price:
                    self.array[index_action].append(
                        self.array[index_action - 1][invest]
                    )
                else:
                    self.array[index_action].append(
                        max(
                            self.array[index_action - 1][invest],
                            (
                                self.array[index_action - 1][
                                    invest - market.actions[index_action - 1].price
                                ]
                            )
                            + market.actions[index_action - 1].income
                        )
                    )
        print(self.array[len(market.actions)][max_invest * 100])
        return self.array

    def search_dynamic_wallet(self, array, market, max_invest):
        """Fonction permettant d'obtenir le portefeuille d'actions le plus rentable
        en utilisant l'algorithme dynamique:
        On construit pas à pas un tableau des choix les plus rentables à partir de
        la solution la plus rentable déjà trouvée.

        Arguments:

        """
        client_wallet = Wallet()
        n = len(market.actions)
        v = array[len(market.actions)][max_invest]
        w = max_invest

        for j in range(len(market.actions) - 1, -1, -1):
            print("v: ", v)
            print("w: ", w)
            wj = market.actions[j].price
            vj = market.actions[j].income
            print("wj: ", wj)
            print("vj: ", vj)
            if (wj <= w) and (v - vj == array[j][w - wj]):
                client_wallet.actions.append(market.actions[j])
                v -= vj
                w -= wj
            client_wallet.view_wallet()            
            input("...")
        client_wallet.update_income_wallet()
        client_wallet.update_value_wallet()
        client_wallet.view_wallet()            
        input("...")
        return client_wallet


            


if __name__ == "__main__":

    TWENTY_ACTIONS = market.TWENTY_ACTIONS
    THOUSAND_ACTIONS_1 = market.convert_csv_in_dict("dataset1.csv")
    THOUSAND_ACTIONS_2 = market.convert_csv_in_dict("dataset2.csv")

    current_market = Wallet()
    for action in TWENTY_ACTIONS:
        if float(action["price"]) > 0.0:
            current_market.actions.append(
                Action(
                    action["name"],
                    (int(float(action["price"])) ),
                    float(action["profit"]),
                )
            )
        else:
            continue

    print()
    print("*****************Algorithme dynamique******************")
    print()
    tps1 = time.time()

    current_market.view_wallet()
    
    dynamic_array = DynamicArray(MAX_CLIENT_WALLET)
    dynamic_client_array = dynamic_array.build_dynamic_array(
        current_market, MAX_CLIENT_WALLET
    )
    
    
    dynamic_client_wallet = dynamic_array.search_dynamic_wallet(dynamic_client_array,
        current_market, MAX_CLIENT_WALLET
    )
    """dynamic_client_wallet.view_wallet()"""

    tps2 = time.time()
    print()
    print("***************** ", round(tps2 - tps1, 2), " s ******************")
    print()
