import action_func

def value_wallet(client_wallet):
    value = 0
    for action in client_wallet:
        value += action_func.cost(action)
    return value

def income_wallet(client_wallet):
    income_w = 0
    for action in client_wallet:
        income_w += action_func.income(action) * action_func.cost(action) / 100        
    return round(income_w,2)
