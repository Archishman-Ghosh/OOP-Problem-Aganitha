# OOP-Problem-Aganitha
### Solutions for Oop Problem asked by Aganitha Solutions

Class X is the base class.
Objects of Class X can only be created by Classes A, B & C.

*All Classes have three methods - __init__(), execute() & shutdown().*

* *__init__() takes a name argument & sets the name of the object.*

* *execute() takes a dictionary argument and prints the dictionary content with class name.*

The main program has an infinite loop based menu which has the following options:
#### 1. Add new object 
  * Give object name
  * Choose between Classes A, B & C
#### 2. Delete an object by name
  * Give object name
#### 3. Run execute() method
  * Give object name
  * Enter dictionary contents
#### 4. Quit the program

After quiting, we will get the following stats:
* Number of times execute() is invoked
* Number of times Class A is invoked
* Number of times Class B is invoked
* Number of times Class C is invoked
