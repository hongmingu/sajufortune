from django.db import models


class DayOverall(models.Model):
    text = models.TextField(max_length=800)
    quote = models.TextField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "DayOverall pk: %s, quote: %s" % (self.pk, self.quote)


class DayOverallEnglish(models.Model):

    day_whole = models.OneToOneField(DayOverall, on_delete=models.CASCADE)

    text = models.TextField(max_length=800)
    quote = models.TextField(max_length=200)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.day_whole.pk


class DayOverallSpanish(models.Model):
    day_whole = models.OneToOneField(DayOverall, on_delete=models.CASCADE)

    text = models.TextField(max_length=800)
    quote = models.TextField(max_length=200)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.day_whole.pk


class DayOverallChinese(models.Model):
    day_whole = models.OneToOneField(DayOverall, on_delete=models.CASCADE)

    text = models.TextField(max_length=800)
    quote = models.TextField(max_length=200)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.day_whole.pk


class DayOverallArabic(models.Model):
    day_whole = models.OneToOneField(DayOverall, on_delete=models.CASCADE)

    text = models.TextField(max_length=800)
    quote = models.TextField(max_length=200)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.day_whole.pk


class DayOverallPortuguese(models.Model):
    day_whole = models.OneToOneField(DayOverall, on_delete=models.CASCADE)

    text = models.TextField(max_length=800)
    quote = models.TextField(max_length=200)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.day_whole.pk
