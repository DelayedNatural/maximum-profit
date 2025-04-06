print("\n")

possible = False
while possible == False:
    QD1 = int(input("Give QD of the first equation: "))
    P1 = int(input("Give the P of the first equation: "))
    QD2 = int(input("Give the QD of the second equation: "))
    P2 = int(input("Give the P of the second equation: "))
    b = (QD2 - QD1) / (P2 - P1) #calculate b
    a = QD1 - P1 * b #calculate a
    if QD1 != 0 and P1 != 0 and QD2 != 0 and P2 != 0 and P2 != P1 and (QD2 - QD1) / (P2 - P1) !=0 and QD1 - P1 * b != 0:
        possible = True
    else:
        print("The values you have provided are impossible. Give the correct values.\n")

print(f"The equation is: QD = {a}{b}P.\n")

QDm = a / 2
Pm = (a / b) / 2
if Pm < 0:
    Pm *= -1
print(f"Profit is maximized at QD = {QDm} and P = {Pm}.")