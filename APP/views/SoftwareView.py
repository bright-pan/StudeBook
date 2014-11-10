from django.http import HttpResponseRedirect
from APP.views.MainView import MainView
from APP.models.SoftwareModel import Software
from APP.forms.SoftwareForm import SoftwareForm

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

    def create(self, request):
        form = SoftwareForm(request.POST or None)

        if form.is_valid():
            software = form.save(commit=False)
            software.user = super(SoftwareView, self).getUserLogin(request).user
            software.save()

            return HttpResponseRedirect(self.url)
        else:
            return super(SoftwareView, self).render(request, 'software/create.html', {
                'title': 'Add Software',
                'form': form
            })

    def read(self, request, software_id):
        return super(SoftwareView, self).render(request, 'software/read.html', {
            'software': Software.objects.get(software_id=software_id)
        })

    def update(self, request, software_id):
        return super(SoftwareView, self).render(request, 'software/update.html', {
            'software': Software.objects.get(software_id=software_id)
        })

    def delete(self, request, software_id):
        software = Software.objects.get(software_id=software_id)
        userLogin = super(SoftwareView, self).getUserLogin(request)

        if(software.user_id == userLogin.user.user_id):
            software.delete()
            return HttpResponseRedirect(self.url)

        return HttpResponseRedirect(self.url)
