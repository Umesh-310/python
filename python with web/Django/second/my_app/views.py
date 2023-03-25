from django.shortcuts import render

# Create your views here.


def example(request):
    my_var = {
        'first_name': 'aku',
        'last_name': 'Saini',
        'names': ['Aku', 'Umesh', 'Raj', 'Yash', 'Nilesh']
    }
    return render(request, 'page/index.html', context=my_var)


def variable_view(request):
    return render(request, 'page/variable.html')
