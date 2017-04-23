Introduction to Flask
=====================

* :ref:`flask_introduction_flask_layout`
* :ref:`flask_introduction_basic_flask`
* :ref:`flask_introduction_flask_routes`
* :ref:`flask_introduction_flask_templates`
* :ref:`flask_introduction_flask_advance_routes`
* :ref:`flask_introduction_flask_blueprints`
  
.. highlight:: none
  
.. _flask_introduction_flask_layout:

Flask Layout
------------
The standard Flask app directory tree looks something like:
::

   Parent Directory/
   |___ app.py        // this Python file contains the code for running your app; may
   |                  // be renamed to something else
   |
   |___ templates     // has to be named 'templates'; place all your html files here
   |
   |___ static        // only the 'static' directory is open for public access; store
   |                  // all your js, css, images, and etc here
   |
   |___ utils/        // named 'utils' by convention; place all your other Python code here
   |
   |___ data/         // named 'data' by convention; place all your data files here

.. highlight:: python   

.. _flask_introduction_basic_flask:
	       
Basic Flask
-----------
Let us start with a basic Flask app:
::

   # Import the Flask class from the flask module
   from flask import Flask

   # Bind an instance of the Flask class to 'app'.  The first argument is name of
   # the module allowing Flask to find your templates, static files, and etc.
   # Note: 'app' is the name used by convention, but may differ
   app = Flask(__name__)

   # The route decorator is used to tell Flask what URL should run the function
   # The '/' denotes root and is the page that is loaded by default (aka the home page)
   @app.route('/')
   def home():                    # Standard function definition, name need not match the route
       return 'Hello World!'      # Return text that would be rendered in the browser

   # If the program is ran directly instead of imported...
   if __name__ == '__main__':

       # Turn on debugging, enabling more specific error messages and restart the Flask
       # app upon code changes
       app.debug = True

       # Run the app
       app.run()

       # By default the host is 127.0.0.1 (localhost) and the port is 5000
       # Access the site by entering host:port (127.0.0.1:5000) into your browser

       # You may change the port or the host by giving app.run() extra parameters
       # Ex: app.run(host='192.0.0.1', port=8000) would change the address to 192.0.0.1:8000

       # Note: Ports under 1024 are restricted to those with sudo access on Unix machines
       #       port 80 is the default HTTP port
       #       port 443 is the default HTTPS port
   
.. _flask_introduction_flask_routes:

Flask Routes
------------
In Flask, the ``route()`` decorator is used to bind URL(s) to a function.  Every time you access the route
in your browser, the corresponding function is called.  The name of the function does not need to match
the route.

Here is a basic example:
::

   from flask import Flask

   app = Flask(__name__)

   @app.route('/')
   def home():
       return 'Hello World!'

In the example above, ``app`` in ``@app.route('/')`` corresponds to the name of the variable you assign
to the instance of the Flask class.  All routes should start with ``/`` which is the root.

Here is a more complex example:
::

   from flask import Flask

   @app.route('/')
   def home():
       return 'Hello World!'

   @app.route('/food/')
   def mochi():
       return 'I am very hungry!'

   @app.route('/favorites/programming/languages/')
   def language():
       return 'Python'

Note that not all pages in your routes needs to be defined.  In the example above, the ``favorites`` page
and the ``programming`` page were never defined but you can still access the ``languages`` page.

When writing your Flask app, it would be helpful to know the url that a function is bound to.  To build
the url when given the function name, use the following format:
::

   from flask import url_for

   # The name of the function should be inside quotes
   url_for('function_name')

.. _flask_introduction_flask_templates:

Flask Templates
---------------
In IntroCS2, the way you would render HTML is by printing HTML source code.  Why is this bad?

  * Does not allow for modular design; it is hard to reuse code
  * Squeeze all your HTML and Python together, creating a mess

So, how can Flask templates fix this?

  * Reuse your HTML code with inheritance
  * Separates the HTML and Python code into HTML files and Python files (usually)
  * Allows you to store Python variables and run Python functions directly in your HTML file

Sounds too good to be true?  Try it out!  Here is some sample HTML code to be placed into your templates
folder.

.. important::
   Most of your HTML files will be located in the templates folder.

.. highlight:: html
   
::

   <!DOCTYPE html>
   <html>
       <body>
           <h1>Hello World!</h1>
	   <!-- Use <strong instead of <b> and <em> instead of <i> (HTML5 standard) -->
	   <p><strong><em>This is the best web page ever!!</em></strong></p>
       </body>
   </html>

.. highlight:: python
   
In your Flask app, revise the function definition for home:
::

   # Replace the import statement at the top with the following:
   from flask import Flask, render_template

   # The '/' denotes root and is the page loaded by default
   @app.route('/')
   def home():
       # Return your html template instead of the previous 'Hello World!'
       return render_template('<name of html file>')

Run your Flask app.

.. important::
   Make sure that your virtualenv is activated when running the Flask app!

Great!  Leave your Flask app running and now let us add some excitement by throwing some Python in
there...

.. highlight:: html+jinja

