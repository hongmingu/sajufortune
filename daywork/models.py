from django.db import models


class DayWork(models.Model):
    text = models.TextField(max_length=800, null=True, blank=True)
    quote = models.TextField(max_length=200, null=True, blank=True)

    num = models.PositiveSmallIntegerField(default=0)

    quote_arabic = models.TextField(max_length=200, null=True, blank=True)
    quote_chinese = models.TextField(max_length=200, null=True, blank=True)
    quote_english = models.TextField(max_length=200, null=True, blank=True)
    quote_portuguese = models.TextField(max_length=200, null=True, blank=True)
    quote_spanish = models.TextField(max_length=200, null=True, blank=True)

    arabic = models.TextField(max_length=800, null=True, blank=True)
    chinese = models.TextField(max_length=800, null=True, blank=True)
    english = models.TextField(max_length=800, null=True, blank=True)
    portuguese = models.TextField(max_length=800, null=True, blank=True)
    spanish = models.TextField(max_length=800, null=True, blank=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "DayWork num: %s, quote: %s" % (self.num, self.quote)

