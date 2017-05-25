.. |br| raw:: html

   <br />

Introduction to reStructuredText
================================

* :ref:`restructuredtext_introduction_what_is_rst`
* :ref:`restructuredtext_introduction_why_use_rst`
* :ref:`restructuredtext_introduction_introduction_to_toctree`
* :ref:`restructuredtext_introduction_editing_rst_files`
* :ref:`restructuredtext_introduction_basic_rst_directives`
* :ref:`restructuredtext_introduction_building_the_source`
* :ref:`restructuredtext_introduction_fixing_the_search_bar`
* :ref:`restructuredtext_introduction_additional_links`

.. highlight:: none

.. _restructuredtext_introduction_what_is_rst:

What is reST
------------
**reStructuredText** (reST) is a readable, unobtrusive, and powerful markup syntax commonly uses to build
in-line program documentation or simple web pages.  **Sphinx** is a tool that parses and converts
reStructuredText source files into various formats such as HTML, LaTex, and manual pages.

.. _restructuredtext_introduction_why_use_rst:

Why use reST
------------
There are many advantages to using reST:

* Clean and Readable
* Extensible

  * Define your own custom roles and directives
* Powerful Facilities

  * Features extra utilities such as admonition (note, caution, danger, tip, important, and etc)
  * Allows the inclusion of footnotes very easily
  * Easy syntax highlighting for code blocks
  * And more...
* Consistent with the format produced by sphinx-apidoc which extracts documentation from Python docstring
  and writes it in reST format
* Capable of doing everything HTML can and more

Minor disadvantages:

* Not widely known
* Requires additional libraries

.. _restructuredtext_introduction_introduction_to_toctree:

Introduction to Toctree
-----------------------
A "TOC tree" is a tree of individual TOCs (Table of Contents) which is reflected on the sidenav.  When you
expand the project, make sure to insert an entry into the toctree of the index file.  Otherwise, your file
would not be accessible to the general public.
|br|
The syntax for a toctree is as follows:
::

   .. toctree::
      :maxdepth: <int>
      :caption: <string>

      entry_1
      entry_2
      entry_3

``:maxdepth:`` and ``:caption:`` are optional and controls how many levels to show and the title of the
toctree respectively.  It is important to insert a newline before specifying the entries of the toctree.
The name of each entry is the name of the file you want to include without the file extension.  The
title of the file would be rendered in place of the filename.

.. _restructuredtext_introduction_editing_rst_files:

Editing reST Files
------------------
The reST source files are located in the source directory at the root of the project folders.  Currently,
the path to the project folders are as followed:
::

   // Documentation of the Dojo Website (Repo path)
   dojo-docs/docs

   // Documentation of the Dojo Website (On the web server)
   /projects/dojo-docs/docs

   // Resource materials for the Dojo Website (Repo path)
   dojo-resources/private_resources
   dojo-resources/public_resources

   // Resource materials for the Dojo Website (On the web server)
   /projects/dojo-resources/private_resources
   /projects/dojo-resources/public_resources

When you first start out...

* Focus on the textual portion and forget about the styling
* Come up with headings and subheadings that summarize each sections/subsections
* Mentally mark or physically note the places where a code block would be appropriate
* After planning out the design, proceed to the next section for a quick run through of common reST
  directives.

.. _restructuredtext_introduction_basic_rst_directives:

