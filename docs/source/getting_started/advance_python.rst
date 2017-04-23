Advance Python
==============

* :ref:`advance_python_default_arguments`
* :ref:`advance_python_string_formatting`
* :ref:`advance_python_list_comprehension`
* :ref:`advance_python_decorators`

  * :ref:`advance_python_decorators_components`
  * :ref:`advance_python_basic_decorators`
  * :ref:`advance_python_order_of_decorators`
  * :ref:`advance_python_decorators_with_arguments`
  * :ref:`advance_python_debugging_decorators`
* :ref:`advance_python_classes`

.. _advance_python_default_arguments:

Default Arguments
-----------------
In Python, it is possible to write functions that have optional parameters with default values.  The
syntax is pretty straightforward:
::

   def func_name(arg=value, arg2=value2):
       # rest of function definition

Simply add an equal sign followed by the default value after the parameter the way you would normally
define that variable.  Here is a more concrete example:
::

   def hello(name='bob'):
       return 'Hello ' + name + '!'

   print hello()           # Outputs: Hello bob!
   print hello('World')    # Outputs: Hello World!

In the definition of ``hello()`` above, if you don't provide a value for ``name``, the function would
simply assign to ``name`` the value of 'bob'.  If you do provide a value, that value would overwrite the
default value.

.. important::
   Any parameters with default values must be listed after all the parameters without default values.

Therefore, the following definition is not valid:
::

   def func_name(arg=value, arg2, arg3=value2):
       # rest of function declaration

On a slight digression, if you are not sure what is the order of the parameters, but you know which
parameters you need to enter...
::

   def hello(lastname, firstname):
       return 'Hello ' + firstname + ' ' + lastname + '!'
   
   hello(firstname='bob', lastname='gates')

Using a similar syntax to declaring parameters with default values, it is possible to provide the
arguments in a different order than it was defined without generating an error.

.. _advance_python_string_formatting:

String Formatting
-----------------

.. _advance_python_list_comprehension:

List Comprehension
------------------
*List Comprehension* in Python allows you to construct lists in a easy and natural manner.  For example,
if you want a list ranging from 0 to 9 inclusive, the way you learn to do it was:
::

   l = []
   for i in xrange(10):
       l.append(i)

The ``xrange()`` function might be unfamiliar to you, but it is just a more memory efficient ``range()``.
``xrange()`` takes the same parameters as ``range()`` and in the example above, we are generating a
sequence that would run from 0 to 9.

However, the aforementioned problem can also be solved with the following snippet:
::

   l = [i for i in xrange(10)]

While difficult to read at first, you will find it pretty intuitive with some practice.  Let us go over
each component...

