class Wallet:
    """Classe modélisant un portefeuille d'actions.
    """

    def __init__(self):
        """A l'instanciation on crée un portefeuille vide d'actions.
        """
        self.value = 0
        self.income = 0
        self.actions = []

    def __str__(self):
        """Permet l'affichage de la valeur et du gain à deux ans du
        portefeuille sur une ligne.

        Returns:
            [string] -- valeur(€) et gain(€) à 2 ans du portefeuille
        """
        return f"value wallet: {self.value}€ -\
profit wallet: {round(self.income, 2)}€"

    def update_value_wallet(self):
        """Met à jour la valeur du portefeuille

        Returns:
            [int] -- valeur du portefeuille (€)
        """
        for action in self.actions:
            self.value += action.cost
        return self.value

    def update_income_wallet(self):
        """Met à jour le gain à deux ans du portefeuille

        Returns:
            [int] -- gain du portefeuille (€)
        """
        for action in self.actions:
            self.income += action.income * action.cost / 100
        return round(self.income, 2)

    def sort_actions_by_rentability(self, reverse_order=False):
        """Trie les actions par rentalibité décroissante.
        Sert à l'algorithme glouton

        Keyword Arguments:
            reverse_order {bool} -- sens du tri. Par défaut décroissant
                                    (default: {False})
        """
        self.actions = sorted(self.actions,
                              key=lambda action: action.rentability,
                              reverse=reverse_order)

    def view_wallet(self):
        """Permet l'affichage de la liste des actions du portefeuille
        """
        print("action      coût(€)   bénéfice(%)")
        for action in self.actions:
            print(action)
        print()
        print(self)
        print()
