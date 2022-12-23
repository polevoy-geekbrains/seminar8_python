# Задача: *Создать информационную систему позволяющую работать с сотрудниками некой компании \ студентами вуза \ учениками школы. В рамках обсуждения необходимо нарисовать “архитектуру” (например, в виде блок-схемы) для работы данного приложения.*

## Описание программы:

Программа "Электронный дневник"

- Для запуска программы необходимо запустить -> main.py

Интерфейс разделен на два вида пользователей:
1. Учитель - ему доступно четыре функции:
- ввод данных об ученике (фамилия, имя, отчество, класс);
- изменение этих данных;
- внесение оценок;
- просмотр успеваемости учеников по всем предметам или по конкретному.

2. Ученик - доступна функция просмотра успеваемости учеников, как своей так и других.

Поиск производится по фамилии.

Ситуация возможного существования учеников с одинаковой информацией разрешена запросом порядкового номера интересующего ученика, который выводится в консоль вместе с фамилией, именем, отчеством и номером класса.

Данные и изменения сохраняются в файле с расширением .csv. При желании его можно просматривать через MS Excel или аналогичные программы.

Скопинцев Алексей - работа с search.py и вся работа поиска в программе.

Палагнюк Руслан - работа c файлом add_info.py, и объединению файлов группы в репозиторий.

Майоров Андрей - работа с user_interface.py и составление блок-схемы структуры программы

Нилова Екатерина - работа с check.py 

Сафатов Антон - работа с creating_file.py

Полевой Александр - работа с main.py, добавление логирования и ассистирование 

## Блок-схема:
![БлокСхема](<Блок-схема.jpg>)