When you write ``for i in xrange(10)``, you are declaring the variable ``i`` which will take on the values
from 0 to 9 inclusive with each iteration of the loop.  The ``i`` between that snippet and ``[`` is the
*output expression*.  The result of the *output expression* would become a member of the new list in the
order in which it was generated.

We can also utilize a slightly more complex form:
::

   l = [i ** 2 for i in xrange(10) if i % 2 == 0]
   print l

In the above example, we are squaring the variable ``i`` and adding it to the list only if the expression
``i % 2 == 0`` is true.  Thus, the above example would evaluate to ``[0, 4, 16, 36, 64]``.

.. note::
   Any one line expression with valid syntax can be used for the *output expression*.  This does not
   include statements such as ``if``, ``return``, ``print``, etc.

.. _advance_python_decorators:

Python Decorators
-----------------
Python decorators allows the programmer to dynamically alter the functionality of a function, method, or
class without having to modify the original behavior of the code.  A couple of things to note before we
cover decorators:

.. _advance_python_decorators_components:

Components of Decorators
^^^^^^^^^^^^^^^^^^^^^^^^
1. Binding functions to variables
   ::

      def hello(name):
          return 'hello'

      say_hello = hello
      print say_hello()      # Outputs: hello
      print hello()          # Outputs: hello

2. Defining functions inside other functions
   ::

      def greet_someone(name):
          def retrieve_greeting():
	      return 'Hello, '

	  result = retrieve_greeting() + name
	  return result

3. Treating a function as a parameter to other functions
   ::

      def hello(name):
          return 'Hello, ' + name

      def greet_someone(func, name):
          return func(name)

      print greet_someone(hello, 'bob')    # Outputs: Hello, bob

4. Returning functions within a function
   ::

      def get_greeting():
          def greeting():
	      return 'Hello there!'

	  return greeting

      print get_greeting()    # Outputs: Hello there!

5. Closure: accessing variables/functions in the enclosing scope from an inner function
   ::

      def get_greeting(name):
          def greeting():
	      return 'Hello there, ' + name + '!'

	  return greeting

      print get_greeting('bob')    # Outputs: Hello there, bob!

   In the example above, the inner function, ``greeting()``, is able to access the ``name`` variable which
   lies in the scope/definition of the outer function.

.. note::
   Python only allows **read access to the outer scope/definition**.  You may not modify those variables.

.. _advance_python_basic_decorators:
   
Basic Decorators
^^^^^^^^^^^^^^^^
Now that you have been introduced to all the components of a decorator, here is an example of a basic
decorator:
::

   def get_message():
       return 'Lorem ipsum, bacon ipsum dolor amet chicken turducken salami'

   # Decorator function
   def add_p_tags(func):
       def func_wrapper():
           return '<p>{0}</p>'.format(func())
       return func_wrapper

   decorated_with_p_tags = add_p_tags(get_message)
   print decorated_with_p_tags()
   # Outputs: <p>Lorem ipsum, bacon ipsum dolor amet chicken turducken salami</p>

Remember, a decorator is simply a function that wraps around another function to augment the work of the
original function by generating a new function and returning that function so we can use it anywhere.

However, the decorator as used above is really messy.  Here is an alternative and cleaner method:
::

   def add_p_tags(func):
       def func_wrapper():
           return '<p>{0}</p>'.format(func())
       return func_wrapper

   @add_p_tags
   def message(name):
       return 'bacon ipsum, {0} dolor amet chicken turducken salami'.format(name)

   print message('bob')
   # Outputs: bacon ipsum, bob dolor amet chicken turducken salami

Simply insert an '@' symbol followed by the name of the decorator function before the function to be
decorated.  Now, let us experiment with the ordering of the decorators.

.. _advance_python_order_of_decorators:

Order of Decorators
^^^^^^^^^^^^^^^^^^^
In general, Python decorators are evaluated from the bottom to the top.  If we were to have the following
definition:
::

   @add_strong_tags
   @add_p_tags
   @add_div_tags
   def text():
       return 'bacon ipsum'

   print text()
       
First, the ``add_div_tags`` decorator would be applied, then the ``add_p_tags`` decorator, and finally the
``add_strong_tags`` decorator.  Therefore, running the last statement in the example above would give you:
``<strong><p><div>bacon ipsum</div></p></strong>``.  If we were to switch the order to:
::

   @add_div_tags
   @add_p_tags
   @add_strong_tags
   def text():
       return 'bacon ipsum'

   print text()

The order of the decorators have been reversed, so the resulting output is now:
``<div><p><strong>bacon ipsum</strong></p></div>``.

.. _advance_python_decorators_with_arguments:

Passing Arguments to Decorators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
It will be useful to know how to pass arguments to decorators so that we will not need to write a
different decorator for each tag.  To do this, we need to write a function that takes as many parameters
as we need and generates a decorator on the fly.  Here's the basic syntax:
::

   def decorator_generator(arg, arg1, arg2, argn):
       def actual_decorator(func):
           def inner_function():
	       # do something in the inner function
	   return inner_function
       return actual_decorator

Here's how you will use it:
::

   @decorator_generator(arg, arg1, arg2, argn)
   def function_to_be_decorated():
       # do something inside the function

Instead of using the name of the actual decorator, we use the name of the decorator generator and pass to
it the arguments it needs.  Then, it generates the actual decorator which wraps around
``function_to_be_decorated()``.  ``actual_decorator()`` is written in the same manner as the basic
decorator you were introduced to before.

.. _advance_python_debugging_decorators:

Debugging Decorators
^^^^^^^^^^^^^^^^^^^^
When debugging decorators, you might find it problematic if you don't have access to the name of the
function, the name of the module, or the docstring.  This is because the attributes ``__name__``,
``__module__``, and ``__doc__`` are overridden by those of the wrapper (ie ``func_wrapper``).  To access
the original, we need to import the ``wraps()`` method from the ``functools`` module.  Here is an example:
::

   def tags(tag_name):
       def tags_decorator(func):
           @wraps(func)
	   def func_wrapper():
	       return '<{0}>{1}</{0}>'.format(tag_name, func())
	   return func_wrapper
       return tags_decorator

   @tags('p')
   def get_text():
       '''return some text'''
       return 'hello'

   print get_text.__name__    # Outputs: get_text
   print get_text.__module__  # Outputs: __main__
   print get_text.__doc__     # Outputs: return some text

By adding the line, ``@wraps(func)`` to the definition of the decorator in the example above, we were able
to access the original attributes (those of the function being wrapped around).

.. _advance_python_classes:

Python Classes
--------------
