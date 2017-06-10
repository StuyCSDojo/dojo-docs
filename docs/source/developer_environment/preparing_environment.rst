Preparing the Developer Environment
===================================

* :ref:`preparing_environment_windows`

  * :ref:`preparing_environment_windows_installing_git`
  * :ref:`preparing_environment_windows_installing_python`
  * :ref:`preparing_environment_windows_installing_mongodb`
  * :ref:`preparing_environment_windows_installing_virtualenv`
  * :ref:`preparing_environment_windows_installing_dependencies`
* :ref:`preparing_environment_unix`

  * :ref:`preparing_environment_unix_installing_git`
  * :ref:`preparing_environment_unix_installing_python`
  * :ref:`preparing_environment_unix_installing_mongodb`
  * :ref:`preparing_environment_unix_installing_virtualenv`
  * :ref:`preparing_environment_unix_installing_dependencies`
* :ref:`preparing_environment_school_linux`

  * :ref:`preparing_environment_school_linux_cloning_repos`
  * :ref:`preparing_environment_school_linux_creating_virtualenv`
  * :ref:`preparing_environment_school_linux_installing_dependencies`

.. highlight:: none

.. _preparing_environment_windows:

Windows
-------
.. note::
   ``C:\Users\Username>`` signals that you should enter the commands afterward in the command prompt.

.. _preparing_environment_windows_installing_git:

Install Git and Clone Repos
^^^^^^^^^^^^^^^^^^^^^^^^^^^
* If you do not have Git installed, check the
  `Installing Git </testing/private/resources/software_installation_and_tips/installation_instructions/programming_tools/installing_git.html#windows>`_ guide for instructions
* For a brief introduction to Git, check the
  `Introduction to Git </testing/private/resources/software_installation_and_tips/software_tutorials/programming_tools/git_tutorial.html>`_ guide
* It is also recommended to set up SSH keys, information can be found in the
  `SSH Keys </testing/private/resources/software_installation_and_tips/software_tutorials/remote_file_transfer/ssh_keys_tutorial.html>`_ guide
* Create a folder for the project and clone the Dojo Website repos inside that directory by running the
  following commands in Powershell or command prompt:
  ::

     C:\Users\Username> mkdir <name of directory>
     C:\Users\Username> cd <name of directory>
     C:\Users\Username> git clone git@github.com:StuyCSDojo/dojo-website.git
     C:\Users\Username> git clone git@github.com:StuyCSDojo/dojo-docs.git
     C:\Users\Username> git clone git@github.com:StuyCSDojo/dojo-resources.git

.. _preparing_environment_windows_installing_python:

Install Python and Configure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* If you do not have Python installed or your version is not at least 2.7.9, follow the instructions
  `here </testing/private/resources/software_installation_and_tips/installation_instructions/programming_languages/installing_python.html#windows>`_ (uninstall the old version if necessary)
* At this point, if you are still using a previous installation, make sure that Python and Pip are on your
  path.  To check, run the following commands:
  ::

     C:\Users\Username> python --version
     C:\Users\Username> pip --version

  If the first command gave you an error, add ``C:\Python27`` to your path.  If the second command gave
  you an error, add ``C:\Python27\Scripts``.

  .. tip::
     Not sure how to add a directory to your path?  Read the `Modifying Windows Path guide </testing/private/resources/software_installation_and_tips/software_tutorials/system/modifying_windows_path_tutorial.html>`_.

.. _preparing_environment_windows_installing_mongodb:

Download and Configure MongoDB
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
MongoDB is one of the databases that you will learn in Software Development.  We are using it to store
user credentials along with the announcements on the homepage.  Check the `Installing MongoDB for Windows guide </testing/private/resources/software_installation_and_tips/installation_instructions/programming_tools/installing_mongodb.html#windows>`_ for instructions to installing it.

.. _preparing_environment_windows_installing_virtualenv:

Installing and Creating Virtualenv
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The virtualenv module:

* Allows you to create isolated python environments to install libraries without cluttering the system
* Allows you to test for compatibility with newer libraries without breaking current products

If you installed Anaconda Python, you can skip the installation step.  Otherwise, run the following
command in the command prompt or Powershell:
::

   C:\Users\Username> pip install virtualenv

In the directory where you clone the dojo-website repository, create a virtualenv.  The general syntax for
creating a virtualenv is:
::

   C:\Users\Username> virtualenv <name of virtualenv>

.. note::
   The parameter for the ``virtualenv`` command is simply a name of your choice.  The result of the
   command would be a directory.

.. _preparing_environment_windows_installing_dependencies:

Installing Dependencies
^^^^^^^^^^^^^^^^^^^^^^^
If you are using Anaconda Python, you are good to go as the dependencies are already installed!
Otherwise...

* Activate the virtualenv with the following commands:
  ::

     C:\Users\Username> cd <path\to\virtualenv\created\in\previous\step>
     C:\Users\Username> cd <name of virtualenv>
     C:\Users\Username> Scripts\activate

* Install the dependencies with the following command:
  ::

     C:\Users\Username> pip install -r ..\dojo-website\app\requirements.txt

.. note::
   The requirements.txt file contains a list of dependencies in a format readable by Pip and humans.

