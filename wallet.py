from constant import MAX_CLIENT_WALLET

class Wallet:
    
    def __init__(self):

        self.value = 0
        self.income = 0
        self.wallet_actions = []

    def __str__(self):
        return f"value wallet: {self.value}€ - profit wallet: {round(self.income, 2)}€"

    @property
    def actions(self):
        return self.wallet_actions

    def update_value_wallet(self):
        for action in self.actions:
            self.value += action.cost
        return self.value

    def update_income_wallet(self):
        for action in self.actions:
            self.income += action.income * action.cost / 100        
        return round(self.income,2)

    def view_wallet(self):
        print(f"action      coût(€)   bénéfice(%)")
        for action in self.actions:
            print(action)
        print()
        

    def sort_actions_by_cost(self, reverse_order=False):
        self.wallet_actions = sorted(self.wallet_actions, key=lambda action: action.cost, reverse=reverse_order)

    
    def sort_actions_by_rentability(self, reverse_order=False):
        self.wallet_actions = sorted(self.wallet_actions, key=lambda x: x.rentability_action, reverse=reverse_order)

    
