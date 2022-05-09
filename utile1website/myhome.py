from django.http import HttpResponse
from django.shortcuts import render
def start(request):
    mines={'name': 'shubham', 'place': 'mumbai'}
    return render(request,'home1.html',mines)
def analyze(request):
    clntext=request.POST.get('clntext','default')
    rmvpunc=request.POST.get('rmvpnc','default')
    spacermv=request.POST.get('extraspacermv','default')
    linermv=request.POST.get('linermv','default')
    captlz=request.POST.get('caps','default')
    back=request.POST.get('back','default')
    analyzetxt=""
    punctuation='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
    if(rmvpunc=="on"):
        analyzetxt=""
        for char in clntext:
            if char not in punctuation:
                analyzetxt= analyzetxt+char
        mines={'Entered_text':"Remove Punctuation's","Ready_text":analyzetxt}
        clntext=analyzetxt
    if(spacermv=="on"):
        analyzetxt=""
        for index,char in enumerate(clntext):
            if clntext[index]==" " and clntext[index +1]==" ":
                pass
            else:
                analyzetxt=analyzetxt+char
        mines = {'Entered_text':"Remove Extra Space", "Ready_text": analyzetxt}
        clntext=analyzetxt
    if(linermv=="on"):
        analyzetxt=""
        for char in clntext:
            if char !="\n"and char !="\r":
                analyzetxt=analyzetxt+char
        mines = {'Entered_text':"Remove Extra Line's", "Ready_text": analyzetxt}
        clntext=analyzetxt
    if (captlz=="on"):
        analyzetxt=""
        for char in clntext:
            analyzetxt=analyzetxt+char.upper()
        mines = {'Entered_text':"Capitlize your Text", "Ready_text": analyzetxt}
    if(rmvpunc !="on" and spacermv !="on" and linermv !="on" and captlz !="on"):
        return render(request,'error.html')
    return render(request,'analyze.html',mines)
def contactus(request):
    return render(request,'contactus.html')
def feedback(request):
    return render(request,'feedback.html')
def feedbacksbmt(request):
    clientname=request.POST.get('clntname','default')
    clntemail=request.POST.get('clnteml','default')
    clntfdbk=request.POST.get('clntfdbk','default')
    mines={'name':clientname}
    return render(request,'feedbacksbmt.html',mines)











