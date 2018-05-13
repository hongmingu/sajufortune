from django.db import models


class DayRelationships(models.Model):
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
        if self.arabic is "":
            ara = "0"
        else:
            ara = "1"
        if self.chinese is "":
            chi = "0"
        else:
            chi = "1"
        if self.english is "":
            eng = "0"
        else:
            eng = "1"
        if self.portuguese is "":
            por = "0"
        else:
            por = "1"
        if self.spanish is "":
            spa = "0"
        else:
            spa = "1"
        if self.quote_arabic is "":
            quote_ara = "0"
        else:
            quote_ara = "1"
        if self.quote_chinese is "":
            quote_chi = "0"
        else:
            quote_chi = "1"
        if self.quote_english is "":
            quote_eng = "0"
        else:
            quote_eng = "1"
        if self.quote_portuguese is "":
            quote_por = "0"
        else:
            quote_por = "1"
        if self.quote_spanish is "":
            quote_spa = "0"
        else:
            quote_spa = "1"
        return "num: %s,  %s-%s-%s-%s-%s, quote: %s-%s-%s-%s-%s" % (self.num, ara, chi, eng, por, spa, quote_ara, quote_chi, quote_eng, quote_por, quote_spa)



