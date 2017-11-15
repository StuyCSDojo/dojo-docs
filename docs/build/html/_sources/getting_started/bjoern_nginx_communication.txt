Bjoern and Nginx Communication
==============================

* :ref:`bjoern_nginx_communication_nginx_benefits`
* :ref:`bjoern_nginx_communication_servers_communication`

  * :ref:`bjoern_nginx_communication_port_filtering`
  * :ref:`bjoern_nginx_communication_location_filtering`
  * :ref:`bjoern_nginx_communication_nginx_as_reverse_proxy`

.. highlight:: none

.. _bjoern_nginx_communication_nginx_benefits:

Benefits of Nginx
-----------------
Nginx provides many benefits over the server bundled with Flask:

* Provide the gzip module to compress data before transfer (improve performance)
* Directly serve static content (and do so faster)
* Allows easy configuration of SSL encryption
* Caches frequently accessed files (useful for resources section and static content)

.. _bjoern_nginx_communication_servers_communication:

Server Communication
--------------------

.. _bjoern_nginx_communication_port_filtering:

Port Filtering
^^^^^^^^^^^^^^
Nginx only listens on the following ports:

* **Port 80** (*default HTTP port*): Users who accidentally navigate to the site under HTTP would be
  permanently redirected to use HTTPS.
* **Port 443** (*default HTTPS port*): Traffic using HTTPS would either be routed by Nginx to Bjoern or
  be handled by Nginx directly.

.. _bjoern_nginx_communication_location_filtering:

Location Filtering
^^^^^^^^^^^^^^^^^^
We have defined multiple location filters in the config file (located at ``/etc/nginx/sites-available``)

* Requests accessing static files using the route (``/static``) would be served by Nginx directly
* Requests accessing content on the public resources page (``dojo.stuycs.org/resources``) is also served
  by Nginx directly

This is because...

* No further processing is required for access to such files
* Serving files directly with Nginx is faster
* Nginx can cache files that are frequently accessed for even faster performance

.. _bjoern_nginx_communication_nginx_as_reverse_proxy:

Nginx as Reverse Proxy
^^^^^^^^^^^^^^^^^^^^^^
Aside from the routes handled the aforementioned location filters, all other traffic are passed to
Bjoern, a C WSGI server that is used instead of the server bundled in Flask for faster performance,
via a Unix socket.  Responses from Bjoern is sent back to the client via Nginx as a reverse proxy.

Key Notes:

* Nginx reduces the workload for Bjoern by handling static files
* Nginx as a reverse proxy allows responses from Bjoern to be tunneled under HTTPS for extra security
  (SSL encryption is implemented for Nginx)
* Nginx as a reverse proxy accepts the client connection on Bjoern's behalf, freeing up Gunicorn workers
  to spend more time handling requests instead of waiting for client to respond
