from studieplan import studieplan  # импортируем словарь 'studieplan' из файла studieplan.py

def sjekk_gyldighet():  # определяем функцию для проверки действительности учебного плана
    # считаем общее количество studiepoeng во всей учебной программе
    # len(emner) * 10 предполагает, что каждый предмет даёт 10 studiepoeng
    total_studiepoeng = sum(len(emner) * 10 for emner in studieplan.values())
    
    # проверяем, набрано ли 180 или больше учебных баллов
    if total_studiepoeng >= 180:
        print("Studieplanen er gyldig (180 studiepoeng eller mer).")  # если >= 180, план действителен
    else:
        # если меньше 180, показываем, сколько всего баллов набрано
        print(f"Studieplanen er IKKE gyldig ({total_studiepoeng} studiepoeng).")
