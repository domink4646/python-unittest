szam = int(input("Adjon meg egy számot: "))


def is_armstrong(n: int) -> bool:
    if n < 0:
        return False
    s_n = str(n)
    power = len(s_n)
    return sum(int(d) ** power for d in s_n) == n

if is_armstrong(szam):
    print(f"{szam} egy Armstrong szám.")
else:
    print(f"{szam} nem egy Armstrong szám.")
