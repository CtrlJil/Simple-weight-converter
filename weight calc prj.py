weight = int(input("Weight: "))
unit = input("(L)bs or (K)g: ")
if unit.upper() == ("L"):
    weight = weight * 0.45
    print(f'You are {weight} kilos')
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")