Basic reST Directives
---------------------
Here you will find a list of the more commonly used reST directives [#f2]_.  Check the
:ref:`restructuredtext_introduction_additional_links` section for more directives.

* **Paragraphs**

  * Indentation is very important.  All lines of a paragraph must be on the same indentation level.
* **Headers**

  .. important::
     The punctuation character must span at least as long as the header text.

  * Use the following conventions for creating section headers:

    * For the main header, underline the header text with the "=" character
    * For the section headers, underline the header text with the "-" character
    * For the subsection headers, underline the header text with the "^" character

    We will be using the "=" character for the title of the page, the "-" for section headers, and the
    "^" character for the subsections.
* **Inline Markups**

  * One asterisk: \*text\* for emphasis (italics)
  * Two asterisks: \**text\** for strong emphasis (bold)
  * Backquotes: \``text\`` for code samples
* **Code Blocks**
  |br|
  For longer sample of code, user code blocks instead of code samples.  Here is an example:
  ::

     Some text here
     ::

	This starts the code block, make sure to leave a newline after the ::
	Anything on the same indentation level would be interpreted as part of
	the code block.

     Normal text starts here

  To change the syntax  highlighting, insert  the following directive:
  ::

     .. highlight:: <language/none>

  .. note::
     The directive changes the syntax highlighting for all code blocks after it until the next
     usage of the directive.
* **Admonitions**
  |br|
  One of the additional features offered by reST, it is useful for making a block of text as special.
  The syntax is as follow:
  ::

     .. <admonition type>::
	The text that you want to render with the admonitions.

  The following admonition types are available: attention, caution, danger, error, hint, important, note,
  tip, and warning.

  .. hint::
     This is an example of an admonition...  Use them to attract the reader's attention.

* **Links**
  |br|
  There are two forms of links:

  * External Links:

    * If all you want to display is the web address, just insert the link as is
    * Otherwise, use the following syntax for an external link: ```Text to display <link>`_``
    * Here is an example:
      ::

	 Here is an example of a `link <dojo.stuycs.org>`_ to the best site ever.
	 Check it out!

  * Internal Links:
    |br|
    Internal links have two components

    * One to describe the destination utilizing the following syntax: ``.. _<insert label>:``
    * One to describe the link to the destination utilizing the following syntax: ``:ref:`<insert label>```

    Here is an example:
    ::

       .. _link_to_section:

       Section to reference
       --------------------

       It referes to itself, see :ref:`link_to_section`


* **Images**
  |br|
  If you ever need to insert an image, use the following syntax:
  ::

     .. image:: <path/to/image>                           // the path of the image is relative to the file
	:height: length                                   // height of the image, ie 100px (this attribute is optional)
	:width: length or percentage                      // width of the image, ie 50px or 50% (this attribute is optional)
	:scale: percentage                                // scaling factor of the image, ie 50% (this attribute is optional)
	:alt: text                                        // text to show if the image is not found, ie Cool image! (this attribute is optional)
	:align: top, middle, bottom, left, center, right  // align the image, ie right (this attribute is optional)
	:target: text                                     // link the image to an url, ie https://www.google.com (this attribute is optional)

* **Custom Directives**
  |br|
  It is possible to create your own directives (possibly for inserting HTML code) with the following
  syntax:
  ::

     // Insert your custom directive code here

     .. |<name>| raw:: <language> (<language> should typically be html or latex)

	// your language code here

  Here is an example:
  ::

     .. |br| raw:: html

	<br />

     Introduction to reST
     ====================

  When you need to use the custom directive defined above, simply use ``|br|``.

.. rubric:: Footnotes

.. [#f2] A few examples were taken from `the reST primer <http://www.sphinx-doc.org/en/stable/rest.html>`_.

.. _restructuredtext_introduction_building_the_source:

Building the Source
-------------------
* If you have not done so, activate the virtualenv
* Navigate to the root of the project folder (directory with the MakeFile and make.bat)
* On Windows, run:
  ::

     C:\Users\Username> make.bat html

* On Unix, run:
  ::

     $ make html

* If the command "make" is not found, follow the `Installing Make </testing/private/resources/software_installation_and_tips/installation_instructions/programming_tools/installing_make.html>`_ guide to install it.

  Once you are able to run ``make.bat html`` or ``make html``, check to make sure that the build did not
  resulted in any warnings.  These typically appear near the middle of the output.  Aim to fix all
  warnings if possible.  Typical warnings include, but are not limited to:

  * ``WARNING: Explicit markup ends without a blank line; unexpected unindent.``: You need to insert a
    blank line before the specified line number
  * ``WARNING: Title underline too short``: You need to make sure that the row of symbols following the
    line specified is as long as the text on the line specified

  Once you have successfully build the pages, you may proceed to the next step.  Otherwise, use trial and
  error to learn what is wrong and how to fix it.

.. _restructuredtext_introduction_fixing_the_search_bar:

Fixing the Search Bar
---------------------
By default, the search bar included by Sphinx for the HTML pages uses the reST files as the source to
search through.  This causes search results to be cluttered by reST directives.  At the root of the git
repo, you will find extract_source_from_html.py inside the extra_utilities folder.

.. important::
   Only run the script after a successful build (without warnings), otherwise the script may crash due to
   nonexistent or broken HTML files.

To run the script:

* Navigate to the directory containing extract_source_from_html.py
* Depending on which sections you updated...

  * Only the resources section: ``python extract_source_from_html.py --resources``
  * Only the docs section: ``python extract_source_from_html.py --docs``
  * Both sections: ``python extract_source_from_html.py --all``

.. _restructuredtext_introduction_additional_links:

Additional Links
----------------
* For a quick reference to more reST directives, check out the `reST primer <http://www.sphinx-doc.org/en/stable/rest.html#>`_
* For a more detailed and complete list, check the documentation from `docutils <http://docutils.sourgeforge.net/docs/ref/rst/directives.html>`_

.. highlight:: python
