from constant import MAX_CLIENT_WALLET
import market

from action import Action
from wallet import Wallet

import time


class DynamicArray:
    """Classe modélisant un tableau dynamique 
    """

    def __init__(self, max_invest):
        """Une branche de l'arbre binaire correspond à un portefeuille possible
        en terme d'investissement. L'arbre est une liste de portefeuilles.

        Arguments:
            branch {objet Wallet} -- portefeuille possible
        """
        self.array = [[0 for i in range(max_invest + 1)]]     

    def search_dynamic_wallet(self,market):
        """Fonction permettant d'obtenir le portefeuille d'actions le plus rentable
        en utilisant l'algorithme dynamique:
        On construit pas à pas un tableau des choix les plus rentables à partir de
        la solution la plus rentable déjà trouvée.     
        """
        client_wallet = Wallet()
        
        # Penser à rediviser par 100 les prix et gain avant de donner les résultats
        


if __name__ == '__main__':

    # market.FOOR_ACTIONS
    # market.TWENTY_ACTIONS
    THOUSAND_ACTIONS_1 = market.convert_csv_in_dict('dataset1.csv')   
    THOUSAND_ACTIONS_2 = market.convert_csv_in_dict('dataset2.csv')    

    current_market = Wallet()
    for action in market.TWENTY_ACTIONS:
        if float(action['price']) != 0.00:
            current_market.actions.append(Action(action['name'],
                                             abs(float(action['price'])) * 100,
                                             float(action['profit']) * 100))
        else:
            continue

    print()
    print("*****************Algorithme dynamique******************")
    print()
    tps1 = time.time()

    dynamic_array = DynamicArray(MAX_CLIENT_WALLET)
    # dynamic_client_wallet = dynamic_array.search_dynamic_wallet(current_market)
    # dynamic_client_wallet.view_wallet()
    
    print(dynamic_array.array)

    tps2 = time.time()
    print()
    print("***************** ", round(tps2 - tps1, 2), " s ******************")
    print()
