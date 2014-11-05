import json

#StudeBook
from APP.views.MainView import MainView
from django.http import HttpResponseRedirect
from django.http import HttpResponse

#sb
from django.db.models import Avg
from APP.models.FileModel import File
from APP.models.FileRatingModel import FileRating
from APP.models.FileCategoryModel import FileCategory
from APP.forms.FileForm import FileForm

"""
 ### StudeBook Files page ### 
 @class FileView
 @version 0.1
 @author StudeBook inc.
"""

class FileView (MainView):

    def index (self, request, categoryId) :
        
        fileCategory = FileCategory.objects.get(file_category_id = categoryId)
    	files = File.objects.filter(file_category = fileCategory).order_by('-upload_date');

        for index in range(0, len(files)):
            files[index].rating = FileRating.getAverage(files[index]);
            files[index].numberOfRatings = FileRating.getNumberOfRatings(files[index]); 

        return super(FileView, self).render(request, 'file/index.html', {
            'title'   : 'File overview',
            'category' : fileCategory.category,
            'file_list' : files            

        });

    def show (self, request, id) :
        
    	file = File.objects.get(file_id = id)

        numberOfRatings = FileRating.getNumberOfRatings(file)
        avgRating = FileRating.getAverage(file)
        ratedByUser = FileRating.fileRatedByUser(file, super(FileView, self).getUserLogin(request).user)

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
            'avgRating' :   avgRating,
            'ratedByUser' : ratedByUser 
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
            'title'   : 'File upload failed',
            'formset' : form
        });  
        else:
            form = FileForm()

        return super(FileView, self).render(request, 'file/create.html', {
            'title'   : 'Upload new file',
            'formset' : form
        });  

    def addRating (self, request) :
        file_id = request.POST.get('fileId', False)

        file = File.objects.get(file_id = file_id)
        
        if FileRating.fileRatedByUser(file, super(FileView, self).getUserLogin(request).user) == False:
            fr = FileRating(user = super(FileView, self).getUserLogin(request).user, file = file, rating = request.POST['rating'])
            fr.save();

            avgRating = FileRating.getAverage(file)
            numberOfRatings = FileRating.getNumberOfRatings(file)

            return HttpResponse(json.dumps({ 'status' : 200, 'avgRating' : avgRating, 'numberOfRatings' : numberOfRatings }), content_type = 'application/json');
        else:
            return HttpResponse(json.dumps({ 'status' : 500 }), content_type = 'application/json');

