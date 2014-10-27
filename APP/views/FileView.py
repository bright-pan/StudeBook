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

    def get (self, request) :
        
    	files = File.objects.all().order_by('name');

        return super(FileView, self).render(request, 'files.html', {
            'title'   : 'All Files',
            'message' : 'Table of all files',
            'file_list' : files

        });


