# Django
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# App
from APP.views.MainView import MainView
from APP.models.SoftwareModel import Software
from APP.forms.SoftwareForm import SoftwareForm

"""
 @class SoftwareView
 @version 1.0
 @author StudeBook inc.
"""


class SoftwareView(MainView):

    def index(self, request, page=1):
        software = Software.objects.all()
        paginator = Paginator(software, 10)

        try:
            software = paginator.page(page)
        except PageNotAnInteger:
            software = paginator.page(1)
        except EmptyPage:
            software = paginator.page(paginator.num_pages)

        pagination_range = [i+1 for i in range(software.paginator.num_pages)]

        return super(SoftwareView, self).render(request, 'software/index.html', {
            'title': 'Software',
            'software_list': software,
            'pagination_range': pagination_range
        })

    def create(self, request):
        form = SoftwareForm(request.POST or None)

        if form.is_valid():
            software = form.save(commit=False)
            software.user = super(SoftwareView, self).getUserLogin(request).user
            software.save()

            return HttpResponseRedirect('/software/')
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
        instance = Software.objects.get(software_id=software_id)
        form = SoftwareForm(request.POST or None, instance=instance)

        if form.is_valid():
            software = form.save(commit=False)
            software.save()

            return HttpResponseRedirect('/software/')
        else:
            return super(SoftwareView, self).render(request, 'software/update.html', {
                'title': 'Edit Software',
                'form': form
            })

    def delete(self, request, software_id):
        software = Software.objects.get(software_id=software_id)
        user_login = super(SoftwareView, self).getUserLogin(request)

        if(software.user_id == user_login.user.user_id):
            software.delete()
            return HttpResponseRedirect(software)

        return HttpResponseRedirect('/software/')
