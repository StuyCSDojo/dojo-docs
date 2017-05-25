Advance Python: Part II
=======================

* :ref:`advance_python_python_classes`

  * :ref:`advance_python_old_style_vs_new_style`
  * :ref:`advance_python_basics_of_writing_a_class`
  * :ref:`advance_python_constructing_a_class`
  * :ref:`advance_python_expanding_the_basics`
  * :ref:`advance_python_inheritance`

.. _advance_python_python_classes:

Python Classes
--------------
The syntax for writing Python classes are awkward, but Python is still an object oriented language. Take a
look at Python list:
::

   >>> a = []
   >>> a.append(3)
   >>> print a
   [3]

Python lists are one example of a Python object

* The first line instantiates an instance of ``list`` and binds it to ``a``
* In the second line, we call the ``append()`` method of the ``list`` class

.. _advance_python_old_style_vs_new_style:

Old Style Classes vs New Style Classes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
When writing classes in Python 2, you should be aware of the differences between the old style and the new
style.

Old style classes have one of the following class headers:
::

   class <ClassName>:
   # or
   class <ClassName>():
   # or
   class <ClassName>(OldStyleClass)

The last class header would be covered in more details in the inheritance section, but simply means that
the class is extending a class of the old style.

New style classes have one of the following class headers:
::

   class <ClassName>(object):
   # or
   class <ClassName>(NewStyleClass):

As before, the last class header will be covered in more details in the inheritance section.  It simply
denotes that the class is extending another class of the new style.

You should generally avoid writing classes in the old style unless mandated.  The new style comes with a
few new features including the usage of ``super()``, extending builtin types, and more.

.. _advance_python_basics_of_writing_a_class:

Basics of Writing a Class
^^^^^^^^^^^^^^^^^^^^^^^^^
Here is the syntax of a basic class:
::

   class <ClassName>(object):

       def <method_name>(self, arg1, arg2, ...):
	   # do stuff

Here is an example:
::

   class Hello(object):

       def say_hello(self):
	   print 'Hello'

How would you use it?
::

   >>> a = Hello()
   >>> a.say_hello()
   Hello

Key Notes:

* Declare a class with the ``class`` keyword

  * Convention is to use CamelCase for the name of a class
* Each non-static method has to take ``self`` as the first argument
* Instantiating a class is similar to making a function call
  ::

     variable_name = ClassName()

* Methods of a class are accessed through the dot operator
  ::

     ClassName.method_name()
     # or
     variable_name = ClassName()
     variable_name.method_name()

.. _advance_python_constructing_a_class:

Constructing a Class
^^^^^^^^^^^^^^^^^^^^
Like Java, Python provides a default constructor for classes where one was not explicitly defined.  Here
is a class with an explicitly defined constructor:
::

   class BankAccount(object):

       def __init__(self):
	   pass

       def deposit(self):
	   return 'You deposited some cash!'

The ``__init__()`` method is the constructor.  In this case, it is the same as the default constructor
which does nothing.  Here is a more useful constructor:
::

   class BankAccount(object):

       def __init__(self):
	   self. money = 50

       def deposit(self, amount):
	   self.money += amount

When we test it out...
::

   >>> bank_account = BankAccount()
   >>> bank_account.deposit(400)
   >>> print bank_account.money
   450

Key Notes:

* Python uses the special keyword, ``__init__``, to denote the constructor of a class

  * Like usual, you need to specify ``self`` as the first argument of the constructor
* Instance variables are prefixed with ``self.`` (note the dot)

  * They are global to the entire class
  * Each instance of the class has its own copies of instance variables

.. _advance_python_expanding_the_basics:

Expanding the Basics
^^^^^^^^^^^^^^^^^^^^
Before we move on to a different topic, we will tie up some loose ends:

* Modifying instance variables directly
  ::

     >>> b = BankAccount()
     >>> print b.money
     50
     >>> b.money = 500
     >>> print b.money
     500

  * Key Things to Note:

    * Python does not have the concept of private or protected variables
    * Python prefers simplicity over the possibility that the user might do something stupid
    * Python does support basic name mangling, but it is more of a deterrence

      * Ways to control how the user might alter instance variables are beyond the scope of this guide
* Who am I?
  ::

     class BankAccount(object):

	 ...

	 def deposit(self, amount):
	     self.money += amount

  * Key Things to Note:

    * In Java, you refer to the current instance of the class with the ``this`` keyword
    * Python uses the ``self`` keyword
* Static methods
  ::

     class BankAccount(object):

	 def __init__(self):
	     self.money = 50

	 @staticmethod
	 def name():
	     print 'BankAccount'

  A static method is declared by utilizing the ``staticmethod`` decorator.  It can be called without
  creating an instance:
  ::

     >>> BankAccount.name()
     BankAccount
     >>> BankAccount().name()
     BankAccount

* Static variables/Class variables
  ::

     class BankAccount(object):

	 money = 50

	 def deposit(self, amount):
	     money += amount

  * Key Things to Note:

    * Declared without the ``self.`` prefix
    * Can be accessed without declaring an instance of the class
    * Modifying the class copy, but not the instance copy will cause the instance copy to change as well
      (as expected)
    * Not truly static, each instance of the class has its own copy

      * If you change the instance's copy, it will no longer sync up with the class copy

    ::

       >>> BankAccount.money
       50
       >>> b = BankAccount()
       >>> print b.money          # should be the same as BankAccount.money
       50
       >>> BankAccount.deposit(400)
       >>> BankAccount.money
       450
       >>> print b.money
       450
       >>> b.money = 400          # will not modify the class copy
       >>> print b.money
       400
       >>> print BankAccount.money
       450

