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


def view_actions(actions):
    print(f"action      coût(€)   bénéfice(%)   rentablilité")
    for action in actions:
        print(f"{name(action):10} {cost(action):>6}€   {income(action):>10}%\
  {rentability(action):>13}")
