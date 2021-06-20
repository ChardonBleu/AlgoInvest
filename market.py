import csv


FOOR_ACTIONS = [{'name': 'action_1', 'price': 20, 'profit': 5},
                {'name': 'action_2', 'price': 30, 'profit': 10},
                {'name': 'action_3', 'price': 50, 'profit': 15},
                {'name': 'action_4', 'price': 70, 'profit': 20}]

TWENTY_ACTIONS = [{'name': 'action_1', 'price': 20, 'profit': 5},
                  {'name': 'action_2', 'price': 30, 'profit': 10},
                  {'name': 'action_3', 'price': 50, 'profit': 15},
                  {'name': 'action_4', 'price': 70, 'profit': 20},
                  {'name': 'action_5', 'price': 60, 'profit': 17},
                  {'name': 'action_6', 'price': 80, 'profit': 25},
                  {'name': 'action_7', 'price': 22, 'profit': 7},
                  {'name': 'action_8', 'price': 26, 'profit': 11},
                  {'name': 'action_9', 'price': 48, 'profit': 13},
                  {'name': 'action_10', 'price': 34, 'profit': 27},
                  {'name': 'action_11', 'price': 42, 'profit': 17},
                  {'name': 'action_12', 'price': 110, 'profit': 9},
                  {'name': 'action_13', 'price': 38, 'profit': 23},
                  {'name': 'action_14', 'price': 14, 'profit': 1},
                  {'name': 'action_15', 'price': 18, 'profit': 3},
                  {'name': 'action_16', 'price': 8, 'profit': 8},
                  {'name': 'action_17', 'price': 4, 'profit': 12},
                  {'name': 'action_18', 'price': 10, 'profit': 14},
                  {'name': 'action_19', 'price': 24, 'profit': 21},
                  {'name': 'action_20', 'price': 114, 'profit': 18}]


def convert_csv_in_dict(fichier_csv):
    Dict_actions = []
    with open(fichier_csv, newline='') as csvfile:
        reader= csv.DictReader(csvfile)
        for row in reader:
            Dict_actions.append(row)
    return Dict_actions



if __name__ == "__main__":
    
    THOUSAND_ACTIONS_1 = convert_csv_in_dict('dataset1.csv')    
    print(THOUSAND_ACTIONS_1)
    
