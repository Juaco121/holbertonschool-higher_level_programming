# 0x0A. Python - Inheritance

## Overview
This project delves farther into the world of OOP and classes/objects

## Requirements
### Python Scripts
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the PEP 8 style (version 1.7.*)
* All your files must be executable
* The length of your files will be tested using `wc`

### Python Test Cases
* Allowed editors: vi, vim, emacs
* All your files should end with a new line
* All your test files should be inside a folder tests
* All your test files should be text files (extension: .txt)
* All your tests should be executed by using this command: python3 -m doctest ./tests/*
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')

## Tasks
### Mandatory
**[0-lookup.py](0-lookup.py)** - Function that returns the list of available attributes and methods of an object
```
vagrant:0x0A-python-inheritance$ ./0-main.py

```

**[1-my_list.py](1-my_list.py)** - Class MyList that inherits from list
```
vagrant:0x0A-python-inheritance$ ./1-main.py
[1, 4, 2, 3, 5]
[1, 2, 3, 4, 5]
[1, 4, 2, 3, 5]
```

**[2-is_same_class.py](2-is_same_class.py)** - Function that returns True if the object is exactly an instance of the specified class
```
vagrant:0x0A-python-inheritance$ ./2-main.py
1 is an instance of the class int
```

**[3-is_kind_of_class.py](3-is_kind_of_class.py)** - Function that returns True if the object is an instance of, or if the object is an instance of a class
```
vagrant:0x0A-python-inheritance$ ./3-main.py
1 comes from int
1 comes from object
```

**[4-inherits_from.py](4-inherits_from.py)** - Function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class
```
vagrant:0x0A-python-inheritance$ ./4-main.py
True inherited from class int
True inherited from class object
```

**[5-base_geometry.py](5-base_geometry.py)** - Empty class BaseGeometry
```
vagrant:0x0A-python-inheritance$ ./5-main.py

```

**[6-base_geometry.py](6-base_geometry.py)** - Class BaseGeometry (based on 5-base_geometry.py)
```
vagrant:0x0A-python-inheritance$ ./6-main.py
[Exception] area() is not implemented
```

**[7-base_geometry.py](7-base_geometry.py)** - Class BaseGeometry (based on 6-base_geometry.py)
```
vagrant:0x0A-python-inheritance$ ./7-main.py
[TypeError] name must be an integer
[ValueError] age must be greater than 0
[ValueError] distance must be greater than 0
```

**[8-rectangle.py](8-rectangle.py)** - Class Rectangle that inherits from BaseGeometry (7-base_geometry.py)
```
vagrant:0x0A-python-inheritance$ ./8-main.py

```

**[9-rectangle.py](9-rectangle.py)** - Class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)
```
[Rectangle] 3/5
15
```

**[10-square.py](10-square.py)** - Class Square that inherits from Rectangle (9-rectangle.py)
```
vagrant:0x0A-python-inheritance$ ./10-main.py
[Rectangle] 13/13
169
```

**[11-square.py](11-square.py)** - Class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py)
```
vagrant:0x0A-python-inheritance$ ./11-main.py
[Square] 13/13
169
```

2020 - All programs written by Juan Granada ([@juangraram](https://twitter.com/JuanGraRam)) at [Holberton School](https://www.holbertonschool.com/)