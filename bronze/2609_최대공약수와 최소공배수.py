n, m = map(int, input().split())
def gcd(a, b):
    if a < b:
        a, b = b, a

    if a % b == 0:
        return b

    return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(n, m))
print(lcm(n, m))