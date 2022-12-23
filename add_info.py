import csv
import logger

def add_info(file):
    last_name = input('Введите фамилию ученика: ').capitalize()
    logger.add(last_name, 'добавление ученика')
    first_name = input('Введите имя ученика: ').capitalize()
    middle_name = input('Введите отчество ученика: ').capitalize()
    num_class = input('Введите класс ученика: ').lower()
    with open(file, 'a', encoding = 'UTF-8', newline='') as data:
        fields = ['Фамилия', 'Имя', 'Отчество', 'Класс', 'Литература', 'Русский язык', 'Математика', 'Физкультура', 'Информатика', 'Иностранный язык',\
                'Биология', 'Химия', 'История', 'География', 'Физика']
        writer = csv.DictWriter(data, fieldnames= fields)
        writer.writerow({'Фамилия': last_name, 'Имя': first_name, 'Отчество': middle_name, 'Класс': num_class})

        
def add_grades(file,word):
    subject = input('Введите название предмета: ').capitalize()
    grade = input('Введите оценку: ')
    number = int(input('Введите порядковый номер, указанный выше перед фамилией ученика: '))
    my_dict = []
    with open(file, 'r', encoding = 'UTF-8', newline='') as data:
        for row in csv.reader(data):
            my_dict.append({'Фамилия': row[0], 'Имя': row[1], 'Отчество': row[2], 'Класс': row[3], 'Литература': row[4], 'Русский язык': row[5], 'Математика': row[6],\
                      'Физкультура': row[7], 'Информатика': row[8], 'Иностранный язык': row[9], 'Биология': row[10], 'Химия': row[11], 'История': row[12],\
                          'География': row[13], 'Физика': row[14]})
    with open(file, 'r', encoding = 'UTF-8', newline='') as data:
        count = 0
        total = 0
        file_reader = csv.DictReader(data, delimiter=',')
        for line in file_reader:
            total +=1
            for i in ['Фамилия','Имя','Отчество','Класс']:
                if word == '' and total == number:
                    my_dict[total][subject] += f'{grade} '
                    with open(file, 'w', encoding = 'UTF-8', newline='') as data:
                        fields = ['Фамилия', 'Имя', 'Отчество', 'Класс', 'Литература', 'Русский язык', 'Математика', 'Физкультура', 'Информатика', 'Иностранный язык',\
                                'Биология', 'Химия', 'История', 'География', 'Физика']
                        writer = csv.DictWriter(data, fieldnames= fields)
                        writer.writerows(my_dict)
                        return
                if word == line[i]:
                    count += 1
                if count == number:
                    my_dict[total][subject] += f'{grade} '
                    with open(file, 'w', encoding = 'UTF-8', newline='') as data:
                        fields = ['Фамилия', 'Имя', 'Отчество', 'Класс', 'Литература', 'Русский язык', 'Математика', 'Физкультура', 'Информатика', 'Иностранный язык',\
                                'Биология', 'Химия', 'История', 'География', 'Физика']
                        writer = csv.DictWriter(data, fieldnames= fields)
                        writer.writerows(my_dict)
                        return
    

def change_info(file,word):
    print('Введите цифру, соответствующую типу информации, которую нужно изменить:')
    type_info = int(input('1 - фамилия\n2 - имя\n3 - отчество\n4 - класс\n'))
    column = ''
    if type_info == 1:
        column = 'Фамилия'
    elif type_info == 2:
        column = 'Имя'
    elif type_info == 3:
        column = 'Отчество'
    else:
        column = 'Класс'
    number = int(input('Введите порядковый номер, указанный выше перед фамилией ученика: '))
    my_dict = []
    with open(file, 'r', encoding = 'UTF-8', newline='') as data:
        for row in csv.reader(data):
            my_dict.append({'Фамилия': row[0], 'Имя': row[1], 'Отчество': row[2], 'Класс': row[3], 'Литература': row[4], 'Русский язык': row[5], 'Математика': row[6],\
                      'Физкультура': row[7], 'Информатика': row[8], 'Иностранный язык': row[9], 'Биология': row[10], 'Химия': row[11], 'История': row[12],\
                          'География': row[13], 'Физика': row[14]})
    new_info = input('Введите новую информацию: ')
    with open(file, 'r', encoding = 'UTF-8', newline='') as data:
        count = 0
        total = 0
        file_reader = csv.DictReader(data, delimiter=',')
        for line in file_reader:
            total +=1
            print(total)
            for i in ['Фамилия','Имя','Отчество','Класс']:
                if word == '' and total == number:
                    my_dict[total][column] = new_info
                    with open(file, 'w', encoding = 'UTF-8', newline='') as data:
                        fields = ['Фамилия', 'Имя', 'Отчество', 'Класс', 'Литература', 'Русский язык', 'Математика', 'Физкультура', 'Информатика', 'Иностранный язык',\
                                'Биология', 'Химия', 'История', 'География', 'Физика']
                        writer = csv.DictWriter(data, fieldnames= fields)
                        writer.writerows(my_dict)
                        return
                if word == line[i]:
                    count += 1
                if count == number:
                    my_dict[total][column] = new_info
                    with open(file, 'w', encoding = 'UTF-8', newline='') as data:
                        fields = ['Фамилия', 'Имя', 'Отчество', 'Класс', 'Литература', 'Русский язык', 'Математика', 'Физкультура', 'Информатика', 'Иностранный язык',\
                                'Биология', 'Химия', 'История', 'География', 'Физика']
                        writer = csv.DictWriter(data, fieldnames= fields)
                        writer.writerows(my_dict)
                        return