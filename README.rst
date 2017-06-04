Dojo Documentation
==================

.. contents::

What is Here?
-------------
This repository contains the files behind the Dojo Website documentation.  There are two directories:

* **app/**

  * Contains the standalone Flask app for accessing the documentation (mainly used to test locally)
* **docs/**

  * Contains the rst source files and the corresponding html files
  * Access is given only to developers and teachers

Setting Things Up
-----------------

During Development
^^^^^^^^^^^^^^^^^^
This repository contains a standalone Flask app that is used to test your changes before pushing them to
upstream.  Before modifying files in this repo, you should prepare the developer environment as per the
instructions found at `Dojo Documentation <https://dojo.stuycs.org/docs>`_.

Before running the Flask app, make sure you:

* Activate the virtualenv

  .. code-block:: bash

     $ cd path/to/virtualenv
     $ cd virtualenv
     $ source bin/activate

* Install and start up Mongod, instructions can be found `here <https://dojo.stuycs.org/resources/software_installation_and_tips/installation_instructions/programming_tools/installing_mongodb.html>`_.

Run the Flask app by:

.. code-block:: bash

   $ cd path/to/dojo-docs
   $ cd dojo-docs/app
   $ python api.py

The first time you run the Flask app, make sure you:

* Register an account at <http://localhost:5000/testing/register/>
* Stop the Flask app
* Promote yourself to developer privileges

  .. code-block:: bash

     $ cd lib/security
     $ python
     >>> from AuthManager import AuthManager
     >>> auth_manager = AuthManager('dojo_website')
     >>> auth_manager.make_admin(<your username>)
     (True, 'User is now an admin!')
     >>> exit()

* Run the Flask app again

  .. code-block:: bash

     $ cd ../..
     $ python api.py

Production Server
^^^^^^^^^^^^^^^^^
On the local machine:

.. code-block:: bash

   $ cd path/to/virtualenv
   $ cd virtualenv
   $ source bin/activate
   $ cd ..
   $ mkdir testing_directory
   $ cd testing_directory
   $ git clone git@github.com:StuyCSDojo/dojo-docs
   $ cd dojo-docs/app/
   $ python api.py

**Double check that the version accessible at** http://localhost:5000 **is what you want the other developers to
see when they navigate to** http://dojo.stuycs.org/docs **.**

On the production server:

.. code-block:: bash

   $ cd /projects/
   $ source dojo/bin/activate
   $ cd dojo-website/dojo-docs
   $ git reset --hard && git pull
   $ cd ..
   $ ./start_server

**If you run** ``git pull`` **at /projects/dojo-docs, the changes will be reflected at** http://dojo.stuycs.org/testing/docs
**which is meant to serve a beta version of the documentation.**

RST Convention
--------------
Please adhere to the following rules:

* Use "=" for title documents, "-" for title of sections, and "^" for title of subsections
* Use the |br| custom directives to move text to the next line
* Insert a newline when you want an actual line break
* Unlike all the other repositories, the default highlighting language should be ``none``

  * Simulate this behavior by stating ``.. highlight:: none`` at the top of every file (below the outline)
  * Only exception is when the majority of the code block needs to be highlighted in a different language
* For all sections, use the following format for labels:
  ::

     <name_of_file_without_extension>_<section_description>

  Example: ``flask_introduction_flask_layout``

Basic Structure:
::

   .. Custom directives goes here

   .. Title of the document goes here, underlined with "="

   .. Page outline in bullet point format

   .. Section label

   .. Section title underlined with '-'

   .. (Optional) Subsection label

   .. Subsection title underlined with '^'

Example:
::

   .. |br| raw:: html

      <br />

   Example Document
   ================

   * :ref:`section_name_1`
   * :ref:`section_name_2`

     * :ref:`subsection_of_section_2_name_1`
     * :ref:`subsection_of_section_2_name_2`
     * :ref:`section_name_3`

   .. _section_name_1:

   Section Name 1
   --------------
   Text for Section 1

   .. _section_name_2:

   Section Name 2
   --------------
   Text for Section 2

   .. _subsection_of_section_2_name_1:

   Section 2 Subsection 1
   ^^^^^^^^^^^^^^^^^^^^^^
   Text for subsection of Section 2
