#StudeBook
from APP.views.MainView import MainView

#sb
from APP.models.FileModel import File

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


