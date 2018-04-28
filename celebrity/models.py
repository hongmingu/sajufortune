# Create your models here.
from django.db import models


class Celebrity(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)

    birthday_year = models.CharField(max_length=4, null=True, blank=True)
    birthday_month = models.CharField(max_length=2, null=True, blank=True)
    birthday_day = models.CharField(max_length=2, null=True, blank=True)

    photo = models.ImageField(null=True, blank=True, upload_to="photo/%Y/%m/%d")

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "name: %s, birthday_date: %s %s %s" % (self.name, self.birthday_year, self.birthday_month, self.birthday_day)


class CelebrityEnglish(models.Model):
    celebrity = models.OneToOneField(Celebrity, on_delete=models.CASCADE)

    name = models.TextField(max_length=100)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "name: %s English" % self.celebrity.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('celebrity:profile', kwargs={'lang': 'eng', 'num': self.celebrity.pk})


class CelebrityChinese(models.Model):
    celebrity = models.OneToOneField(Celebrity, on_delete=models.CASCADE)

    name = models.TextField(max_length=100)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "name: %s Chinese" % self.celebrity.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('celebrity:profile', kwargs={'lang': 'chi', 'num': self.celebrity.pk})


class CelebrityArabic(models.Model):
    celebrity = models.OneToOneField(Celebrity, on_delete=models.CASCADE)

    name = models.TextField(max_length=100)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "name: %s Arabic" % self.celebrity.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('celebrity:profile', kwargs={'lang': 'ara', 'num': self.celebrity.pk})


class CelebrityPortuguese(models.Model):
    celebrity = models.OneToOneField(Celebrity, on_delete=models.CASCADE)

    name = models.TextField(max_length=100)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "name: %s Portuguese" % self.celebrity.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('celebrity:profile', kwargs={'lang': 'por', 'num': self.celebrity.pk})


class CelebritySpanish(models.Model):
    celebrity = models.OneToOneField(Celebrity, on_delete=models.CASCADE)

    name = models.TextField(max_length=100)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "name: %s Spanish" % self.celebrity.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('celebrity:profile', kwargs={'lang': 'spa', 'num': self.celebrity.pk})
