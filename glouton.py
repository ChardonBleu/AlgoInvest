from constant import MAX_CLIENT_WALLET
from actions import TWENTY_ACTIONS

def name(action):
    return action['name']

def cost(action):
    return action['cost']

def income(action):
    return action['income']

def rentability_calculation(actions):
    for action in actions:
        action['rentability'] = income(action) / cost(action)

def rentability(action):
    return action['rentability']

def view_actions(actions):
    for action in actions:
        print(f"{name(action)} {")
    print()

def value_wallet(client_wallet):
    value = 0
    for action in client_wallet:
        value += cost(action)
    return value

def income_wallet(client_wallet):
    income_w = 0
    for action in client_wallet:
        income_w += income(action) * cost(action) / 100        
    return round(income_w,2)

def sort_actions(actions, sort_order, reverse_order=False):
    sorted_actions = sorted(actions, key=sort_order, reverse=reverse_order)
    return sorted_actions

def glouton(actions):
    client_wallet = []
    value_client_wallet = 0
    for action in actions:        
        if value_client_wallet + cost(action) <= MAX_CLIENT_WALLET:
            value_client_wallet += cost(action)
            client_wallet.append(action)
    return client_wallet           
        


if __name__ == '__main__':
    
    actions = TWENTY_ACTIONS
    rentability_calculation(actions)    
    actions = sort_actions(actions, rentability, True)  

    print("*****************Algorithme glouton******************")
    glouton_client_wallet = glouton(actions)
    value_glouton_client_wallet = value_wallet(glouton_client_wallet)
    income_glouton_client_wallet = income_wallet(glouton_client_wallet)
    view_actions(glouton_client_wallet)
    print("Valeur du portefeuille du client: ",
          str(value_glouton_client_wallet), " euros")    
    print("bénéfices du client à 2 ans: ", 
          str(income_glouton_client_wallet), " euros")
    print("******************************************************")
    