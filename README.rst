Dojo Documentation
==================

* `What is Here?`_
* `RST Convention`_
* `Running the Flask App`_
* `Serving it on the Droplet`_

What is Here?
-------------
This repository contains the files for the Dojo Website documentation.  There are three directories:

* **app/**

  * Contains the standalone Flask app for accessing the documentation (mainly used to test locally)
* **docs/**

  * Contains the rst source files and the corresponding html version

RST Convention
--------------
Please adhere to the following rules:

* Use "=" for title documents, "-" for title of sections, and "^" for title of subsections
* Use the |br| custom directives to move text to the next line
* Insert a newline when you want an actual line break
* For all sections, use the following format for labels:
  ::

     <name_of_file_without_extension>_<section_description>

  Example: ``flask_introduction_flask_layout``

Basic Structure:
::

   .. Custom directives goes here

   .. Title of the document goes here, underlined with "="

   .. The author's name and the date in italics

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

   *Written by <author name> on <year-month-day>*

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

Running the Flask App
---------------------
There are two parts to running the Flask app:

1. Virtualenv

   a. Activating a previously prepared virtualenv (prepared with the instructions in part b)
      ::

	 $ cd /path/to/virtualenv
	 $ source <virtualenv>/bin/activate

   b. Preparing the virtualenv
      ::

	 $ virtualenv <name>
	 $ source <name>/bin/activate
	 $ cd /path/to/dojo-docs
	 $ pip install -r dojo-docs/app/requirements.txt

2. Flask App
   ::

      $ cd /path/to/dojo-docs
      $ cd dojo-docs/app
      $ python api.py

Serving it on the Droplet
-------------------------
To run it on the server, follow the following steps:
::

   $ source /projects/dojo/bin/activate
   $ cd /projects/dojo-docs/app
   $ ./start_server.sh
