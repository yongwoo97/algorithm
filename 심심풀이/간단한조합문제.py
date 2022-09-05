import random
main = round(random.random(), 5)
a_list = []
b_list = []

a_list += [round(main-(0.1*i), 5)for i in range(1, 11)]
b_list += [round(-(i), 5) for i in reversed(a_list)]

result = a_list + b_list
result.sort()
result = result[len(result)//2:]
print(main)
for i in result:
    for j in result:
        if round(i+j, 5) == 0.1:
            print(f'{i} + {j} = {round(i+j, 5)}')
            #exit()

if not None:
    print('he')