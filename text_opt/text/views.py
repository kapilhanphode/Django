#own created file by user
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def analyze(request):
    #Get text
    textbox_text=request.POST.get('text','default')
    #Check textbox tick
    cb_remove_punctuation=request.POST.get('removepunc','off')
    cb_upper_case=request.POST.get('uppercase','off')
    cb_new_line_remove=request.POST.get('newlineremove','off')
    cb_remove_number=request.POST.get('removenumber','off')

    if cb_remove_punctuation=='on':
        punctuation='''/[-[\]{}()*@+?.,\\^$|#\]/g,%!"\\$&"'''
        analyze=''
        for char in textbox_text:
            if char not in punctuation:
                analyze=analyze+char
        parameters = {'operation': 'Remove punctuation', 'analyzed_text': analyze}
        textbox_text=analyze
        #return render(request,'analyze.html',parameters)
    if cb_upper_case=='on':
        analyze=''
        for char in textbox_text:
            analyze=analyze+char.upper()
        parameters = {'operation': 'Upper Case', 'analyzed_text': analyze}
        textbox_text=analyze
        #return render(request,'analyze.html',parameters)
    if cb_new_line_remove=='on':
        analyze=''
        for char in textbox_text:
            if char !="\n" and char !="\r":
                analyze=analyze+char
        parameters = {'operation': 'New Line Remove', 'analyzed_text': analyze}
        textbox_text=analyze
        #return render(request,'analyze.html',parameters)
    if cb_remove_number=='on':
        analyze=''
        numbers='0123456789'
        for char in textbox_text:
            if char not in numbers:
                analyze=analyze+char
        parameters = {'operation': 'New Line Remove', 'analyzed_text': analyze}
        analyze = textbox_text
        #return render(request, 'analyze.html', parameters)
    if cb_remove_punctuation!='on' and cb_upper_case!='on' and cb_new_line_remove!='on' and cb_remove_number!='on':
        return HttpResponse("<h1>Check box tick missing</h1>")

    return render(request,'analyze.html',parameters)