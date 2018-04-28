# Create your models here.
from django.db import models


class Post(models.Model):
    celebrity = models.ForeignKey('celebrity.Celebrity', on_delete=models.CASCADE, null=True, blank=True)
    title = models.TextField(max_length=200, null=True, blank=True)

    target_year = models.CharField(max_length=4, null=True, blank=True)
    target_month = models.CharField(max_length=2, null=True, blank=True)
    target_day = models.CharField(max_length=2, null=True, blank=True)

    photo = models.ImageField(null=True, blank=True, upload_to="photo/%Y/%m/%d")

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        celebrity_name = None
        try:
            celebrity_name = self.celebrity.name
        except:
            celebrity_name = 'noname'

        return "name: %s, title: %s,  target_date: %s %s %s" % (celebrity_name,
                                                                self.title,
                                                                self.target_year,
                                                                self.target_month,
                                                                self.target_day)


class PostEnglish(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)

    title = models.TextField(max_length=200)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "name: %s, target_date: %s %s %s, post_pk: %s" % (self.post.celebrity.name,
                                                                 self.post.target_year,
                                                                 self.post.target_month,
                                                                 self.post.target_day,
                                                                 self.post.pk)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('post:detail', kwargs={'lang': 'eng', 'num': self.post.pk})


class PostSpanish(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)

    title = models.TextField(max_length=200)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "name: %s, target_date: %s %s %s, post_pk: %s" % (self.post.celebrity.name,
                                                                 self.post.target_year,
                                                                 self.post.target_month,
                                                                 self.post.target_day,
                                                                 self.post.pk)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('post:detail', kwargs={'lang': 'spa', 'num': self.post.pk})


class PostChinese(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)

    title = models.TextField(max_length=200)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "name: %s, target_date: %s %s %s, post_pk: %s" % (self.post.celebrity.name,
                                                                 self.post.target_year,
                                                                 self.post.target_month,
                                                                 self.post.target_day,
                                                                 self.post.pk)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('post:detail', kwargs={'lang': 'chi', 'num': self.post.pk})


class PostArabic(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)

    title = models.TextField(max_length=200)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "name: %s, target_date: %s %s %s, post_pk: %s" % (self.post.celebrity.name,
                                                                 self.post.target_year,
                                                                 self.post.target_month,
                                                                 self.post.target_day,
                                                                 self.post.pk)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('post:detail', kwargs={'lang': 'ara', 'num': self.post.pk})


class PostPortuguese(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)

    title = models.TextField(max_length=200)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "name: %s, target_date: %s %s %s, post_pk: %s" % (self.post.celebrity.name,
                                                                 self.post.target_year,
                                                                 self.post.target_month,
                                                                 self.post.target_day,
                                                                 self.post.pk)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('post:detail', kwargs={'lang': 'por', 'num': self.post.pk})
