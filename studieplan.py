studieplan = {}

def legg_til_i_studieplan():
    semester = input("Skriv semester (for eksempel 'V2025'): ")
    emnekode = input("Skriv emnekode: ")

    if semester not in studieplan:
        studieplan[semester] = []
    studieplan[semester].append(emnekode)
    print(f"Emne {emnekode} lagt til i {semester}.")

def skriv_ut_studieplan():
    if not studieplan:
        print("Ingen studieplan registrert.")
    else:
        print("\nStudieplan:")
        for semester, emner in studieplan.items():
            print(f"{semester}: {', '.join(emner)}")
