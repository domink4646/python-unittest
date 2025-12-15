szam = int(input("Adjon meg egy számot: "))


def is_armstrong(n: int) -> bool:
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n

if is_armstrong(szam):
    print(f"{szam} egy Armstrong szám.")
else:
    print(f"{szam} nem egy Armstrong szám.")
