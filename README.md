Steve Koch stevekochscience@gmail.com

As of August 4, 2012, this small set of code works for "Hello world" using Apache on bluehost.com, with python web framework web.py.  I don't know what I'm doing yet, but it serves a test page successfully.  Details:

BLUEHOST

* I am using bluehost.com for my server.  I don't have full access to the Apache configuration, so I am restricted to putting .htaccess file in the local directory (in my case, $HOME/public_html/sjkode/test (my domain name is sjkode.com)).  I am not permitted to use all the commands recommended by web.py cookbook. E.g.AllowOverride, LoadModule.

* I installed the following required apps, packages (I think)
** python 2.7.2
** web.py
** Flup

RESOURCES

* [web.py cookbook](http://webpy.org/cookbook/fastcgi-apache) (Note: I think these instructions are currently for when you have your own Apache service and root privileges.
* [Django/Bluehost instructions by Pawel](http://simplyargh.blogspot.com/2012/04/python-27-django-14-on-bluehost.html) These instructions are excellent for getting Django project working on Bluehost.  Obviously, it's different for web.py, but it helped me _start_ to understand what is going on.
* [Bluehost help page for debugging Django problems](https://my.bluehost.com/cgi/help/585 Again, this is for Django, not web.py, but it helps with the 500 errors.  You can see these errors by going to error log on cPanel, and looking for your IP address, which will be highlighted in red.  It would be easier to look at this file via ssh, but I don't know how to do that yet.

BASIC IDEA (not really instructions) FOR THIS HELLO WORLD

1. ssh to bluehost and install the necessary stuff (python, pip, flup, web.py)
2. create a project directory under your root directory for your domain.  If you're only using one domain, then this will be $HOME/public_html.  Make a subdirectory test/
3. In that subdirectory, put the files that are here:
   * code.py
   * .htaccess

Try to access the page: yourdomain.com/test/ 
 
