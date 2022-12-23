from add_info import add_info, add_grades
from check import check_exist
from add_info import change_info
from search import search_word, search_grades
import logger

def menu():
    flag = input('Введите 0, чтобы продолжить, или любой другой символ, чтобы прервать работу программы... ') #проверка запуска программы
    while flag == '0':
        check_exist()
        print('Введите цифру, соответствующую правам доступа:') 
        flag = input('1 - учитель\n2 - ученик\n')

        while flag != '1' and flag != '2':
            print('Введите цифру, соответствующую правам доступа:') #выясняем кто пытается войти в систему
            flag = input('1 - учитель\n2 - ученик\n')

        if flag == '1': #режим редактор учителя
            print('Введите цифру, соответствующую действию: ')
            choice = int(input('1 - ввести данные об ученике\n2 - изменить данные\n3 - внести оценки\n4 - поиск информации\n'))
            while choice < 1 or choice > 4:
                print('Введите цифру, соответствующую действию: ')
                choice = int(input('1 - ввести данные об ученике\n2 - изменить данные\n3 - внести оценки\n4 - поиск информации\n'))
            
            if choice == 1:
                add_info('pupils.csv')
            elif choice == 2:
                name = input('Введите фамилию имя или отчество ученика, информацию по которому хотите изменить: ').capitalize()
                logger.add(name, 'редактирование')
                search_word(name)
                change_info('pupils.csv',name)
            elif choice == 3:
                name = input('Введите фамилию имя или отчество ученика, которому Вы хотите выставить оценку: ').capitalize()
                logger.add(name, 'выставление оценки')
                search_word(name)
                add_grades('pupils.csv',name)
            elif choice == 4:
                name = input('Введите фамилию имя или отчество ученика, по которому хотите получить информацию или нажмите Enter для вывода всего списка: ').capitalize()
                search_word(name)
                search_grades(name)
        else: # режим просмотра оценок ученика
            name = input('Введите фамилию имя или отчество для поиска: ').capitalize()
            search_word(name)
            search_grades(name)
        flag = input('Введите 0, чтобы продолжить, или любой другой символ, чтобы прервать работу программы... ')
    print('Программа завершена.')
