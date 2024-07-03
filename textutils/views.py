# my file
from django.http import HttpResponse 
from django.shortcuts import render


def index(request):
    return render(request,'index.html')


def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter',"off")
    purpose=''
    #Check which checkbox is on
    if removepunc == "on" :
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        djtext=analyzed   
        purpose +='-Removed Punctuations '     
        params = {'purpose':purpose, 'analyzed_text': analyzed}
       

    if fullcaps=="on" :
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        purpose +='-Changed to Uppercase '
        params = {'purpose':purpose , 'analyzed_text': analyzed}
        djtext=analyzed

    if extraspaceremover=="on":
        analyzed = ""
        try:
            for index, char in enumerate(djtext):
                if not(djtext[index] == " " and djtext [index+1]==" "):
                    analyzed = analyzed + char
        except IndexError:
            return HttpResponse("please remove spaces from the end of your text")           
        purpose +='-Extra Space remove '
        params = {'purpose': purpose, 'analyzed_text': analyzed}
        djtext=analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed = analyzed + char
        purpose += '-Removed NewLines '
        params = {'purpose': purpose, 'analyzed_text': analyzed}
        
    
    if charcounter == "on":
        analyzed = ""
        for char in djtext:
            if char != " ":
                analyzed = analyzed + char
        c=len(analyzed) 
        count=f"\n -number of character in your text is {c}"       
        purpose +='-Character count '
        params = {'purpose':purpose , 'analyzed_text': analyzed+count}
        
    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on"):
        return HttpResponse("please select an option and try again")
    
    return render(request, 'analyze.html', params)
   

