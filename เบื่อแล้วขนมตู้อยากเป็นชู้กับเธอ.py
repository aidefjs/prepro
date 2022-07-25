""" เบื่อแล้วขนมตู้ อยากเป็นชู้กับเธอ """
def main():
    money = int(input())
    water = int(input())
    snack1 = int(input())  
    snack2 = int(input())
    snack3 = int(input())
    result = (money - water) % 3
    
    if result == 0:
        xxx1 = 10 * snack1
    elif result == 1:
        xxx2 = 15 * snack1
    elif result == 2:
        xxx3 = 20 * snack1
    else:
        print('"Now you have', money, 'left."', '\nYou don’t have enough money!')
    
    result2 = result % 3
    if result2 == 0:
        xxx4 = 12 * snack2
    elif result2 == 1:
        xxx5 = 15 * snack2
    elif result2 == 2:
        xxx6 = 18 * snack2
    else:
        print('"Now you have', money, 'left."', '\nYou don’t have enough money!')

    result3 = result2 % 3
    if result3 == 0:
        xxx7 = 5 * snack3
        print('"Now you have', result3, 'left."', '\nHere's your order!', "\nWater: " + water, "baht", "\nSnack number 1:", xxx1, "baht", "\nSnack number 2:", xxx1, "baht",)
    elif result2 == 1:
        xxx8 = 7 * snack3
    elif result3 == 2:
        xxx9 = 9 * snack3
    else:
        print('"Now you have', money, 'left."', '\nYou don’t have enough money!')

print('"Now you have', result3, 'left."', '\nHere's your order!', "\nWater: " + water, "baht", "\nSnack number 1:)
main()
