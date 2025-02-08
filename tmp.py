import random

def generate_cake():
    fillings = ["полуниця", "смородина", "вишня", "манго-маракуя", "снікерс", "орео", "банан"]
    biscuits = ["шоколадний", "ванільний", "red velvet (червоні шоколадні бісквіти)", "банановий"]
    weights = {
        "370-400 грам": 480,
        "500 грам": 580,
        "700 грам": 800,
        "1 кг": 880,
        "1,5 кг": 1320,
        "2 кг": 1760,
    }
    
    chosen_filling = random.choice(fillings)
    chosen_biscuit = random.choice(biscuits)
    chosen_weight, price = random.choice(list(weights.items()))
    
    cake = {
        "Начинка": chosen_filling,
        "Бісквіт": chosen_biscuit,
        "Вага": chosen_weight,
        "Ціна": f"{price} грн"
    }
    
    return cake

if __name__ == "__main__":
    cake = generate_cake()
    for key, value in cake.items():
        print(f"{key}: {value}")
