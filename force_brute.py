from constant import MAX_CLIENT_WALLET
import market

import wallet


def tree(actions):
    """Méthode construisant un arbre binaire avec toutes les combinaisons
    possibles pour des portefeuilles ayant une valeur inférieure à la valeur*
    d'investissement MAX_CLIENT_WALLET

    Arguments:
        actions {dict} -- dictionnaire des actions du marché financier
        
    Return:
        list -- liste contenant des sets 
    """
    branch = []
    tree = [branch]  # contient liste de wallets possibles
    best_income = 0
    best_wallet = []
    for action in actions:
        for index in range(len(tree)):
            new_branch = tree[index].copy()
            new_branch.append(action)
            if wallet.value_wallet(new_branch) <= MAX_CLIENT_WALLET:
                tree.append(new_branch)
                if wallet.income_wallet(new_branch) > best_income:
                    best_income = wallet.income_wallet(new_branch)
                    best_wallet.clear()
                    best_wallet = new_branch
        
    return best_wallet


if __name__ == '__main__':
    
    actions = market.TWENTY_ACTIONS

    print()
    print("*****************Force brute******************")
    print()
    brute_client_wallet = tree(actions)
    value_brute_client_wallet = wallet.value_wallet(brute_client_wallet)
    income_brute_client_wallet = wallet.income_wallet(brute_client_wallet)
    wallet.view_wallet(brute_client_wallet)
    print("Valeur du portefeuille du client: ",
          str(value_brute_client_wallet), " euros")    
    print("bénéfices du client à 2 ans: ", 
          str(income_brute_client_wallet), " euros")
    print()
    print("******************************************************")
    print()

    

