from django.shortcuts import render
from django.http.response import HttpResponse,HttpResponseRedirectBase ,Http404, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def simple_view(request):
    return render(request , 'firstIndex/index.html')



















# articales = {
#     'sports': '<h1> Sport Page </h1>',
#     'finance': '<h1> finance Page </h1>',
#     'news': '<h1> news Page </h1>',
# }


# def sports_page(request, topic):
#     try:
#         result = articales[topic]
#         return HttpResponse(articales[topic])
#     except:
#         raise Http404('404 Nothing Found')


# def add_view(request, num1, num2):
#     totle = num1 + num2
#     return HttpResponse(str(totle))


# def page_num(request, num_page):
#     topice_list = list(articales.keys())
#     print(topice_list)
#     topic = topice_list[num_page]
#     # return HttpResponse('hello')
    
#     return HttpResponseRedirect(reverse('topic-page' , args=[topic]))

# def news_page(request):
#     return HttpResponse('<h1> news Page </h1>')
