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
    return round(action['rentability'],2)

def sort_actions(actions, sort_order, reverse_order=False):
    sorted_actions = sorted(actions, key=sort_order, reverse=reverse_order)
    return sorted_actions
