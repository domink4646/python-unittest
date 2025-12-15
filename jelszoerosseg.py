def jelszo_erosseg(jelszo: str) -> int:
    if not isinstance(jelszo, str):
        raise TypeError("jelszo must be a str")
    if len(jelszo) == 0:
        return 0
    
    low = jelszo.lower()
    if "jelszo" in low or "123" in low:
        return 0

    strength = 1
    if len(jelszo) >= 5:
        strength += 1
    if len(jelszo) >= 8:
        strength += 2

    special_count = sum(1 for ch in jelszo if ch in ("_", "-", "."))
    strength += 2 * special_count

    return strength


if __name__ == "__main__":
    print(jelszo_erosseg("hazi_macska_4_life"))         

def jelszo_erosseg(jelszo: str) -> int:
    if not isinstance(jelszo, str):
        raise TypeError("jelszo must be a str")
    if len(jelszo) == 0:
        return 0
    
    low = jelszo.lower()
    if "jelszo" in low or "123" in low:
        return 0

    strength = 1
    if len(jelszo) >= 5:
        strength += 1
    if len(jelszo) >= 8:
        strength += 2

    special_count = sum(1 for ch in jelszo if ch in ("_", "-", "."))
    strength += 2 * special_count

    return strength


if __name__ == "__main__":
    print(jelszo_erosseg("hazi_macska_4_life"))           
    print(jelszo_erosseg("ez1feltorhetetlenjelszo"))