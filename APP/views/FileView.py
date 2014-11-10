import json
import os.path
import ntpath
import mimetypes

#StudeBook
from APP.views.MainView import MainView
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.servers.basehttp import FileWrapper
from django.utils.encoding import smart_str
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#sb
from django.db.models import Avg
from APP.models.FileModel import File
from APP.models.FileRatingModel import FileRating
from APP.models.FileCategoryModel import FileCategory
from APP.models.FileDownloadModel import FileDownload
from APP.forms.FileForm import FileForm

"""
 ### StudeBook Files page ### 
 @class FileView
 @version 0.1
 @author StudeBook inc.
"""

class FileView (MainView):

    def index (self, request, categoryId, page = 1) :
        
        fileCategory = FileCategory.objects.get(file_category_id = categoryId)
    	files = File.objects.filter(file_category = fileCategory).order_by('-upload_date');
        paginator = Paginator(files, 10);

        try:
            files = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            files = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            files = paginator.page(paginator.num_pages)

        for index in range(0, len(files)):
            files[index].rating = FileRating.getAverage(files[index]);
            files[index].numberOfRatings = FileRating.getNumberOfRatings(files[index]); 
            files[index].numberOfDownloads = FileDownload.getNumberOfDownloads(files[index]);

        paginationRange = [i+1 for i in range(files.paginator.num_pages)];

        return super(FileView, self).render(request, 'file/index.html', {
            'title'   : 'File overview',
            'category' : fileCategory,
            'file_list' : files,
            'paginationRange' : paginationRange            

        });

    def show (self, request, id) :
        
    	file = File.objects.get(file_id = id)

        numberOfRatings = FileRating.getNumberOfRatings(file)
        avgRating = FileRating.getAverage(file)
        ratedByUser = FileRating.fileRatedByUser(file, super(FileView, self).getUserLogin(request).user)
        numberOfDownloads = FileDownload.getNumberOfDownloads(file);

        file.size = round((file.size / 1024) / 1024, 2)
        file.price = file.file_category.file_price

        if file.price > 1:
            file.price = str(file.price) + " credits"
        else: 
            file.price = str(file.price) + " credit"


        return super(FileView, self).render(request, 'file/show.html', {
            'title'   : 'File',
            'file' : file,
            'numberOfDownloads' : numberOfDownloads,
            'numberOfRatings' : numberOfRatings,
            'avgRating' :   avgRating,
            'ratedByUser' : ratedByUser 
        });  

    def download (self, request, id) :
        
        file = File.objects.get(file_id = id);
        user = super(FileView, self).getUserLogin(request).user;

        if user.credits >= file.file_category.file_price:
            # Insert FileDownload and update credits (first time download)
            if FileDownload.objects.filter(file = file, user = user).count() == 0:
                fd = FileDownload(file = file, user = user);
                user.credits -= file.file_category.file_price;
                file.user.credits += file.file_category.file_price;

                fd.save();
                user.save();
                file.user.save();
              
            # Prepare file download...  
            path = file.path.url;
            wrapper = FileWrapper( open( path, "r" ) )
            content_type = mimetypes.guess_type( path )[0]

            response = HttpResponse(wrapper, content_type = content_type)
            response['Content-Length'] = os.path.getsize( path )
            response['Content-Disposition'] = 'attachment; filename=' + smart_str( ntpath.basename( path ) )

            return response
     
        else:
            return super(FileView, self).render(request, 'file/download.html', {
                'title'   : 'File download',
                'message' : 'Not enough credits.'
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

