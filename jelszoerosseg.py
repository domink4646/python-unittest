def jelszo_erosseg(jelszo: str) -> int:
    if not isinstance(jelszo, str):
        raise TypeError("jelszo must be a str")
    
    banned = ["titok", "jelszo", "123"]
    if any(word in jelszo.lower() for word in banned):
        return 0
    
    if len(jelszo) == 0:
        return 0
        
    score = 1
    
    if len(jelszo) >= 5:
        score += 1
    if len(jelszo) >= 8:
        score += 2
        
    spec_count = sum(1 for c in jelszo if not c.isalnum())
    score += spec_count * 2
    
    return score

if __name__ == "__main__":
    print(jelszo_erosseg("hazi_macska_4_life"))           
    print(jelszo_erosseg("ez1feltorhetetlenjelszo"))