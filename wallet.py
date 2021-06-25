import market
from action import Action


class Wallet:
    """Classe modélisant un portefeuille d'actions."""

    def __init__(self):
        """A l'instanciation on crée un portefeuille vide d'actions."""

        self.value = 0
        self.income = 0
        self.actions = []

    def __str__(self):
        """Permet l'affichage de la valeur et du gain à deux ans du
        portefeuille sur une ligne.

        Returns:
            [string] -- valeur(€) et gain(€) à 2 ans du portefeuille
        """
        return f"value wallet: {round(self.value, 2)}€ - \
profit wallet: {round(self.income, 2)}€"

    def update_value_wallet(self):
        """Met à jour la valeur du portefeuille

        Returns:
            [int] -- valeur du portefeuille (€)
        """
        self.value = 0
        for action in self.actions:
            self.value += action.price
        return round(self.value, 2)

    def update_income_wallet(self):
        """Met à jour le gain à deux ans du portefeuille

        Returns:
            [int] -- gain du portefeuille (€)
        """
        self.income = 0
        for action in self.actions:
            self.income += action.profit * action.price / 100
        return round(self.income, 2)

    def sort_actions_by_rentability(self, reverse_order=False):
        """Trie les actions par rentalibité décroissante.
        Sert à l'algorithme glouton

        Keyword Arguments:
            reverse_order {bool} -- sens du tri. Par défaut décroissant
                                    (default: {False})
        """
        self.actions = sorted(
            self.actions, key=lambda action: action.rentability, reverse=reverse_order
        )

    def view_wallet(self):
        """Permet l'affichage de la liste des actions du portefeuille"""
        print("action      coût(€)   bénéfice(%)")
        for action in self.actions:
            print(action)
        print()
        print(self)
        print()

    def choice_market(self):
        """Permet de choisir le panel d'actions pour le marché d'actions dans
        le cas des algorithmes glouton et dynamiques

        Returns:
            [Dict], [string]  -- dictionnaire des actions et titre du marché
                                 correspondant
        """
        TWENTY_ACTIONS = market.TWENTY_ACTIONS
        THOUSAND_ACTIONS_1 = market.convert_csv_in_dict("dataset1.csv")
        THOUSAND_ACTIONS_2 = market.convert_csv_in_dict("dataset2.csv")

        print("choisir le panel d'actions à tester:")
        print("1: TWENTY_ACTIONS, 2: dataset1, 3: dataset2")
        bool = True
        while bool:
            choice = input(">> ")
            if choice == '1':
                CHOICE = TWENTY_ACTIONS
                title = "panel de 20 actions"
                bool = False
            elif choice == '2':
                CHOICE = THOUSAND_ACTIONS_1
                title = "dataset1"
                bool = False
            elif choice == '3':
                CHOICE = THOUSAND_ACTIONS_2
                title = "dataset2"
                bool = False
            else:
                continue
        
        return CHOICE, title