emner = []

def legg_til_emne():
    kode = input("Skriv emnekode: ")
    navn = input("Skriv emnenavn: ")
    studiepoeng = int(input("Skriv antall studiepoeng: "))
    emner.append((kode, navn, studiepoeng))
    print(f"Emne {kode} - {navn} lagt til!")

def skriv_ut_alle_emner():
    if not emner:
        print("Ingen emner registrert.")
    else:
        print("\nRegistrerte emner:")
        for e in emner:
            print(f"{e[0]} - {e[1]} ({e[2]} studiepoeng)")
