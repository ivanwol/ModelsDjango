from django.db import models
#
#
# class User(models.Model):
#     name = models.CharField(max_length=20)
#     firstname = models.CharField(max_length=20)
#     age = models.IntegerField()
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