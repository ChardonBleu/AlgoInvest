from constant import MAX_CLIENT_WALLET
import market

from action import Action
from wallet import Wallet

import time
import timeit


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
        self.array = [[0 for column_invest in range(max_invest * 100 + 1)]
                      for i in range(2)]

    def build_dynamic_array(self, market, max_invest):
        """Fonction permettant d'obtenir le portefeuille d'actions le plus rentable
        en utilisant l'algorithme dynamique:
        On construit pas à pas un tableau des choix les plus rentables à partir de
        la solution la plus rentable déjà trouvée.
        Les valeurs du tableau doivent être des entiers.

        Arguments:

        """
        index_action = 0
        while index_action < len(market.actions):
            column_invest = 0
            if index_action % 2 == 0:
                while column_invest < max_invest * 100:
                    column_invest += 1
                    if market.actions[index_action].price <= column_invest:
                        self.array[1][column_invest] = max(
                            self.array[0][column_invest],
                            (
                                self.array[0][
                                    column_invest - market.actions[index_action].price]
                            )
                            + int(market.actions[index_action].income * 100),
                        )
                    else:
                        self.array[1][column_invest] = self.array[0][column_invest]
            else:
                while column_invest < max_invest * 100:
                    column_invest += 1
                    if market.actions[index_action].price <= column_invest:
                            self.array[0][column_invest] = max(
                            self.array[1][column_invest],
                            (
                                self.array[1][
                                    column_invest - market.actions[index_action].price]
                            )
                            + int(market.actions[index_action].income * 100),
                        )
                    else:
                        self.array[0][column_invest] = self.array[1][column_invest]
            index_action += 1
        if len(market.actions) % 2 == 0:
            return self.array[0][max_invest * 100]
        else:
            return self.array[1][max_invest * 100]


if __name__ == "__main__":

    TWENTY_ACTIONS = market.TWENTY_ACTIONS
    THOUSAND_ACTIONS_1 = market.convert_csv_in_dict("dataset1.csv")
    THOUSAND_ACTIONS_2 = market.convert_csv_in_dict("dataset2.csv")

    current_market = Wallet()
    for action in THOUSAND_ACTIONS_1:
        if float(action["price"]) > 0:
            current_market.actions.append(
                Action(
                    action["name"],
                    (int(float(action["price"]) * 100)),
                    float(action["profit"]),
                )
            )

        else:
            continue

    print()
    print("*****************Algorithme dynamique******************")
    print()

    dynamic_array = DynamicArray(MAX_CLIENT_WALLET)
    
    tps1 = time.time()
    
    best_income = dynamic_array.build_dynamic_array(current_market, MAX_CLIENT_WALLET)
    print("profit wallet: ", round(best_income/10000, 2), " €")
    
    tps2 = time.time()
    
    print()
    print("***************** ", round(tps2 - tps1, 2), " s ******************")
    print()
