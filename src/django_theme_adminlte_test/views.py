from django.shortcuts import render

def test01(request):
    return render(request, "django_theme_adminlte_test/test01.html", {
        
    })