import csv

def search_word(word):
    with open('pupils.csv', encoding='UTF-8') as data:
        file_reader = csv.DictReader(data, delimiter=',')
        total = 0
        count = 0
        for line in file_reader:
            if word == '':
                count += 1
                print(f"{count}. {line['Фамилия']} {line['Имя']} {line['Отчество']}, класс {line['Класс']}")
            for i in ['Фамилия','Имя','Отчество','Класс']:
                if word == line[i]:
                    print(f"{count + 1}. {line['Фамилия']} {line['Имя']} {line['Отчество']}, класс {line['Класс']}")
                    count += 1
            total += 1
        print(f'Найдено {count} из всего {total} записей')
        
def search_grades(word):
    with open('pupils.csv', encoding='UTF-8') as data:
        file_reader = csv.DictReader(data, delimiter=',')
        number = int(input('Введите порядковый номер, указанный выше перед фамилией ученика: '))
        subject = input('Введите полное название предмета или слово "все", если хотите посмотреть оценки по всем предметам: ').capitalize()
        count = 1
        if subject == 'Все':
            for line in file_reader:
                if word == '':
                    if number == count:
                        print(f"{line['Фамилия']} {line['Имя']} {line['Отчество']}, класс {line['Класс']}")
                        print(f"Литература: {line['Литература']}\nРусский язык: {line['Русский язык']}\nМатематика: {line['Математика']}\nФизкультура: {line['Физкультура']}")
                        print(f"Информатика: {line['Информатика']}\nИностранный язык: {line['Иностранный язык']}\nБиология: {line['Биология']}\nХимия: {line['Химия']}\nИстория: {line['История']}")
                        print(f"География: {line['География']}\nФизика: {line['Физика']}")
                    count += 1
                for i in ['Фамилия','Имя','Отчество','Класс']:
                    if word == line[i]:
                        if number == count:
                            print(f"{line['Фамилия']} {line['Имя']} {line['Отчество']}, класс {line['Класс']}")
                            print(f"Литература: {line['Литература']}\nРусский язык: {line['Русский язык']}\nМатематика: {line['Математика']}\nФизкультура: {line['Физкультура']}")
                            print(f"Информатика: {line['Информатика']}\nИностранный язык: {line['Иностранный язык']}\nБиология: {line['Биология']}\nХимия: {line['Химия']}\nИстория: {line['История']}")
                            print(f"География: {line['География']}\nФизика: {line['Физика']}")
                        count += 1
        else: 
            for line in file_reader:
                if word == '':
                    if number == count:
                        print(f'{subject}: {line[subject]}')
                    count += 1
                for i in ['Фамилия','Имя','Отчество','Класс']:
                    if word == line[i]:
                        if number == count:
                            print(f'{subject}: {line[subject]}')
                        count += 1