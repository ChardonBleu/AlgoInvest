from constant import MAX_CLIENT_WALLET
from market import TWENTY_ACTIONS

import action_func
import wallet

import time


def glouton(actions):
    client_wallet = []
    value_client_wallet = 0
    for action in actions:
        if value_client_wallet + action_func.cost(action) <= MAX_CLIENT_WALLET:
            value_client_wallet += action_func.cost(action)
            client_wallet.append(action)
    return client_wallet   
      
        
if __name__ == '__main__':
    
    actions = TWENTY_ACTIONS
    action_func.rentability_calculation(actions)    
    actions = action_func.sort_actions(actions, action_func.rentability, True)
    
    print()
    print("*****************Algorithme glouton******************")
    print()
    tps1 = time.time()
    glouton_client_wallet = glouton(actions)
    
    value_glouton_client_wallet = wallet.value_wallet(glouton_client_wallet)
    income_glouton_client_wallet = wallet.income_wallet(glouton_client_wallet)
    
    glouton_client_wallet = action_func.sort_actions(glouton_client_wallet, action_func.cost, False)
    wallet.view_wallet(glouton_client_wallet)
    
    print("Valeur du portefeuille du client: ",
          str(value_glouton_client_wallet), " euros")    
    print("bénéfices du client à 2 ans: ", 
          str(income_glouton_client_wallet), " euros")
    tps2 = time.time()
    print()
    print("***************** ", round(tps2 - tps1, 2), " s ******************")
    print()
