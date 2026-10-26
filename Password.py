password = "Heslo"
attempts = 3

for attempt in range(attempts, 0, -1):
    guess = input("Zadejte heslo: ")
    
    if guess == password:
        print("Správně")
        break
        
    remaining = attempt - 1
    if remaining == 0:
        print("Zablokované heslo")
    else:
        print(f"Zbývá ještě {remaining} pokusů.")
