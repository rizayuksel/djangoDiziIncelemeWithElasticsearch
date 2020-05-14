from django.db import models

class TvShow(models.Model):  # Diziler tablosu
    title = models.CharField(max_length=150, verbose_name="Dizi Ad")
    kind = models.CharField(max_length=100, verbose_name="Tür")
    issue = models.CharField(max_length=800, verbose_name="Konu")
    year = models.CharField(max_length=12, verbose_name="Yıl")
    director = models.CharField(max_length=70, verbose_name="Yönetmen")
    performer = models.CharField(max_length=250, verbose_name="Oyuncular")
    season = models.CharField(max_length=30, verbose_name="Sezon Sayısı")
    imdbPoint = models.CharField(max_length=5, verbose_name="IMDB Puanı")
    link = models.CharField(max_length=200, verbose_name="Fragman")
    createdDate = models.DateTimeField(auto_now_add=True)
    visitors = models.IntegerField(default=0, verbose_name="Ziyaretçi Sayısı")
    keywords = models.CharField(max_length=500, verbose_name="Anahtar Kelimeler")
    seriesImage = models.FileField(blank=True, null=True, verbose_name="Dizinin Resmini Ekleyin")
    #slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    class Meta:  # Son eklenenin en başa gelmesi için
        ordering = ['kind']
        verbose_name_plural = "Diziler"

    #def getAddedFavUser(self):
    #    self.favorite.values_list("username__username", flat=True)


class Comment(models.Model):
    series = models.ForeignKey(TvShow, on_delete=models.CASCADE, verbose_name="Dizi", related_name="comments")
    username = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Kullanıcı", related_name="comments")
    content = models.CharField(max_length=500, verbose_name="Yorum")
    commentDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s - %s" % (self.username, self.series)

    class Meta:
        ordering = ['-commentDate']
        verbose_name_plural = "Yorumlar"

class Watchlist(models.Model):
    series = models.ForeignKey(TvShow, null=True, on_delete=models.CASCADE, verbose_name="Dizi", related_name="watchlist")
    username = models.ForeignKey("auth.User", null=True, on_delete=models.CASCADE, verbose_name="Kullanıcı", related_name="watchlist")
    addedDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s - %s" % (self.username, self.series)

    class Meta:
        ordering = ['-addedDate']
        verbose_name_plural = "İzlenecekler Listesi"