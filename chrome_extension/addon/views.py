from django.shortcuts import render


# Create your views here.
def front_page(request):
    if request.method == "POST":
        print(request.POST.get("link"))
    return render(request, "addon/demo.html")