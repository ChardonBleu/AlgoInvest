class Action:
    
    def __init__(self, name, cost, income):
        self.name_action = name
        self.cost_action = cost
        self.income_action = income
        self.rentability_action = self.income_action / self.cost_action

    def __str__(self):
        return f"{self.name_action:10} {self.cost_action:>6}€   {self.income_action:>10}%"


    @property
    def name(self):
        return self.name_action

    @property
    def cost(self):
        return self.cost_action

    @property
    def income(self):
        return self.income_action

    @property
    def rentability(self):
        return round(self.rentability_action,2)
