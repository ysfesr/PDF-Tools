from django.shortcuts import render
from .utils import *
import os
from django.http import FileResponse

def home(request):
    context = {}
    return render(request, 'home.html', context)

def info(request):  
    if request.method == 'POST':
        try:
            file = request.FILES['file']
        except:
            return render(request,"pdf_tools/info.html",{"results":False, "msg":True})
        context = extract_information(file)
        context['results'] = True
        return render(request, "pdf_tools/info.html", context)
    else:  
        return render(request,"pdf_tools/info.html",{"results":False, "msg":False}) 
    
def merge(request):
    if request.method == "POST":
        f_list= []
        try:
            f1 = request.FILES['file1']
            f_list.append(f1)
        except:
            pass
        try:
            f2 = request.FILES['file2']
            f_list.append(f2)
        except:
            pass
        try:
            f3 = request.FILES['file3']
            f_list.append(f3)
        except:
            pass
        try:
            f4 = request.FILES['file4']
            f_list.append(f4)
        except:
            pass
        try:
            f5 = request.FILES['file5']
            f_list.append(f5)
        except:
            pass
        
        if len(f_list) < 2:
            return render(request,'pdf_tools/merge.html', {'msg':True})
        #f4 = request.FILES['file4']
        #f5 = request.FILES['file5']
        merge_pdfs(f_list)
        response = FileResponse(open(os.path.join('media', 'merged_file.pdf'), 'rb'))
        response['content_type'] = "application/octet-stream"
        response['Content-Disposition'] = 'attachment; filename="merged_file.pdf"'

        return response
    else:
        return render(request,'pdf_tools/merge.html', {'msg':False})