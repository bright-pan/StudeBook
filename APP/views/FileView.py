import json

#StudeBook
from APP.views.MainView import MainView
from django.http import HttpResponseRedirect
from django.http import HttpResponse

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
            fileRatings = FileRating.objects.filter(file=file)
            numberOfRatings = fileRatings.count()
            avgRating = self.getAverageFileRating(id);

        except FileRating.DoesNotExist:
            numberOfRatings = 0
            avgRating = 0

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

    def addRating (self, request) :
        file_id = request.POST.get('fileId', False)

        file = File.objects.get(file_id = file_id)

        ratingExists = FileRating.objects.filter(user = super(FileView, self).getUserLogin(request).user, file = file).count()
        if ratingExists == 0:
            fr = FileRating(user = super(FileView, self).getUserLogin(request).user, file = file, rating = request.POST['rating'])
            fr.save();

            avgRating = self.getAverageFileRating(file_id)
            numberOfRatings = FileRating.objects.filter(file=file).count()

            return HttpResponse(json.dumps({ 'status' : 200, 'avgRating' : avgRating, 'numberOfRatings' : numberOfRatings }), content_type = 'application/json');
        else:
            return HttpResponse(json.dumps({ 'status' : 500 }), content_type = 'application/json');

    def getAverageFileRating (self, id) :
        file = File.objects.get(file_id = id)

        avgRatings = FileRating.objects.values('file').filter(file=file).annotate(avg=Avg('rating'))   
        for r in avgRatings:
            a = r

        try:
            a
        except NameError:
            avgRating = 0
        else:
            avgRating = round(a["avg"])
        
        return avgRating;