::

   <!DOCTYPE html>
   <html>
       <body>
           {# This is a comment #}
	   <h1>Hello World!</h1>

	   {# Python if statements can be used if you wrapped them with {% %} #}
	   {# No colon is necessary #}
	   {% if 1 == 1 %}
	   <p><strong><em>This is the best web page ever!</em></strong></p>

	   {# You can also use elif statements #}
	   {% elif 1 == 0 %}
	   <p>This is the worst web page ever</p>

	   {# And else statements as well... #}
	   {% else %}
	   <p>This is an OK web page...</p>

	   {# Make sure to close your conditionals with this one line #}
	   {% endif %}

	   {# You can use Python for loops! #}
	   {% for i in range(100) %}
	   <p>I am the coolest person ever!</p>

	   {# You can access the variables by surrounding the expression or variable with {{ }} #}
	   <p> {{ i ** 2 }} </p>

	   {# Close for loops with the following line #}
	   {% endfor %}

	   {# Do you think you can use while loops?  What would it look like? #}
       </body>
   </html>

.. highlight:: python
   
Simply refresh the page to see the changes.

.. warning::
   The Python subset in HTML templates is really limited since we do not really want to combine the two in
   one file.  The main goal is to ease repetitive tasks such as creating a large table.

.. _flask_introduction_flask_advance_routes:

Flask Advance Routes
--------------------
Next, you will be introduced to more complex routes.  It is possible to utilize portions of the route as
parameters for the function it is bound to.  Here is a basic example:
::

   from flask import Flask, render_template

   app = Flask(__name__)

   @app.route('/home/<page>')
   def home(page):
       return render_template(page)

In the example above, the ``home()`` function is taking a parameter, ``page``.  To declare that a portion
of the route is a variable, enclose it with < and >.  The content must match the name of the parameter.

.. important::
   When you declare a variable in the in the route, you need to declare that variable as a parameter in
   the function definition and vice versa.  The only exception is when you declare that parameter with a
   default value.

Let us look at a more complex example:
::

   from flask import Flask, render_template

   app = Flask(__name__)

   @app.route('/home/')
   @app.route('/home/<path:filename>')
   def home(filename='index.html'):
       return app.send_static_file(filename)

There are a couple of new concepts here.  First, it is perfectly legal to bind one function to multiple
routes.  The syntax for doing so is shown in the example above.

The order you declared the routes does not matter.  Instead routing is done by certain rules prescribed by
werkzeug.  These rules are:

1. Routes without variables are chosen before routes with variables
2. Shorter routes are preferred over longer routes

In the example above, should the user navigate to the first route, ``filename`` is not specified and so
the parameter would take on the default value.

Another new concept is ``<path:filename>``.  This special format tells Flask to treat the rest of the url
as a path; this would usually be the path for a file.  Otherwise, Flask would split the url into multiple
pieces instead of treating it as one value.

Lastly, the ``send_static_file`` instance method of the Flask class (``app``) is new to you.  This method
allows you to send static files from the static folder to the browser.  This means that ``filename`` in
the example above should be found in the static folder.

Another thing to note is the usage of ``send_static_file`` in files utilizing ``Blueprint``.  In those
files, you would use the following format instead:
::

   from flask import current_app

   current_app.send_static_file(filename)

The ``current_app`` variable in the ``flask`` module refers to the instance of the ``Flask`` class in the
currently running Flask app.

.. _flask_introduction_flask_blueprints:

Flask Blueprints
----------------
In Software Development, you will generally see all the routes in one file, but this reduces modularity.
To avoid this issue, we will use blueprints.

Here is a basic blueprint example:
::

   # You need to import Blueprint from the flask module
   from flask import Blueprint, render_template

   # Bind an instance of the Blueprint class to private_views
   private_views = Blueprint('private_views', __name__)

   @private_views.route('/private/resources')
   def show_resources():
       render_template('index.html')

Make sure to import the ``Blueprint`` class from the ``flask`` module.

After your import statements, you would need to declare an instance of the ``Blueprint`` class and bind it
to a variable.  The ``Blueprint`` class takes two parameters: the name of the blueprint and the
``import_name``.  The ``import_name`` would just be ``__name__``.  For our work, the name of the
``Blueprint`` instance should match the first parameter.

.. note::
   We are assuming that the name of the variable you bound the ``Flask`` instance to is ``app``.

When binding a function to a route, use the name you bound the instance of ``Blueprint`` to instead of
``app``.  In the example above, use ``private_views`` instead of ``app``.  Let us look at another example:
::

   from flask import Blueprint, render_template

   private_views = Blueprint('private', __name__)

   @private_views.route('/private/resources/')
   def resources():
       return 'Hello World!'

In this example, we would still use ``private_views`` instead of ``app`` because it is the name of the
instance that matters, not the name of the blueprint.  So why do we care about the name of the blueprint?

If we want to build an url using ``url_for``, we would need to use the name of the blueprint.  ``url_for``
is a function that returns the url for a given function.  For example, to get the url for the
``resources()`` function in the example above, we would write the following snippet:
::

   from flask import url_for

   # The format of the parameter is blueprint_name.function_name
   url_for('private.resources')

.. important::
   If you are inside the main Flask app, you can simply use ``url_for('function_name')``.  If you are in a
   file utilizing ``Blueprint`` you need ``url_for('blueprint_name.function_name')``.
