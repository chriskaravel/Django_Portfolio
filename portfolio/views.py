import zipfile
from django.http import HttpResponse
from .models import Script
from django.shortcuts import render
import requests

def portfolio_view(request,*args,**kwargs):
    scripts = Script.objects.all()
    database_data = []
    for script in scripts:
        data = {
            'name' : script.name,
            'description' :script.description,
        }
        database_data.append(data)
        print(database_data)
    context = {'database_data' : database_data}
    return render(request,"portfolio.html",context)



README_NAME = 'README.md'
README_CONTENT = """
Keep calm and code in Python!
"""
def download_file(request,name):
    ZIPFILE_NAME = name+'.zip'
    """Download archive zip file of code snippets"""
    response = HttpResponse(content_type='application/zip')
    zf = zipfile.ZipFile(response, 'w')

    # create the zipfile in memory using writestr
    # add a readme
    zf.writestr(README_NAME, README_CONTENT)

    # retrieve snippets from ORM and them to zipfile
    #name ='b.py'
    scripts = Script.objects.all()
    for snippet in scripts:
        if snippet.name == name:
            zf.writestr(snippet.name, snippet.code)

    # return as zipfile
    response['Content-Disposition'] = f'attachment; filename={ZIPFILE_NAME}'
    return response