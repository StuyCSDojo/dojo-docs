Introduction to MongoDB
=======================

* :ref:`mongodb_introduction_overview`
* :ref:`mongodb_introduction_mongod_and_mongo`
* :ref:`mongodb_introduction_basic_commands`
* :ref:`mongodb_introduction_basic_database_commands`

  * :ref:`mongodb_introduction_older_versions`
  * :ref:`mongodb_introduction_newer_versions`

.. highlight:: none

.. _mongodb_introduction_overview:

Overview
--------
MongoDB is a cross-platform document-based database system that is taught in Software Development.  We
will be using it to store login credentials, announcements, and possibly forum posts.

First, let us cover some basic definitions:

.. glossary::

   Dynamic Schema
       In the context of MongoDB, documents in a collection do not need to have the same structure/fields
       as each other.

   Database
       A database is a container of collections.  Think of it as the master spreadsheet in Excel.  A
       MongoDB server typically contains multiple databases.

   Collection
       A collection is a group of MongoDB documents.  Think of it as the individual sheets in the master
       spreadsheet.

   Document
       A document is a set of key-value pairs with a dynamic schema.  Think of it as the individual rows
       of a sheet in a master spreadsheet.

   Field
       A field is a individual key-value pair.  Think of it as the individual columns of each row.

   Primary Key
       The default key _id provided by MongoDB automatically when you insert a document to distinguish
       that document from the others.

.. _mongodb_introduction_mongod_and_mongo:

Mongod and Mongo
----------------
If you have not already done so, follow the `Installing MongoDB </testing/private/resources/software_installation_and_tips/installation_instructions/programming_tools/installing_mongodb.html>`_ guide to install MongoDB.

Mongod is the service that starts up the MongoDB server.  The Mongo Shell is an interactive JavaScript
interface to MongoDB and can be accessed by running ``mongo`` in your terminal.

.. tip::
   If you get an error, make sure that the MongoDB server is running (instructions are found in the
   installation guide).

.. _mongodb_introduction_basic_commands:

Basic Commands
--------------
Next, we will introduce you to a few of the basic commands for interacting with the database.  These
commands are geared toward how to get help if you are lost.

.. note::
   Words in italics are meant to be replaced with actual names.  Ex: *collection* means insert the name of
   a collection here.

==========================  ==================================================
Commands                    Description
==========================  ==================================================
help                        Show help
db.help()                   Show help for database methods
db.\ *collection*\ .help()  Show help for collection methods
show dbs                    Show/list all databases
use dbs                     Switch to a particular database
show collections            Show/list all collections of the selected database
exit                        Exit the Mongo Shell
==========================  ==================================================

.. _mongodb_introduction_basic_database_commands:

Basic Database Commands
-----------------------
Now that you know how to get help and exit the shell, we will introduce you to commands for interacting
with the databases.  These commands will allow you to modify the database directly for finer controls if
there are no Python wrappers for the operation you wish to perform.

.. _mongodb_introduction_older_versions:

Older Versions
^^^^^^^^^^^^^^
On older versions of MongoDB (typically in school and on the droplet), you would need to use the following
commands instead:

=============================================================  ========================================
Database Commands                                              What it does
=============================================================  ========================================
db.\ *collection*\ .insert()                                   Insert a document into the collection
db.\ *collection*\ .update()                                   Update first occurence in the collection
db.\ *collection*\ .update(*filter*, *update*, {multi: true})  Update all occurences in the collection
db.\ *collection*\ .remove()                                   Delete all documents in the collection
db.\ *collection*\ .remove(*filter*, 1)                        Delete first occurence in the collection
db.\ *collection*\ .remove(*filter*)                           Delete all occurences in the collection
=============================================================  ========================================

.. tip::
   *filter* and *update* are discussed below.

.. _mongodb_introduction_newer_versions:

Newer Versions
^^^^^^^^^^^^^^
==================================================  =====================================================
Database Commands                                   What it does
==================================================  =====================================================
db.\ *collection*\ .find()                          Display all data in that collection
db.\ *collection*\ .find(*filter*)                  Display all data matching the search query
db.\ *collection*\ .insertOne(*filter*)             Insert a document into the collection
db.\ *collection*\ .insertMany(*filter*)            Insert multiple documents into the collection at once
db.\ *collection*\ .updateOne(*filter*, *update*)   Update first occurence in the collection
db.\ *collection*\ .updateMany(*filter*, *update*)  Update all occurences in the collection
db.\ *collection*\ .deleteOne(*filter*)             Delete the first occurence in the collection
db.\ *collection*\ .deleteMany(*filter*)            Delete all occurences in the collection
db.\ *collection*\ .drop()                          Remove the entire collection
==================================================  =====================================================

*filter* is a dictionary of key-value pairs (basically a Python dictionary).  The dictionary will be used
to narrow the focus of the command to specific documents/fields.

*update* can just be a dictionary, in which case it will replace any matches of *filter* in the
collection.  For example:
::

   db.collection.update({'name': 'hello'}, {'first_name', 'bye'})

   // Replace the first key-value pair with the second key-value pair

*update* allows for greater control of how you modify the database should you decide to use it with the
update operators.  Here is an example:
::

   db.collection.update({'name': 'hello'}, { $set: {'first_name': 'bye'}})
   // Add the key-value pair {'first_name': 'bye'}

Here are a few of the update operators and what they do:

===============  ===========================================
Update Operator  Description
===============  ===========================================
$rename          Renames a field
$set             Sets the value of a field in the document
$unset           Removes the specified field in the document
===============  ===========================================
