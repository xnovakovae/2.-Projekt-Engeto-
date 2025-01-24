import random
import time

def vygeneruj_tajne_cislo():
    """Vygeneruje ctyrmistne tajne cislo s unikatnimi cislicemi a nezacinajici nulou."""
    while True:
        cislo = random.sample(range(10), 4)  # Nahodna cisla od 0 do 9, ctyri unikatni cislice
        if cislo[0] != 0:  # Prvni cislice nesmi byt 0
            return ''.join(map(str, cislo))

def over_vstup(uzivatelsky_vstup):
    """Overi, zda je vstup ctyrmistne cislo s unikatnimi cislicemi a nezacinajici nulou."""
    if len(uzivatelsky_vstup) != 4:
        return "Vstup musi mit presne 4 cislice."
    if not uzivatelsky_vstup.isdigit():
        return "Vstup smi obsahovat pouze cisla."
    if uzivatelsky_vstup[0] == '0':
        return "Cislo nesmi zacinat nulou."
    if len(set(uzivatelsky_vstup)) != 4:
        return "Vstup nesmi obsahovat duplicitni cislice."
    return None

def vyhodnot_hadanku(tajne_cislo, tip):
    """Porovna tajne cislo s tipem uzivatele a vrati pocet bulls a cows.""" 
    bulls = sum(1 for tajne, t in zip(tajne_cislo, tip) if tajne == t)
    cows = sum(1 for t in tip if t in tajne_cislo) - bulls
    return bulls, cows

def hraj_hru():
    """Hlavni funkce pro spusteni hry Bulls and Cows."""
    print("Ahoj!")
    print("-" * 40)
    print("Myslim si nahodne ctyrmistne cislo.")
    print("Pojdme si zahrat hru Bulls and Cows.")
    print("-" * 40)
    
    tajne_cislo = vygeneruj_tajne_cislo()
    pocet_pokusu = 0
    start_cas = time.time()
    
    while True:
        tip = input("Zadej ctyrmistne cislo, ktere nezacina nulou a ve kterem se cislice neopakuji: ").strip()
        chyba = over_vstup(tip)
        if chyba:
            print(chyba)
            continue
        
        pocet_pokusu += 1
        bulls, cows = vyhodnot_hadanku(tajne_cislo, tip)
        if bulls == 4:
            konec_cas = time.time()
            print(f"Spravne, uhodl(a) jsi cislo na {pocet_pokusu} pokusu!")
            print(f"Cas: {int(konec_cas - start_cas)} sekund")
            break
        else:
            text_bulls = "bull" if bulls == 1 else "bulls"
            text_cows = "cow" if cows == 1 else "cows"
            print(f"{bulls} {text_bulls}, {cows} {text_cows}")

# Spusteni hry
if __name__ == "__main__":
    hraj_hru()
