from studieplan import studieplan

def sjekk_gyldighet():
    total_studiepoeng = sum(len(emner) * 10 for emner in studieplan.values())
    if total_studiepoeng >= 180:
        print("Studieplanen er gyldig (180 studiepoeng eller mer).")
    else:
        print(f"Studieplanen er IKKE gyldig ({total_studiepoeng} studiepoeng).")
