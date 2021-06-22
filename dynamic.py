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
        Les valeurs du tableau doivent être des entiers.

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
                            + int(market.actions[index_action - 1].income * 100),
                        )
                    )

    def search_dynamic_wallet(self, market, max_invest):
        """Fonction permettant d'obtenir le portefeuille d'actions le plus rentable
        en utilisant l'algorithme dynamique:
        On construit pas à pas un tableau des choix les plus rentables à partir de
        la solution la plus rentable déjà trouvée.

        Arguments:

        """
        client_wallet = Wallet()
        income = self.array[len(market.actions)][max_invest * 100]
        value = max_invest * 100

        for j in range(len(market.actions) - 1, -1, -1):
            if (market.actions[j].price <= value) and (
                income - int(market.actions[j].income * 100)
                == self.array[j][value - market.actions[j].price]
            ):
                client_wallet.actions.append(market.actions[j])
                income -= int(market.actions[j].income * 100)
                value -= market.actions[j].price

        for action in client_wallet.actions:
            action.price /= 100
            action.income = round(action.income / 100, 2)
        client_wallet.update_income_wallet()
        client_wallet.update_value_wallet()
        return client_wallet


if __name__ == "__main__":

    TWENTY_ACTIONS = market.TWENTY_ACTIONS
    THOUSAND_ACTIONS_1 = market.convert_csv_in_dict("dataset1.csv")
    THOUSAND_ACTIONS_2 = market.convert_csv_in_dict("dataset2.csv")

    print("choisir le panel d'actions à tester:")
    print("1: TWENTY_ACTIONS, 2: dataset1, 3: dataset2")
    bool = True
    while bool:
        choice = input(">> ")
        if choice == '1':
            CHOICE = TWENTY_ACTIONS
            title = "panel de 20 actions"
            bool = False
        elif choice == '2':
            CHOICE = THOUSAND_ACTIONS_1
            title = "dataset1"
            bool = False
        elif choice == '3':
            CHOICE = THOUSAND_ACTIONS_2
            title = "dataset2"
            bool = False
        else:
            continue

    current_market = Wallet()
    for action in CHOICE:
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
    print(title, ":")
    print()

    dynamic_array = DynamicArray(MAX_CLIENT_WALLET)

    tps1 = time.time()

    dynamic_array.build_dynamic_array(current_market, MAX_CLIENT_WALLET)

    tps2 = time.time()

    dynamic_client_wallet = dynamic_array.search_dynamic_wallet(
        current_market, MAX_CLIENT_WALLET
    )

    dynamic_client_wallet.view_wallet()

    print()
    print("***************** ", round(tps2 - tps1, 2), " s ******************")
    print()
