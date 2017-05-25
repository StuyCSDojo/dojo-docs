Running the Flask App
=====================

* :ref:`running_app_locally`

  * :ref:`running_app_locally_activating_virtualenv`
  * :ref:`running_app_locally_running_it`
  * :ref:`running_app_locally_running_it`
* :ref:`running_app_publicly`

.. highlight:: none

.. _running_app_locally:

Locally
-------
Unlike the Python programs in Intro CS2, Flask apps can be run locally.  This is a great way of testing
your changes on a local machine before integrating them on the production server.  Since our goal is to
keep the website running without downtime, ironing out all errors before merging the changes is very
important.  So how would you do this?

.. _running_app_locally_activating_virtualenv:

Activate the Virtualenv
^^^^^^^^^^^^^^^^^^^^^^^
* Open up a terminal or command prompt and navigate into the virtualenv directory
* Run the activation script

  * On Windows, the command is: ``Scripts\activate``
  * On Unix, the command is: ``source bin/activate``

.. _running_app_locally_running_it:

Running the App
^^^^^^^^^^^^^^^
* Using the terminal, navigate to the git repo of your interest (*dojo-website*, *dojo-docs*, *dojo-resources*)
* Navigate into the app folder to find the ``api.py`` file
* Run the app via the following command: ``python api.py``

.. _running_app_locally_accessing_it:

Accessing the Site
^^^^^^^^^^^^^^^^^^
* While leaving the terminal/command prompt open, open up a web browser and in the address bar, enter:
  ``127.0.0.1:5000``

  .. warning::
     As soon as you terminate the Python program, the site would stop functioning

.. _running_app_publicly:

Publicly
--------
There are two main issues with running the site locally:

1. As soon as you terminate the Python program, the site is unavailable
2. It can only be accessed on your local machine (ie ``localhost:5000``)

To resolve these issues, you need to run it on a web server with 24/7 uptime.

You will need to use a terminal emulator on Windows (ie `Git Bash </testing/private/resources/software_installation_and_tips/installation_instructions/file_transfer_utilities/installing_ssh_programs.html#installation-file-transfer-utilities-ssh-programs-installing-git-bash>`_)
or a terminal on UNIX system for these commands:
::

   $ ssh <username>@dojo.stuycs.org
   $ cd /projects/dojo-website/app
   $ source ../../dojo/bin/activate      // Activate the virtualenv
   $ ./start_server.sh
