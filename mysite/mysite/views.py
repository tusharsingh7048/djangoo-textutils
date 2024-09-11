from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse("Hello")
    # data1 = {'name':'Tushar','rollno':21}
    return render(request,'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    check = request.POST.get('check', 'off')
    upper1= request.POST.get('upper1', 'off')
    charcount=request.POST.get('charcount','off')

    # Check if the checkbox for removing punctuation is checked
    if check == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'removed punctuations', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext=analyzed
    if(upper1 == "on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'uppercase', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext=analyzed
    if(charcount=='on'):
        analyzedd=""
        count=0
        for char in djtext:
            count=count+1
            analyzedd=count
        params = {'purpose': 'counting', 'analyzedtext': analyzedd}
        # return render(request, 'analyze.html', params)
        djtext=analyzedd
    
        # analyzed = djtext
       
        

    if(check!="on" and charcount!="on" and upper1!="on"):
        return HttpResponse("error")
    return render(request, 'analyze.html', params)







