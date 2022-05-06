from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Qori(models.Model):
    name = models.CharField('Qorining ismi' ,max_length=200)
    slug = models.SlugField('Slug' ,max_length=200)
    
    class Meta:
        verbose_name = 'Qori'
        verbose_name_plural = 'Qorilar'

    def get_absolute_url(self):
        return f"/qori/{self.slug}/"

    def __str__(self):
        return self.name

        

class Sura(models.Model):
    title_arabic = models.CharField('Arabcha matni' ,max_length=30)
    title_eng = models.CharField('Inglizcha matni' ,max_length=30)
    title_uz = models.CharField('O\'zbekcha matni' ,max_length=30)
    slug = models.SlugField('Slug' ,max_length=30)
    qori = models.ForeignKey(Qori , on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Sura'
        verbose_name_plural = 'Suralar'

    def get_absolute_url(self):
        return f"/sura/{self.slug}"

    def __str__(self):
        return str(self.qori) + ' | ' + self.title_uz

class Oyat(models.Model):
    audio = models.FileField('Audio' ,upload_to='audios/')
    text_arabic = models.CharField('Arabcha matni' ,max_length=255)
    text_uzb = models.CharField('O\'qilishi' ,max_length=255)
    text_tafsir = models.CharField('O\'zbekchadagi ma\'nosi',max_length=1000)
    tr_sura = models.IntegerField('Suradagi t/r', default=0)
    tr_umumiy = models.IntegerField('Qur\'ondagi t/r', default=0)
    sajda_tafsiya = models.CharField('Sajda tafsiya', default='Yo\'q',max_length=4)
    sajda_majburiy = models.CharField('Sajda majburiy', default='Yo\'q',max_length=4)
    sura = models.ForeignKey(Sura , on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Oyat'
        verbose_name_plural = 'Oyatlar'

    def __str__(self):
        return 'Surada : ' + str(self.tr_sura) + '-oyat | Umumiyda : ' + str(self.tr_umumiy) + '-oyat' 

class Domla(models.Model):
    name = models.CharField('Domlaning ismi' ,max_length=200)
    slug = models.SlugField('Slug' ,max_length=200)

    class Meta:
        verbose_name = 'Domla'
        verbose_name_plural = 'Domlalar'

    def get_absolute_url(self):
        return f"/maruzalar/{self.slug}"

    def __str__(self):
        return self.name

class Maruza(models.Model):
    url_video = models.URLField('Video URL' ,max_length=100)
    popular = models.IntegerField('Ko\'rilganlar soni' ,default=0)
    image = models.ImageField('Rasm' ,upload_to='maruzaimg/')
    title = models.CharField('Sarlavha', max_length=150)
    date = models.DateField(default=timezone.now)
    slug = models.SlugField('Slug' ,max_length=200)
    domla = models.ForeignKey(Domla , on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Maruza'
        verbose_name_plural = 'Maruzalar'
        
  

    def get_absolute_url(self):
        return f"/maruza/{self.slug}"

    def __str__(self):
        return str(self.domla)
