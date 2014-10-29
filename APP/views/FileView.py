#StudeBook
from APP.views.MainView import MainView
from django.http import HttpResponseRedirect

#sb
from APP.models.FileModel import File
from APP.forms.FileForm import FileForm

"""
 ### StudeBook Files page ### 
 @class FileView
 @version 0.1
 @author StudeBook inc.
"""

class FileView (MainView):

    def index (self, request) :
        
    	files = File.objects.all().order_by('name');

        return super(FileView, self).render(request, 'file/index.html', {
            'title'   : 'All Files',
            'message' : 'Table of all files',
            'file_list' : files

        });

    def show (self, request, id) :
        
    	file = File.objects.get(file_id = id)

        return super(FileView, self).render(request, 'file/show.html', {
            'title'   : 'File',
            'message' : 'Table of all files',
            'file' : file

        });    

    def create(self, request):

        if request.method == 'POST':
            form = FileForm(request.POST, request.FILES)
            if form.is_valid():
                # file is saved
                form.user = super(FileView, self).getUserLogin(request).user
                form.save()
                addedFile = File.objects.latest('file_id')

                return HttpResponseRedirect('/file/show/' + str(addedFile.file_id))
            else:
                return super(FileView, self).render(request, 'file/create.html', {
            'title'   : form.errors,
            'message' : 'Create a file',
            'formset' : form
        });  
        else:
            form = FileForm()

        return super(FileView, self).render(request, 'file/create.html', {
            'title'   : 'Create file',
            'message' : 'Create a file',
            'formset' : form
        });  



