#!/home5/sayhell5/python/bin/python

import web

urls = ("/.*", "hello")
app = web.application(urls, globals())

class hello:
    def GET(self):
        print "we are here"
        return 'Hello, world!'

web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
if __name__ == '__main__':
    app.run()

