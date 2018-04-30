from django.db import models


class DayWork(models.Model):
    text = models.TextField(max_length=800, null=True, blank=True)
    quote = models.TextField(max_length=200, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "DayWork pk: %s, quote: %s" % (self.pk, self.quote)


class DayWorkEnglish(models.Model):
    day_work = models.OneToOneField(DayWork, on_delete=models.CASCADE)

    text = models.TextField(max_length=800)
    quote = models.TextField(max_length=200)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.day_work.pk


class DayWorkSpanish(models.Model):
    day_work = models.OneToOneField(DayWork, on_delete=models.CASCADE)

    text = models.TextField(max_length=800)
    quote = models.TextField(max_length=200)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.day_work.pk


class DayWorkChinese(models.Model):
    day_work = models.OneToOneField(DayWork, on_delete=models.CASCADE)

    text = models.TextField(max_length=800)
    quote = models.TextField(max_length=200)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.day_work.pk


class DayWorkArabic(models.Model):
    day_work = models.OneToOneField(DayWork, on_delete=models.CASCADE)

    text = models.TextField(max_length=800)
    quote = models.TextField(max_length=200)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.day_work.pk


class DayWorkPortuguese(models.Model):
    day_work = models.OneToOneField(DayWork, on_delete=models.CASCADE)

    text = models.TextField(max_length=800)
    quote = models.TextField(max_length=200)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.day_work.pk
