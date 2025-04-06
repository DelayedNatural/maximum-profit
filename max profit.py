print("\n")

possible = False
while possible == False:
    QD1 = int(input("Give QD of the first equation: "))
    P1 = int(input("Give the P of the first equation: "))
    QD2 = int(input("Give the QD of the second equation: "))
    P2 = int(input("Give the P of the second equation: "))
    if QD1 != 0 and P1 != 0 and QD2 != 0 and P2 != 0 and P2 != P1:
        possible = True
    else:
        print("A value you have provided is 0, which is impossible. Give the correct values.\n")

b = (QD2 - QD1) / (P2 - P1)
a = QD1 - P1 * b

print(f"The equation is: QD = {a}{b}P.\n")

QDtemp = QD1
Ptemp = P1
Pmax = a / b
QDmax = a
QDm = QDmax / 2
Pm = Pmax / 2
if Pm < 0:
    Pm *= -1
print(f"Profit is maximized at QD = {QDm} and P = {Pm}.")