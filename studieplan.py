studieplan = {}     # Этот файл отвечает за хранение и управление структурой учебного плана
                    # Создает глобальный словарь
def legg_til_i_studieplan():
    semester = input("Skriv semester (for eksempel 'V2025'): ")
    emnekode = input("Skriv emnekode: ")

    if semester not in studieplan:    # Если семестр не в словаре, то он создается
        studieplan[semester] = []
    studieplan[semester].append(emnekode)    # Код предмета добавляется в список этого семестра
    print(f"Emne {emnekode} lagt til i {semester}.")

def skriv_ut_studieplan():
    if not studieplan:
        print("Ingen studieplan registrert.")
    else:
        print("\nStudieplan:")
        for semester, emner in studieplan.items():    # Проход по всем семестрам в словаре и вывод кодов предметов с запятой
            print(f"{semester}: {', '.join(emner)}")
