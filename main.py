from emner import legg_til_emne, skriv_ut_alle_emner
from studieplan import legg_til_i_studieplan, skriv_ut_studieplan
from gyldighetssjekk import sjekk_gyldighet

def meny():
    while True:
        print("\n--- Studieplanmeny ---")
        print("1. Lag et nytt emne")
        print("2. Legg til et emne i studieplanen")
        print("3. Skriv ut alle registrerte emner")
        print("4. Skriv ut studieplanen")
        print("5. Sjekk om studieplanen er gyldig")
        print("6. Lagre data til fil")
        print("7. Les data fra fil")
        print("8. Avslutt")

        valg = input("Velg et nummer: ")

        if valg == "1":
            legg_til_emne()
        elif valg == "2":
            legg_til_i_studieplan()
        elif valg == "3":
            skriv_ut_alle_emner()
        elif valg == "4":
            skriv_ut_studieplan()
        elif valg == "5":
            sjekk_gyldighet()
        elif valg == "8":
            print("Avslutter programmet...")
            break
        else:
            print("Ugyldig valg, prøv igjen!")

if __name__ == "__main__":
    meny()
