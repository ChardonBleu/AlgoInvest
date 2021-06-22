from constant import MAX_CLIENT_WALLET
from market import TWENTY_ACTIONS


from action import Action
from wallet import Wallet

import time


class BinaryTree:
    """Classe modélisant l'arbre binaire de toutes les combinaisons possibles
    avec les N actions du marché financier étudié
    On explore toutes les combinaisons. On mémorise dans l'arbre seulement les
    combinaisons ayant une valeur infèrieure ou égale à la valeur maximale à
    investir.
    """

    def __init__(self, branch):
        """Une branche de l'arbre binaire correspond à un portefeuille possible
        en terme d'investissement. L'arbre est une liste de portefeuilles.

        Arguments:
            branch {objet Wallet} -- portefeuille possible
        """
        self.tree = [branch]

    def search_wallet_force_brute(self, market):
        """Méthode construisant un arbre binaire avec toutes les combinaisons
        possibles pour des portefeuilles ayant une valeur inférieure à la
        valeur d'investissement MAX_CLIENT_WALLET

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
                new_branch.actions = self.tree[index].actions.copy()
                new_branch.actions.append(action)
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


if __name__ == "__main__":

    current_market = Wallet()
    for action in TWENTY_ACTIONS:
        current_market.actions.append(
            Action(action["name"], action["price"], action["profit"])
        )

    print()
    print("*****************Algorithme force brute******************")
    print("panel de 20 actions:")
    print()
    tps1 = time.time()

    binary_tree = BinaryTree(Wallet())
    force_brute_client_wallet = binary_tree.search_wallet_force_brute(current_market)
    force_brute_client_wallet.view_wallet()

    tps2 = time.time()
    print()
    print("***************** ", round(tps2 - tps1, 2), " s ******************")
    print()
