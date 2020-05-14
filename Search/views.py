from django.shortcuts import render
from Search.documents import TvShowDocument

# Create your views here.

def search(request):
    keyword = request.GET.get("keyword")
    if keyword:
        series = TvShowDocument.search().query("match", keywords=keyword)
    return render(request, "search.html", {"series": series})
