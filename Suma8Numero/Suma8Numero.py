NUM = 8
nums = [0]*NUM

total = 0

for i in range(NUM) :
    nums[i] = int(input("Ingresa numero:  """))
    total += nums[i]

print("El resultado es:  ", total)

