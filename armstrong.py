def is_armstrong(n: int) -> bool:
    if n < 0:
        return False
    s_n = str(n)
    power = len(s_n)
    return sum(int(d) ** power for d in s_n) == n

if __name__ == "__main__":
    # Ez a rész csak akkor fut, ha kézzel indítod a fájlt.
    # Teszteléskor (importáláskor) ez kimarad, így nem okoz hibát.
    try:
        szam = int(input("Adjon meg egy számot: "))
        if is_armstrong(szam):
            print(f"{szam} egy Armstrong szám.")
        else:
            print(f"{szam} nem egy Armstrong szám.")
    except ValueError:
        print("Kérjük, egész számot adjon meg!")
