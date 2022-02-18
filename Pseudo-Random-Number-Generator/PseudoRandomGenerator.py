seed = 0

seed = input("please type a seed\n")

psRandNum = ""


for i in range(0,10):
    multiplication = str(int(seed)*int(seed))
    psRandNum = psRandNum[:] + multiplication[:]
    if multiplication[0] == 0:
        for i in range(1,len(multiplication)):
            if multiplication[i] == 0:
                multiplication = multiplication[i + 1 :]
    seed = str(multiplication[1:-1])

print(psRandNum)
