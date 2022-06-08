from django.http import HttpResponse
from django.shortcuts import render


# def func1(request):
#     return HttpResponse("Hello, guys welcome to my Store")


def home(request):
    # data = {
    #     'title':'BNM',
    #     'Home': 'Welcome Back',
    #     'list1': ['PHP','JAVA','Django','Python'],
    #     'numbers':[10,20,22,14,23,20,52,65,33,256],
    #     'list2': [{'name':'Narin Ahir', 'Phone': 7256548530},
    #               {'name':'Denish Patel', 'Phone': 6256548530}
    #             ]
    # }
    return render (request, 'index.html')