.. _preparing_environment_unix:

Unix
----
.. _preparing_environment_unix_installing_git:

Install Git and Clone Repos
^^^^^^^^^^^^^^^^^^^^^^^^^^^
* If you do not already have Git installed, check the `Installing Git guide </testing/private/resources/software_installation_and_tips/installation_instructions/programming_tools/installing_git.html>`_
* For a brief introduction to Git, check the `Introduction to Git guide </testing/private/resources/software_installation_and_tips/software_tutorials/programming_tools/git_tutorial.html>`_
* It is also recommended to set up SSH Keys, information can be found in the `SSH Keys guide </testing/private/resources/software_installation_and_tips/software_tutorials/remote_file_transfer/ssh_keys_tutorial.html>`_
* Create a folder for the project and clone the Dojo Website repos inside that directory by running the
  following commands in the terminal:
  ::

     $ mkdir <name of directory>
     $ cd <name of directory>
     $ git clone git@github.com:StuyCSDojo/dojo-website.git
     $ git clone git@github.com:StuyCSDojo/dojo-docs.git
     $ git clone git@github.com:StuyCSDojo/dojo-resources.git

.. _preparing_environment_unix_installing_python:

Install Python and Pip
^^^^^^^^^^^^^^^^^^^^^^
Pip is the Python package manager that we would be using to install extra Python libraries.  For
instructions on installing Pip and/or Python, check the `Installing Python and Pip guide </testing/private/resources/software_installation_and_tips/installation_instructions/programming_languages/installing_python.html>`_.

.. _preparing_environment_unix_installing_mongodb:

Install and configure MongoDB
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
MongoDB is one of the databases that you will learn in Software Development.  We are using it to store
user credentials along with the announcements on the homepage.  Check the `Installing MongoDB  guide </testing/private/resources/software_installation_and_tips/installation_instructions/programming_tools/installing_mongodb.html>`_ for instructions to installing it.

.. _preparing_environment_unix_installing_virtualenv:

Creating and Activating Virtualenv
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Why use a virtualenv?

* Allows you to create isolated python environments to install libraries without cluttering the system
* Allows you to test for compatibility with newer libraries without breaking current products
* Allows you to install packages without admin privileges

To install virtualenv, run the following command in the terminal:
::

   $ sudo pip install virtualenv

In the directory where you clone the dojo-website repository, create a virtualenv.  The general syntax for
creating a virtualenv is:
::

   $ virtualenv <name of virtualenv>

.. note::
   The parameter for the ``virtualenv`` command is a name of your choice and would result in a directory
   with that name.

.. _preparing_environment_unix_installing_dependencies:

Installing Dependencies
^^^^^^^^^^^^^^^^^^^^^^^
* Activate the virtualenv:
  ::

     $ cd /path/to/virtualenv
     $ cd <name of virtualenv>
     $ source bin/activate

* Install the dependencies via Pip:
  ::

     $ pip install -r ../dojo-website/app/requirements.txt

.. note::
   The requirements.txt file contains a list of dependencies in a format readable by Pip and humans.

.. _preparing_environment_school_linux:

School Linux
------------
The steps for preparing the developer environment on the cs lab machines are different from the standard
installation of Linux.  Most tools are already installed and the rest can be installed via a virtualenv.

.. _preparing_environment_school_linux_cloning_repos:

Cloning Repos
^^^^^^^^^^^^^
On the school machines, Git is already installed so we just need to clone the repositories.  Start by
creating a directory to store all your Dojo Website work.  Inside that directory, you will need to run
the following commands:
::

   $ git clone git@github.com:StuyCSDojo/dojo-docs.git
   $ git clone git@github.com:StuyCSDojo/dojo-resources.git
   $ git clone git@github.com:StuyCSDojo/dojo-website.git

.. note::
   If you need help regarding Git, check out the `Introduction to Git </testing/private/resources/software_installation_and_tips/software_tutorials/programming_tools/git_tutorial.html>`_ guide.  To set up the SSH
   keys, check out `SSH Keys </testing/private/resources/software_installation_and_tips/software_tutorials/remote_file_transfer/ssh_keys_tutorial.html>`_ guide.

.. _preparing_environment_school_linux_creating_virtualenv:

Creating and Activating Virtualenv
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Why use a virtualenv?

* Allows you to create isolated python environments to install libraries without cluttering the system
* Allows you to test for compatibility with newer libraries without breaking current products
* Allows you to install packages without admin privileges

We would create a virtualenv at the root of the folder where you are doing your Dojo Website work.  The
syntax for creating a virtualenv is:
::

   $ virtualenv <name of virtualenv>

.. note::
   The parameter for the ``virtualenv`` command is a name of your choice and would result in a directory
   with that name.

.. _preparing_environment_school_linux_installing_dependencies:

Installing Dependencies
^^^^^^^^^^^^^^^^^^^^^^^
* Activate the virtualenv with the following commands:
  ::

     $ cd /path/to/virtualenv
     $ cd <name of virtualenv>
     $ source bin/activate

* Install the dependencies via Pip:
  ::

     $ pip install -r ../dojo-website/app/requirements.txt

.. note::
   The requirements.txt file contains a list of dependencies in a format readable by Pip and humans.
