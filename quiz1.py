"""Drop Drop"""
def cat():
    """cat"""
    grade = float(input())
    if grade < 1.00:
        print("I'm so sad.")
    elif grade < 2.00:
        xxx = 4 - grade
        print('%.2f' %(xxx))
    else:
        print("I'm so happy.")
cat()
