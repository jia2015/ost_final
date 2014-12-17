#!/usr/bin/python
#
# -*- coding: utf-8 -*-
# vim: set ts=4 sw=4 et sts=4 ai:

"""OpenID login page"""

# Python imports

# AppEngine Imports
from google.appengine.ext.webapp import template
from google.appengine.api import images
# Our App imports
from google.appengine.api import users
from google.appengine.ext import webapp
from questionAnswerSite.models import Pictures
import urllib
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers

providers = {
    'Google'   : 'https://www.google.com/accounts/o8/id',
    'Yahoo'    : 'yahoo.com',
    'MySpace'  : 'myspace.com',
    'AOL'      : 'aol.com',
    'MyOpenID' : 'myopenid.com'
    # add more here
}

# class MainHandler(webapp.RequestHandler):
#     def handle_openid(self, continue_url=None, openid_url=None):
#         if openid_url:
#             self.redirect(users.create_login_url(continue_url, None,
#                 openid_url))
#         else:
#             self.response.out.write(template.render(
#                 'templates/login.html', { 'google_url': users.create_login_url(federated_identity=providers.get('Google')) }))

        
#     def get(self):
#         continue_url = self.request.get('continue')
#         openid_url = self.request.get('openid_identifier')
#         self.handle_openid(continue_url, openid_url)

#     def post(self):
#         continue_url = self.request.get('continue')
#         openid_url = self.request.get('openid_identifier')
#         self.handle_openid(continue_url, openid_url)


# class MainHandler(webapp.RequestHandler):
#   def get(self):
#     upload_url = blobstore.create_upload_url('/upload/serve')
#     self.response.out.write('<html><body>')
#     self.response.out.write('<form action="%s" method="POST" enctype="multipart/form-data">' % upload_url)
#     self.response.out.write("""Upload File: <input type="file" name="file"><br> <input type="submit"
#         name="submit" value="Submit"> </form></body></html>""")

class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
  def post(self):
    user = users.get_current_user()
    if user:
        upload_files = self.get_uploads('file')  # 'file' is file upload field in the form
        blob_info = upload_files[0]
        file_title = self.request.get('title')

        a = Pictures(key_name = str(blob_info.key()))
        a.perlink = str(blob_info.key())
        a.author = str(user.email())
        a.title = file_title
        a.put()
        self.redirect('/list_all_img/')
    else:
        self.response.out.write(template.render('templates/login.html', { 'google_url': users.create_login_url(federated_identity=providers.get('Google')) }))
    
    
    #self.redirect('/upload/serve/%s' % blob_info.key())

class ServeHandler(blobstore_handlers.BlobstoreDownloadHandler):
  def get(self, resource):
    resource = str(urllib.unquote(resource))
    blob_info = blobstore.BlobInfo.get(resource)


    if blob_info:
                img = images.Image(blob_key=resource)
                img.resize(width=580, height=300)
                img.im_feeling_lucky()
                thumbnail = img.execute_transforms(output_encoding=images.JPEG)

               # print self.url
                self.response.headers['Content-Type'] = 'image/jpeg'
                self.response.out.write(thumbnail)
                return



application = webapp.WSGIApplication([
                               #('/upload/', MainHandler),
                               ('/upload/serve', UploadHandler),
                               ('/upload/serve/([^/]+)?', ServeHandler)
], debug=True)


def main():
    run_wsgi_app(application)


if __name__ == '__main__':
    main()



# #!/usr/bin/python
#
# -*- coding: utf-8 -*-
# vim: set ts=4 sw=4 et sts=4 ai:

# """OpenID login page"""

# import config
# config.setup()

# # Python imports

# # AppEngine Imports
# from google.appengine.ext import webapp
# from google.appengine.ext.webapp import template

# # Our App imports
# from google.appengine.api import users
# from google.appengine.ext import webapp
# from google.appengine.ext.webapp.util import run_wsgi_app

# class MainHandler(webapp.RequestHandler):
#     """Handles logins via AppEngine's integrated openid support."""

#     def handle_openid(self, continue_url=None, openid_url=None):
#         """If openid provided, being the dance; else return the login form."""
#         if openid_url:
#             self.redirect(users.create_login_url(continue_url, None,
#                 openid_url))
#         else:
#             self.response.out.write(template.render(
#                 'templates/login.html', {'continue': continue_url}))

#     def get(self):
#         """Serve the login form."""
#         continue_url = self.request.get('continue')
#         openid_url = self.request.get('openid_identifier')
#         self.handle_openid(continue_url, openid_url)

#     def post(self):
#         """Should have an endpoint now; start the dance"""
#         continue_url = self.request.get('continue')
#         openid_url = self.request.get('openid_identifier')
#         self.handle_openid(continue_url, openid_url)

# application = webapp.WSGIApplication([
#     ('.*', MainHandler),
# ], debug=True)

# def main():
#     run_wsgi_app(application)

# if __name__ == '__main__':
#     main()
