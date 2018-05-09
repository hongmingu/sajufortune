from django.db import models


class DayRelationships(models.Model):
    text = models.TextField(max_length=800, null=True, blank=True)
    quote = models.TextField(max_length=200, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "DayRelationships pk: %s, quote: %s" % (self.pk, self.quote)


class DayRelationshipsEnglish(models.Model):

    day_relationships = models.OneToOneField(DayRelationships, on_delete=models.CASCADE)

    text = models.TextField(max_length=800, null=True, blank=True)
    quote = models.TextField(max_length=200, null=True, blank=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.day_relationships.pk


class DayRelationshipsSpanish(models.Model):
    day_relationships = models.OneToOneField(DayRelationships, on_delete=models.CASCADE)

    text = models.TextField(max_length=800, null=True, blank=True)
    quote = models.TextField(max_length=200, null=True, blank=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.day_relationships.pk


class DayRelationshipsChinese(models.Model):
    day_relationships = models.OneToOneField(DayRelationships, on_delete=models.CASCADE)

    text = models.TextField(max_length=800, null=True, blank=True)
    quote = models.TextField(max_length=200, null=True, blank=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.day_relationships.pk


class DayRelationshipsArabic(models.Model):
    day_relationships = models.OneToOneField(DayRelationships, on_delete=models.CASCADE)

    text = models.TextField(max_length=800, null=True, blank=True)
    quote = models.TextField(max_length=200, null=True, blank=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.day_relationships.pk


class DayRelationshipsPortuguese(models.Model):
    day_relationships = models.OneToOneField(DayRelationships, on_delete=models.CASCADE)

    text = models.TextField(max_length=800, null=True, blank=True)
    quote = models.TextField(max_length=200, null=True, blank=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.day_relationships.pk
