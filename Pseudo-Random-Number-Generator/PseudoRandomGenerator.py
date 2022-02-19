seed = 0

seed = input("please type a seed\n")

psRandNum = ""
multiplication = ""

for i in range(0,22):

    try :
        multiplication = str(int(seed)*int(seed))
    except:
        seed = seed[0]
        seed = (int(seed[0]) + 5)
        multiplication = str(int(seed)*int(seed))
        
    psRandNum = psRandNum[:] + multiplication[:]
    
    seed = str(multiplication[1:-1])

print(psRandNum)
