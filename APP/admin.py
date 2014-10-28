from django.contrib import admin
from APP.models.FileModel import File
from APP.models.UserModel import User
from APP.models.PageModel import Page

admin.site.register(User)
admin.site.register(File)
admin.site.register(Page)