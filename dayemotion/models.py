from django.db import models


class DayEmotion(models.Model):
    text = models.TextField(max_length=800)
    quote = models.TextField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "DayEmotion pk: %s, quote: %s" % (self.pk, self.quote)


class DayEmotionEnglish(models.Model):

    day_emotion = models.OneToOneField(DayEmotion, on_delete=models.CASCADE)

    text = models.TextField(max_length=800)
    quote = models.TextField(max_length=200)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.day_emotion.pk


class DayEmotionSpanish(models.Model):
    day_emotion = models.OneToOneField(DayEmotion, on_delete=models.CASCADE)

    text = models.TextField(max_length=800)
    quote = models.TextField(max_length=200)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.day_emotion.pk


class DayEmotionChinese(models.Model):
    day_emotion = models.OneToOneField(DayEmotion, on_delete=models.CASCADE)

    text = models.TextField(max_length=800)
    quote = models.TextField(max_length=200)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.day_emotion.pk


class DayEmotionArabic(models.Model):
    day_emotion = models.OneToOneField(DayEmotion, on_delete=models.CASCADE)

    text = models.TextField(max_length=800)
    quote = models.TextField(max_length=200)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.day_emotion.pk


class DayEmotionPortuguese(models.Model):
    day_emotion = models.OneToOneField(DayEmotion, on_delete=models.CASCADE)

    text = models.TextField(max_length=800)
    quote = models.TextField(max_length=200)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.day_emotion.pk

