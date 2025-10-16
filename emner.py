emner = []  # создаём пустой список для хранения предметов

def legg_til_emne():  # функция для добавления нового предмета
    kode = input("Skriv emnekode: ")  # ввод кода предмета (например, MAT100)
    navn = input("Skriv emnenavn: ")  # ввод названия предмета (например, Matematikk)
    studiepoeng = int(input("Skriv antall studiepoeng: "))  # ввод количества учебных баллов (преобразуем в число)
    emner.append((kode, navn, studiepoeng))  # добавляем предмет в список как кортеж (код, название, баллы)
    print(f"Emne {kode} - {navn} lagt til!")  # подтверждение, что предмет добавлен

def skriv_ut_alle_emner():  # функция для вывода всех зарегистрированных предметов
    if not emner:  # проверяем, пуст ли список emner
        print("Ingen emner registrert.")  # если пустой, выводим сообщение
    else:  # если список не пустой
        print("\nRegistrerte emner:")  # выводим заголовок
        for e in emner:  # проходим по каждому предмету в списке
            print(f"{e[0]} - {e[1]} ({e[2]} studiepoeng)")  # выводим код, название и количество studiepoeng
