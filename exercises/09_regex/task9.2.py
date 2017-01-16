# -*- coding: utf-8 -*-

'''
Задание 9.2

Создать функцию return_ip, которая ожидает два аргумента:
* имя файла, в котором находится вывод команды show
* регулярное выражение

Функция должна обрабатывать вывод команды show построчно и возвращать список подстрок,
которые совпали с регулярным выражением (не всю строку, где было найдено совпадение,
а только ту подстроку, которая совпала с выражением).

Регулярное выражение должно описывать подстроку с IP-адресом (то есть, совпадением должен быть IP-адрес).

Проверить работу функции на примере вывода команды sh ip int br (файл sh_ip_int_br.txt).
Вывести список всех IP-адресов из вывода команды.

Обратите внимание, что в данном случае, мы можем не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как мы обрабатываем вывод команды, а не ввод пользователя.
'''
