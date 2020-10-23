from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView

# Create your views here.


def home_view(httprequest, *args):
    my_dict = {
        "name": "alex",
        "lastname": "buechel",
        "year": 1922,
        "myList" : ["this", "is", "my", "list", "hello"],
    }
    return render(httprequest, "home.html", my_dict)


class HomeViewClass(View):
    def get(self, httprequest):
        return HttpResponse("<hl>Hello world from the class</hl>")


class AboutView(TemplateView):
    template_name = "about.html"