* "toString()" method
  ::

     class BankAccount(object):

	 def __init__(self):
	     self.money = 50

	 def __repr__(self):
	     return 'BankAcccount Representation Form'

	 def __str__(self):
	     return 'BankAccount String Form'

  ::

     >>> bank_account = BankAccount()
     >>> bank_account
     BankAccount Representation Form
     >>> print bank_account
     BankAccount String Form
     >>> [BankAccount(), BankAccount()]
     ['BankAccount Representation Form', 'BankAccount Representation Form']
     >>> print [BankAccount(), BankAccount()]
     ['BankAccount Representation Form', 'BankAccount Representation Form']

  * Key Things to Note:

    * Generally ``__repr__`` should be defined as a string representation of the object

      * This means ``eval(repr(object)) == object == True``
    * ``__str__`` is a user-friendly form of ``__repr__`` and therefore does not have the same
      constraints

      * Default implementation simply contains the id (memory address) and object name
    * If ``__str__`` is not found, ``__repr__`` is used
    * ``__repr__`` is used when printing a container of objects
    * ``__repr__`` corresponds to ``repr()`` and ``__str__`` corresponds to ``str()``

.. _advance_python_inheritance:

Inheritance
^^^^^^^^^^^
Now that we have covered the basics, the next step is inheritance...
::

   class DerivedClassName(BaseClassName):
       pass

Simply pass the parent class as an argument to the derived class (in the class header).  For example:
::

   class Animal(object):

       def __init__(self, name):
	   self.name = name

       def speak(self):
	   return 'idk'

   class Dog(Animal):

       pass

Let's see what we can do with this:
::

   >>> tom = Dog('tom')
   >>> tom.name
   tom
   >>> tom.speak()
   idk

Here the ``Dog`` class is inheriting both the constructor (``__init__``) and the ``speak()`` method from
``Animal``.

.. note::
   Unlike Java, Python supports multiple base classes.  Simply list them after the first base class and
   separate them with commas.  Use multiple inheritance at your own risk.

The next step is learning how to override methods:
::

   class Animal(object):

       def __init__(self, name):
	   self.name = name

       def speak(self):
	   return 'idk'

   class Dog(Animal):

       def speak(self):
	   return 'Woof!'

And the result is...
::

   >>> animal = Animal('animal')
   >>> animal.speak()
   idk
   >>> dog = Dog('dog')
   >>> dog.name
   dog
   >>> dog.speak()
   Woof!

Notice how ``dog`` says "Woof!" while ``animal`` says "idk".

The logical step after learning how to override methods is to learn how to access the overridden method.
If you are writing a class in the new style, you have access to the ``super()`` function.  Much like Java,
``super()`` refers to the parent class or the superclass.  However, the syntax is slightly different:
::

   super(SubClass, self).method_name()

Here is an example:
::

   class Animal(object):

       def __init__(self, name):
	   self.name = name

       def speak(self):
	   return 'idk'

   class Dog(Animal):

       def speak(self):

	   # In Python2, super() takes two arguments: name of subclass
	   # and the current instance
	   print super(Dog, self).speak()
	   return 'Woof!'

While *overriding* is simple in Python, **overloading** is a lot more complicated.
::

   class Animal(object):

       def __init__(self, name):
	   self.name = name

       def speak(self):
	   return '??'

   class Dog(Animal):

       def eat(self):
	   return 'Yummy!'

       def eat(self, food_name):
	   if food_name == 'dogfood':
	       return 'Yummy!'
	   else:
	       return 'Disgusting!'

Testing it out, we get...
::

   >>> tom = Dog('tom')
   >>> tom.eat('dogfood')
   Yummy!
   >>> tom.eat()
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: eat() takes exactly 2 arguments (1 given)

Key Notes:

* Override a method by implementing the same method in the child class (only the function name matters)
* If you try overloading a method, the last overloaded method implemented would override the ones you try
  to overload

We can sort of get around this with either default arguments or argument packing/unpacking:
::

   class Animal(object):

       def __init__(self, name):
	   self.name = name

       def speak(self):
	   return '??'

   class Dog(Animal):

       def eat(self, dogfood=None):
	   if not dogfood or dogfood == 'dogfood':
	       return 'Yummy!'
	   else:
	       return 'Disgusting!'

       def eat2(self, *args):
	   if not len(*args) or args[0] == 'dogfood':
	       return 'Yummy!'
	   else:
	       return 'Disgusting!'

When we test it...
::

   >>> tom = Dog('tom')
   >>> tom.eat('dogfood')
   Yummy!
   >>> tom.eat()
   Yummy!
   >>> tom.eat('halal')
   Disgusting!
   >>> tom.eat2()
   Yummy!
   >>> tom.eat2('catfood')
   Disgusting!

.. note::
   Implementation of overloaded methods using either of these workarounds are messy and should be avoided
   when possible.
