# Python Django Dizi Inceleme With Elasticsearch

Python'ın Django framework'ü kullanılarak hazırlanılan, Elasticsearch arama teknolojisi kullanılan full stack web projesi.

## 1.Ana Sayfa
Siteye eklenen dizilerin listelendiği sayfa.
![2 Anasayfa](https://user-images.githubusercontent.com/52426752/95788525-61557780-0ce4-11eb-8b16-3d76bd66aabe.PNG)

## 2.Türlerine Göre Dizi Filtreleme
Navbar'dan seçilen dizi türünden dizilerin filtrelendiği sayfalar.
![3 Suç Dizileri Sayfası](https://user-images.githubusercontent.com/52426752/95788541-64506800-0ce4-11eb-9ccf-668182ca95a0.PNG)

## 3.Elasticsearch ile Arama Sayfası
Bu sayfada Elasticsearch yapısı kullanıldı. Navbar'daki form'dan gelen keyword Backend'e gönderildi, bu keyword'e göre arama yapıldı.
![4 Arama Yapma Ekranı](https://user-images.githubusercontent.com/52426752/95788586-7af6bf00-0ce4-11eb-98e0-0126590b019a.PNG)

## 4.Dizilerin Detaylarını İçeren Sayfalar
Veri tabanımızdaki Dizi Id'lerine göre her diziye bir URL ayarlandı, Bu sayfalarda dizilerin detayları ve yorumları gösterildi. Kullanıcı eğer giriş yapmadıysa yorum yapmaması sadece yorumları görmesi sağlandı.
![5 Dizilerin Detay Sayfası2](https://user-images.githubusercontent.com/52426752/95788617-8cd86200-0ce4-11eb-8628-a7de1a95b8f6.PNG)
![6 Kullanıcı Girişi Yapılmamışken Yorumlar Ekranı2](https://user-images.githubusercontent.com/52426752/95788670-a24d8c00-0ce4-11eb-9eed-8a27df782741.png)
![8 Yorumların Listelenmesi2](https://user-images.githubusercontent.com/52426752/95788710-b2fe0200-0ce4-11eb-9c95-179f6db227ef.PNG)

## 5.Register
Kullanıcının sitemize üye olmasını sağlamak için bir Kayıt Ol formu tasarlandı. Burada Crispy Forms yapısı kullanıldı.
![10 Kayıt Ol Sayfası](https://user-images.githubusercontent.com/52426752/95788719-b7c2b600-0ce4-11eb-8985-4cd9b90bc749.PNG)

## 6.Login
Kayıtlı olan kullanıcılarımızın sitemize giriş yapabilmesi için bir Giriş Yap formu tasarlandı. Burada Crispy Forms yapısı kullanıldı.
![9 Giriş Yap Sayfası](https://user-images.githubusercontent.com/52426752/95788715-b5605c00-0ce4-11eb-88c0-25c5965fb6c4.PNG)

## 7.Admin Paneli
Sitemize dizi ekleyebilmek, silebilmek, güncelleyebilmek, gerektiği zaman kullanıcılara yetki vermek veya banlayabilmek için bir admin paneli tasarlandı.

![11 Admin Paneline Giriş](https://user-images.githubusercontent.com/52426752/95789715-b2ff0180-0ce6-11eb-8f17-a3ed86f59372.PNG)
![12 Dizilerin Admin Panelindeki Görünümü](https://user-images.githubusercontent.com/52426752/95789722-b4c8c500-0ce6-11eb-9d72-2653c3d84f7b.PNG)
![13 Yeni Dizi Ekleme Sayfası](https://user-images.githubusercontent.com/52426752/95788727-bc876a00-0ce4-11eb-9317-a88e28f74cdf.PNG)
