even_num = []
i = 0
while len(even_num) <= 100:
    if i%2 == 0:
        even_num.append(i)
    
    i = i+1


print(even_num)