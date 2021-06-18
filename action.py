class Action:
    """Classe modélisant une action du marché fincancier
    """
    
    def __init__(self, name, cost, income):
        """A l'instanciation de l'action on passe en arguments le nom, le prix
        et le bénéfice  à 2 ans en pourcentage.
        Attribute:
            self.rentability_action {float}  -- se calcule à l'instanciation

        Arguments:
            name {string} -- nom de l'action
            cost {int} -- prix d'achat de l'action en euros
            income {int} -- bénéfice à 2 ans en pourcentage du pris de l'action
        """
        self.name = name
        self.cost = cost
        self.income = income
        self.rentability_action = self.income / self.cost

    def __str__(self):
        """Permet l'affichage formaté sur une ligne des caractéristiques d'une
        action

        Returns:
            [string] -- "nom       prix(€)      bénéfice(%)"
        """
        return f"{self.name:10} {self.cost:>6}€   {self.income:>10}%"

    @property
    def rentability(self):
        """Permet d'accéder à l'attribut rentability tout en en prenant la
        valeur arrondie au centième.

        Returns:
            [float] -- valeur arrondie au centième de self.rentability_action
        """
        return round(self.rentability_action,2)
