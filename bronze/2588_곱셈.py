n1 = input()
n2 = input()

int_n1 = int(n1)
int_n2 = int(n2)
for i in range(3):
    print(int_n1 * int(n2[len(n2)-i-1]))
print(int_n1 * int_n2)