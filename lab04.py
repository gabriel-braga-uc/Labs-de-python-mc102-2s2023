
hpIv = int(input())
hpPi = int(input())
speedIv = int(input())
speedPk = int(input())

while hpIv > 0 and hpPi > 0:
    if speedIv > speedPk and (hpPi > 0 and hpIv > 0):
        atkIv = int(input())
        effIv = float(input())
        atkPk = int(input())
        effPk = float(input())
        hpPi -= atkIv*effIv
        if hpPi > 0:
            hpIv -= atkPk*effPk
    elif speedIv < speedPk and (hpPi > 0 and hpIv > 0):
        atkPk = int(input())
        effPk = float(input())
        atkIv = int(input())
        effIv = float(input())
        hpIv -= atkPk*effPk
        if hpIv > 0:
            hpPi -= atkIv*effIv
    if hpPi <= 0:
        hpPi = 0
    elif hpIv <= 0:
        hpIv = 0
    print("HP Ivysaur =", str(int(hpIv)) + "\nHP Pikachu =", str(int(hpPi)))
if hpPi > hpIv:
    hpIv = 0
    print("Pokémon Vencedor: Pikachu\nHP do Vencedor: " + str(int(hpPi)))
else:
    hpPi = 0
    print("Pokémon Vencedor: Ivysaur\nHP do Vencedor: " + str(int(hpIv)))
