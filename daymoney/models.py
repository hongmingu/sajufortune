from django.db import models


class DayMoney(models.Model):
    text = models.TextField(max_length=800, null=True, blank=True)
    quote = models.TextField(max_length=200, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "DayMoney pk: %s, quote: %s" % (self.pk, self.quote)


class DayMoneyEnglish(models.Model):

    day_money = models.OneToOneField(DayMoney, on_delete=models.CASCADE)

    text = models.TextField(max_length=800, null=True, blank=True)
    quote = models.TextField(max_length=200, null=True, blank=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.day_money.pk


class DayMoneySpanish(models.Model):
    day_money = models.OneToOneField(DayMoney, on_delete=models.CASCADE)

    text = models.TextField(max_length=800, null=True, blank=True)
    quote = models.TextField(max_length=200, null=True, blank=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.day_money.pk


class DayMoneyChinese(models.Model):
    day_money = models.OneToOneField(DayMoney, on_delete=models.CASCADE)

    text = models.TextField(max_length=800, null=True, blank=True)
    quote = models.TextField(max_length=200, null=True, blank=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.day_money.pk


class DayMoneyArabic(models.Model):
    day_money = models.OneToOneField(DayMoney, on_delete=models.CASCADE)

    text = models.TextField(max_length=800, null=True, blank=True)
    quote = models.TextField(max_length=200, null=True, blank=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.day_money.pk


class DayMoneyPortuguese(models.Model):
    day_money = models.OneToOneField(DayMoney, on_delete=models.CASCADE)

    text = models.TextField(max_length=800, null=True, blank=True)
    quote = models.TextField(max_length=200, null=True, blank=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.day_money.pk
