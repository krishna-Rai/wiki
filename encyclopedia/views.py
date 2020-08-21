from django.shortcuts import render
from markdown2 import Markdown
markdowner = Markdown()
from . import util
from django.http import HttpResponseRedirect
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entryPage(request,TITLE):

    entry_md = util.get_entry(TITLE)
    html=""
    if(entry_md):
        html = markdowner.convert(entry_md)
    else:
        html = None

    return render(request,"encyclopedia/entryPage.html",{
        "title" : TITLE,
        "entry" : html
    })

def search(request):

    if(request.method == 'POST'):
        query = request.POST['q']
        if(util.get_entry(query)):
            return entryPage(request,query)
        else:
            all_entries = util.list_entries()
            matching_entries = []
            for entry in all_entries:
                print(entry)
                print(entry.find(query))
                if((entry.lower()).find(query.lower()) !=-1):
                    matching_entries.append(entry)
            return render(request,"encyclopedia/searchResults.html",{
                "query" : query,
                "matching_entries" : matching_entries 
            })

def newPage(request):
    
    if(request.method == 'POST'):
        print(request.POST['title'])
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title,content)
        return entryPage(request,title)
    return render(request,"encyclopedia/newpage.html")

def editPage(request,TITLE):


    if(request.method == 'POST'):
        print(request.POST['title'])
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title,content)
        return entryPage(request,title)
    return render(request,"encyclopedia/editPage.html",{
        "title" : TITLE,
        "content" : util.get_entry(TITLE) 
    })

def randompage(request):

    entry_list = util.list_entries()
    random.shuffle(entry_list)
    rand_entry = entry_list[0]
    return entryPage(request,rand_entry)
