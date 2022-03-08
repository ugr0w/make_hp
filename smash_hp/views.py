from django.shortcuts import render


import sys
# Create your views here.
import zipfile
import urllib.parse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import os
from fastapi import FastAPI, File, UploadFile
from django.http import FileResponse

def fprint(val,p_f=False):
    if p_f:
        print(val)
        return val
    else:
        return val

@login_required
def smash(request):
    print("a")
    return render(request, 'index.html')

#@login_required
def smash_charas(request):
    print("b")
    return render(request, 'sumabura.html')

@login_required
def push_image(request):
    print("c")
    #file_path_1 = '/home/tmptmp/test.zip'
    file_path_1 = '/home/tmptmp/キャプチャ.zip'
    file_path_2 = '/home/tmptmp/ubuntu-20.04.3-desktop-amd64.iso_bk'
    
    print("file_path_1",sys.getsizeof(file_path_1))
    print("file_path_2",sys.getsizeof(file_path_2))
    
    response = FileResponse(open(file_path_1, 'rb'))
    os.remove(file_path_1)
    response.encodeing = "utf8"
    response['content_type'] = 'application/zip'
    response['charset'] = "utf8"
    #response['Content-Disposition'] = 'attachment; filename={}'.format("キャプチャ.zip")
    #response['Content-Disposition'] = "attachment; filename='{}'; filename*=UTF-8''{}".format("キャプチャ.zip", "キャプチャ.zip")
    response['Content-Disposition'] = 'attachment; filename={}'.format(urllib.parse.quote("キャプチャ.zip"))

    print("$$$$$$$$$$$$$$$$$$$")
    return response
