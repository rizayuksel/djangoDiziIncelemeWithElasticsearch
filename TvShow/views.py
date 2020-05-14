from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse, HttpResponseRedirect
from .models import TvShow, Comment, Watchlist
from django.db.models import F
#from django.utils.text import slugify
#from Search.documents import TvShowDocument

# Create your views here.

def index(request):
    #ESKİ ARAMA YAPISI
    #keyword = request.GET.get("keyword")  # arama yapmak için
    #if keyword:
    #    series = TvShow.objects.filter(title__contains=keyword)
    #    return render(request, "index.html", {"series": series})
    series = TvShow.objects.all()  # Autos veri tabanındaki tüm verileri sözlük yapısıyla aldık
    return render(request, "index.html", {"series": series})


def crime(request):
    series = TvShow.objects.filter(kind__contains="Suç")
    kind = "Suç"
    return render(request, "kind.html", {"series": series, "kind": kind})

def comedy(request):
    series = TvShow.objects.filter(kind__contains="Komedi")
    kind = "Komedi"
    return render(request, "kind.html", {"series": series, "kind": kind})

def mystery(request):
    series = TvShow.objects.filter(kind__contains="Gizem")
    kind = "Gizem"
    return render(request, "kind.html", {"series": series, "kind": kind})

def scifi(request):
    series = TvShow.objects.filter(kind__contains="Bilim Kurgu")
    kind = "Bilim Kurgu"
    return render(request, "kind.html", {"series": series, "kind": kind})

def sport(request):
    series = TvShow.objects.filter(kind__contains="Spor")
    kind = "Spor"
    return render(request, "kind.html", {"series": series, "kind": kind})

def action(request):
    series = TvShow.objects.filter(kind__contains="Aksiyon")
    kind = "Aksiyon"
    return render(request, "kind.html", {"series": series, "kind": kind})

def documentary(request):
    series = TvShow.objects.filter(kind__contains="Belgesel")
    kind = "Belgesel"
    return render(request, "kind.html", {"series": series, "kind": kind})

def detective(request):
    series = TvShow.objects.filter(kind__contains="Dedektiflik")
    kind = "Dedektiflik"
    return render(request, "kind.html", {"series": series, "kind": kind})

def drama(request):
    series = TvShow.objects.filter(kind__contains="Dram")
    kind = "Dram"
    return render(request, "kind.html", {"series": series, "kind": kind})

def thriller(request):
    series = TvShow.objects.filter(kind__contains="Gerilim")
    kind = "Gerilim"
    return render(request, "kind.html", {"series": series, "kind": kind})

def horror(request):
    series = TvShow.objects.filter(kind__contains="Korku")
    kind = "Korku"
    return render(request, "kind.html", {"series": series, "kind": kind})

def romantic(request):
    series = TvShow.objects.filter(kind__contains="Romantik")
    kind = "Romantik"
    return render(request, "kind.html", {"series": series, "kind": kind})

def historical(request):
    series = TvShow.objects.filter(kind__contains="Tarih")
    kind = "Tarih"
    return render(request, "kind.html", {"series": series, "kind": kind})

def foreign(request):
    series = TvShow.objects.filter(kind__contains="Yabancı")
    kind = "Yabancı"
    return render(request, "kind.html", {"series": series, "kind": kind})

def domestic(request):
    series = TvShow.objects.filter(kind__contains="Yerli")
    kind = "Yerli"
    return render(request, "kind.html", {"series": series, "kind": kind})

def detail(request, id):
    # ziyaretçi sayısı
    post = TvShow.objects.get(id=id)
    post.visitors = F('visitors') + 1
    post.save()

    #Tablodaki verileri çekme
    series = get_object_or_404(TvShow, id=id)
    comments = series.comments.all()
    return render(request, "detail.html", {"series": series, "comments": comments})


def comment(request, id):
    series = get_object_or_404(TvShow, id=id)
    if request.method == "POST":
        username = request.user
        content = request.POST.get("content")

        newComment = Comment(username=username, content=content)
        newComment.series = series
        newComment.save()
    return redirect(reverse("TvShow:detail", kwargs={"id": id}))

def watchlist(request, id):
    series = get_object_or_404(TvShow, id=id)
    watchl = Watchlist.objects.filter(series = series, username = request.user)
    if watchl.exists():
        watchl.delete()
    else:
        Watchlist.objects.create(series = series, username = request.user)
    return redirect(reverse("TvShow:detail", kwargs={"id": id}))
