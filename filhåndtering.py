# filhåndtering.py
from emner import emner
from studieplan import studieplan

# Сохранение emner в файл
def lagre_emner():
    with open("emner.txt", "w") as f:
        for e in emner:
            f.write(f"{e[0]},{e[1]},{e[2]}\n")
    print("Emner lagret til fil.")

# Чтение emner из файла
def les_emner():
    global emner
    emner = []
    try:
        with open("emner.txt", "r") as f:
            for line in f:
                kode, navn, studiepoeng = line.strip().split(",")
                emner.append((kode, navn, int(studiepoeng)))
        print("Emner lest fra fil.")
    except FileNotFoundError:
        print("Ingen emner.txt fil funnet.")

# Сохранение studieplan в файл
def lagre_studieplan():
    with open("studieplan.txt", "w") as f:
        for sem, emner_liste in studieplan.items():
            f.write(f"{sem}:{','.join(emner_liste)}\n")
    print("Studieplan lagret til fil.")

# Чтение studieplan из файла
def les_studieplan():
    from studieplan import studieplan as sp
    sp.clear()
    try:
        with open("studieplan.txt", "r") as f:
            for line in f:
                sem, emner_liste = line.strip().split(":")
                sp[sem] = emner_liste.split(",")
        print("Studieplan lest fra fil.")
    except FileNotFoundError:
        print("Ingen studieplan.txt fil funnet.")
