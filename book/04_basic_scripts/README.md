# Создание базовых скриптов

Если говорить в целом, то скрипт это обычный файл.
В этом файле хранится последовательность команд, которые необходимо выполнить.

Начнем с базового скрипта. Попробуем просто вывести на стандартный поток вывода несколько строк.
Для этого надо создать файл access_template.py с таким содержимым:
```python
access_template = ['switchport mode access',
                   'switchport access vlan %d',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

print '\n'.join(access_template) % 5
```

После этого, сохраняем его и переходим в командную строку.

Запускаем скрипт:
```python
$ python access_template.py
switchport mode access
switchport access vlan 5
switchport nonegotiate
spanning-tree portfast
spanning-tree bpduguard enable
```

Сначала мы объединяем элементы списка в строку, которая разделена символом '\n', а затем подставляем номер VLAN, используя форматирование строк.

> Ставить расширение .py у файла не обязательно. 

> Но, если вы используете windows, то это желательно делать, так как Windows использует расширение файла, для определения того как обрабатывать файл.

> В курсе все скрипты, которые будут создаваться, используют расширение .py.
Можно сказать, что это "хороший тон", создавать скрипты Python  с таким расширением.

### Кодировка

Теперь попробуем напечатать текст, который мы набрали кириллицей (access_template_encoding.py):
```python
access_template = ['switchport mode access',
                   'switchport access vlan %d',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

print "Конфигурация интерфейса в режиме access:"
print '\n'.join(access_template) % 5
```

При попытке запустить скрипт получаем такую ошибку:
```python
$ python access_template_encoding.py
  File "access_template_encoding.py", line 7
SyntaxError: Non-ASCII character '\xd0' in file access_template_encoding.py on line 7,
but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
```

Для того чтобы не было такой ошибки, необходимо добавить в начале файла такую строку:
```python
# -*- coding: utf-8 -*-
```

Тогда скрипт access_template_encoding.py будет выглядеть так:
```python
# -*- coding: utf-8 -*-

access_template = ['switchport mode access',
                   'switchport access vlan %d',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

print "Конфигурация интерфейса в режиме access:"
print '\n'.join(access_template) % 5
```

Теперь ошибки нет:
```
$ python access_template_encoding.py
Конфигурация интерфейса в режиме access:
switchport mode access
switchport access vlan 5
switchport nonegotiate
spanning-tree portfast
spanning-tree bpduguard enable
```


### Исполняемый файл

Для того, чтобы файл был исполняемым и не нужно было каждый раз писать python перед вызовом файла, нужно:
* сделать файл исполняемым (для linux)
* в первой строке файла должна находится строка ```#!/usr/bin/env python```

Пример файла access_template_exec.py:
```python
#!/usr/bin/env python

access_template = ['switchport mode access',
                   'switchport access vlan %d',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

print '\n'.join(access_template) % 5
```

После этого:
```
chmod +x access_template_exec.py
```

Теперь можно вызывать файл таким образом:
```
$ ./access_template_exec.py
```