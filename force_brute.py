from constant import MAX_CLIENT_WALLET
from market import TWENTY_ACTIONS

from action import Action
from wallet import Wallet

import time
from copy import deepcopy, copy


class BinaryTree:
    
    def __init__(self, branch):
        self.tree = [branch]
        

    def wallet_force_brute(self, market):
        """Méthode construisant un arbre binaire avec toutes les combinaisons
        possibles pour des portefeuilles ayant une valeur inférieure à la valeur*
        d'investissement MAX_CLIENT_WALLET

        Arguments:
            actions {objet Wallet} -- contient la liste des objets Actions du 
                                    marché financier
            
        Return:
            objet wallet -- Objet contenant la liste des actions donnant le
                            meilleur profit 
        """
    
        best_income = 0
        best_wallet = Wallet()
        for action in market.actions:
            for index in range(len(self.tree)):
                new_branch = Wallet()                
                new_branch.wallet_actions = self.tree[index].wallet_actions.copy()
                new_branch.wallet_actions.append(action)            
                new_branch.update_value_wallet()
                new_branch.update_income_wallet()
                if new_branch.value <= MAX_CLIENT_WALLET:
                    self.tree.append(new_branch)
                    if new_branch.income > best_income:
                        best_income = new_branch.income
                        del best_wallet
                        best_wallet = new_branch
                del new_branch           
        return best_wallet


if __name__ == '__main__':
    
    current_market = Wallet()
    for action in TWENTY_ACTIONS:
        current_market.actions.append(Action(action['name'], action['cost'], action['income']))
    # current_market.update_income_wallet()
    # current_market.update_value_wallet()
    # current_market.view_wallet()
    
    
    print()
    print("*****************Algorithme force brute******************")
    print()
    tps1 = time.time()
    
    binary_tree = BinaryTree(Wallet())
    force_brute_client_wallet = binary_tree.wallet_force_brute(current_market)
    force_brute_client_wallet.view_wallet()
    
    tps2 = time.time()
    print()
    print("***************** ", round(tps2 - tps1, 2), " s ******************")
    print()
