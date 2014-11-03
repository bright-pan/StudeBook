#StudeBook
from APP.views.MainView import MainView
from django.http import HttpResponseRedirect

#sb
from django.db.models import Avg
from APP.models.FileModel import File
from APP.models.FileRatingModel import FileRating
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

        try:
            fileRatings = FileRating.objects.get(file=file)
            numberOfRatings = fileRatings.count()
            avgRating = fileRatings.annotate(Avg('rating'))
        except FileRating.DoesNotExist:
            numberOfRatings = 555
            avgRating = 1

        file.size = round((file.size / 1024) / 1024, 2)
        file.price = file.file_category.file_price

        if file.price > 1:
            file.price = str(file.price) + " credits"
        else: 
            file.price = str(file.price) + " credit"

        


        return super(FileView, self).render(request, 'file/show.html', {
            'title'   : 'File',
            'file' : file,
            'numberOfRatings' : numberOfRatings,
            'avgRating' :   avgRating

        });    

    def create(self, request):

        if request.method == 'POST':
            form = FileForm(request.POST, request.FILES)
            if form.is_valid():
                # file is saved
                file = form.save(commit=False)
                file.user = super(FileView, self).getUserLogin(request).user
                file.size = request.FILES['path'].size
                file.save()
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



