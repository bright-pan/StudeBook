from django.http import HttpResponseRedirect
from APP.views.MainView import MainView
from APP.models.SoftwareModel import Software

"""
 @class SoftwareView
 @version 0.1
 @author StudeBook inc.
"""


class SoftwareView(MainView):
    url = '/software/'

    def index(self, request):
        return super(SoftwareView, self).render(request, 'software/index.html', {
            'title': 'Software',
            'software_list': Software.objects.all()
        })

    def create(self, request, softwareID):
        return super(SoftwareView, self).render(request, 'software/read.html', {
            'software': Software.objects.get(software_id=softwareID)
        })

    def read(self, request, softwareID):
        return super(SoftwareView, self).render(request, 'software/read.html', {
            'software': Software.objects.get(software_id=softwareID)
        })

    def update(self, request, softwareID):
        return super(SoftwareView, self).render(request, 'software/read.html', {
            'software': Software.objects.get(software_id=softwareID)
        })

    def delete(self, request, softwareID):
        software = Software.objects.get(software_id=softwareID)
        userLogin = super(SoftwareView, self).getUserLogin(request)

        if(software.user_id == userLogin.user.user_id):
            software.delete()
            return HttpResponseRedirect(self.url)

        return HttpResponseRedirect(self.url)
