from django.db import models


class DayLove(models.Model):
    text = models.TextField(max_length=800, null=True, blank=True)
    quote = models.TextField(max_length=200, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "DayLove pk: %s, quote: %s" % (self.pk, self.quote)


class DayLoveEnglish(models.Model):

    day_love = models.OneToOneField(DayLove, on_delete=models.CASCADE)

    text = models.TextField(max_length=800, null=True, blank=True)
    quote = models.TextField(max_length=200, null=True, blank=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.day_love.pk


class DayLoveSpanish(models.Model):
    day_love = models.OneToOneField(DayLove, on_delete=models.CASCADE)

    text = models.TextField(max_length=800, null=True, blank=True)
    quote = models.TextField(max_length=200, null=True, blank=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.day_love.pk


class DayLoveChinese(models.Model):
    day_love = models.OneToOneField(DayLove, on_delete=models.CASCADE)

    text = models.TextField(max_length=800, null=True, blank=True)
    quote = models.TextField(max_length=200, null=True, blank=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.day_love.pk


class DayLoveArabic(models.Model):
    day_love = models.OneToOneField(DayLove, on_delete=models.CASCADE)

    text = models.TextField(max_length=800, null=True, blank=True)
    quote = models.TextField(max_length=200, null=True, blank=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.day_love.pk


class DayLovePortuguese(models.Model):
    day_love = models.OneToOneField(DayLove, on_delete=models.CASCADE)

    text = models.TextField(max_length=800, null=True, blank=True)
    quote = models.TextField(max_length=200, null=True, blank=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.day_love.pk
