from django.db import models
from django.db.models import F
#
#
# class User(models.Model):
#     name = models.CharField(max_length=20)
#     firstname = models.CharField(max_length=20)
#     age = models.IntegerField()


class User(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    age = models.PositiveSmallIntegerField()
#
#
# class TypeFields(models.Model):
#     field1 = models.BinaryField()  # Хранит бинарные данные(видео, музыку и т.д.)
#     field2 = models.BooleanField()  # Хранит значения 0 или 1(True or False)
#     field3 = models.NullBooleanField()  # Хранит значения True, False and Null
#     field4 = models.DateField()  # Хранит дату
#     field5 = models.TimeField()  # Хранит время
#     field6 = models.DateTimeField()  # Хранит дату и время
#     field7 = models.DurationField()  # Хранит период времени
#     field8 = models.AutoField()  # Хранит целочисленное значение которое автоматически инкрементируется(увеличивается на еденицу)
#     field9 = models.BigIntegerField()  # Хранит целочисленное число в диапазоне(-9223372036854775808 до 9223372036854775807)
#     field10 = models.FloatField()  # Хранит значения чисел с плавающей точкой
#     field11 = models.IntegerField()  # Хранит значения целых чисел в диапазоне(-2147483648 до 2147483647)
#     field12 = models.PositiveIntegerField()  # Хранит значения целых положительных чисел в диапазоне(0 до 2147483647)
#     field13 = models.PositiveSmallIntegerField()  # Хранит значения целых положительных чисел в диапазоне(0 до 32767)
#     field14 = models.SmallIntegerField()  # Хранит значения целых чисел в диапазоне(-32768 до 32767)
#     field15 = models.CharField(max_length=20)  # Хранит строку длиной неболее которую мы указываем
#     field16 = models.TextField()  # Хранит строку неопределенной длинны
#     field17 = models.EmailField()  # Хранит строку неболее 100 символов и имеет особую валидацию
#     field18 = models.FileField()  # Хранит строку которая предоставляет имя файла
#     field19 = models.FilePathField()  # Хранит строку которая предоставляет путь файла(максимальная длина 100 символов)
#     field20 = models.ImageField()  # Хранит строку которая предоставляет информацию об изображении
#     field21 = models.GenericIPAddressField()  # Хранит строку имеет особую валидацию для IP
#     field22 = models.SlugField()  # Хранит строку состаящую только из символов нижнего регистра
#     field23 = models.URLField()  # Хранит строку имеет особую валидацию для URL


# class Person(models.Model):  # Создание класса Person который является моделью
#     name = models.CharField(max_length=20)  # Создание поля модели типа данных стринг
#     age = models.PositiveSmallIntegerField()  # Создание поля модели типа данных инт

# create
# object1 = Person.objects.create(name='Artem', age=23)  # Создание объекта класса и занесение его в DB


# object2 = Person(name='Nazar', age=18)  # Создание объекта класса
# object2.save()  # Занесение объекта в DB

# read
# object3 = Person.objects.get(name='Serhii')  # Вытаскиваем объект из DB по определеному параметру
# print(object3)
# print(object3.age)


# object4, created = Person.objects.get_or_create(name='Vika', age=20)  # Вытаскиваем объект при его наличии, в случаи отсутствия добавляем его
# print(object4.name)
# print(object4.age)
# print(created)


# object5 = Person.objects.all()  # Вытаскиваем все объекты из таблицы DB
# print(object5)


# object6 = Person.objects.filter(age=18, name='Ivan')  # Получает объекты по определенным критериям
# print(object6)


# object7 = Person.objects.exclude(age=18)  # Исключает из выборки записи которые соответствуют переданному параметру
# print(object7)


# object8 = Person.objects.filter(age=18).exclude(name='Nazar')  # Вытаскиваем элеенты которые имеют age = 18 и не имеют name = 'Nazar
# print(object8)


# object9 = Person.objects.in_bulk()  # Собирает все элементы в dict
# for id in object9:  # Вытягивает id из dict
#     print(object9[id].name)  # Принтуем имя елемента по данному id
#     print(object9[id].age)  # Принтуем age елемента по данному id


# object10 = Person.objects.in_bulk([1, 6, 11])  # Собирает элементы в dict с данными индексами
# for id in object10:  # Вытягивает id из dict
#     print(object10[id].name)  # Принтуем имя елемента по данному id
#     print(object10[id].age)  # Принтуем age елемента по данному id


# object11 = Person.objects.get(id=1)  # Вытаскиваем объект с id 1
# object11.age = 15  # Обращаемся к полю age и присваеваем ему новое значение
# object11.save()  # Сохраняем изменение в БД


# object12 = Person.objects.get(id=7)  # Вытаскиваем объект с id 7
# object12.name = 'Nikita'  # Обращаемся к полю name и присваеваем ему новое значение
# object12.save(update_fields=['name'])  # Сохраняем изменения и обнавляем ТОЛЬКО параметр name


# Person.objects.filter(id=9).update(name='Victor')  # Фильтрует объекты по id 9 и изменяет name на Виктор


# Person.objects.filter(id=7).update(age = F('age') + 12)  # Фильтрует по id 7 и достаем значение age и увеличеваем его на 12


# user1 = User.objects.create(name='Ivan', surname='Ivanow', age=15)
# user2 = User(name='Serhii', surname='Petrow', age=22)
# user2.save()
# user3 = User.objects.get(name='Ivan')
# print(user3.age)
# user4, created = User.objects.get_or_create(name='Cristiano', surname='Petrow', age=37)
# print(user4)
# print(created)
# user5 = User.objects.all()
# print(user5)
# user6 = User.objects.filter(surname='Petrow')
# print(user6)
# user7 = User.objects.in_bulk()
# print(user7)
# for id in user7:
#     print(user7[id].name)
#     print(user7[id].surname)
#     print(user7[id].age)
# User.objects.filter(id=3).update(surname='Shevchenko')


# checked_dict = {
#     'name': 'Ivan',
#     'surname': 'Ivanow',
#     'age': 15
# }
# user8, created = User.objects.update_or_create(id=7, defaults=checked_dict)
# print(user8)
# print(created)


user9 = User.objects.get(id=2)
user9.age = 21
user9.save(update_fields=['age'])