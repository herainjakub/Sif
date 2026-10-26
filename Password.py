Password = "Heslo"
Attempts = 5

while True:
    Guess = input(":")
    if(Guess == Password):
        print("Správně")
        break
    else: 
        Attempts -= 2
        if(Attempts == 0):
            print("Zablokované heslo")
            break
        else:
            print(f"Zbývá ještě {Attempts} Pokusů ")
