A = 1.92
B = 13.91
C = 2.82

TAB = 355
TAC = 690

TBC = TAC - TAB

D = (TBC*A + TAC*B) / (TAC + TBC)

VibNum = (D - B) / TBC

print('Point D is at: ', D)
print('The rate of vibration is: ', VibNum)

ChenVibNum = (abs(A - B)) / (TAC + TBC)

print('The Chens rate of vibration is: ', ChenVibNum)

