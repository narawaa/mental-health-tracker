from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306241770',
        'name': 'Nashwa Ghania',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)