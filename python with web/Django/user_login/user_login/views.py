from django.http import HttpResponse


def home(request):
    # print(request + '  hello')
    return HttpResponse('''
                        <center>
                        <h1> Home</h1>
                        <br/> 
                        <a href="/login/2/">
                        login tag
                        </a>
                        </center>
                        ''')
