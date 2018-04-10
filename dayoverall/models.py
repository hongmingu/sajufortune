from django.db import models

# Create your models here.
# 어차피 데이터베이스에 들어간 년도 숫자 월 숫자 일 숫자 다 더하고 오전과 오후 나눠서 0과 1 주고 나눠서 나머지로 가
# 애드센스 에이잭스 안되고 목록에 같이 애드센스 있는 것처럼 가는 것이 클릭률 높이기에 좋을 것 같다. 막연한 예측 운세면 내일운세, 며칠 후 운세 보기 아래에 목록 만들고 그 사이에 넣기
# 톡스위버는 목록에 하나놓고 글 시작할 때 채팅창 처음에 애드센스 넣고 맨위나 아래에 애드센스 등장하게 구성.
# 페이스북 트위터 텀블러 핀터레스트 모두 다 퍼가기 쉽게 만들어야 한다. 레딧도 가능하면 하고 .
# 2000로 채우면 대부분, 데일리는 1000byte 안에 다 들어갈 것이다.


class DayOverall(models.Model):

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "DayOverall of %s" % self.pk


class DayOverallEnglish(models.Model):

    day_whole = models.OneToOneField(DayOverall, on_delete=models.CASCADE)

    text = models.TextField(max_length=1200)
    quote = models.TextField(max_length=400)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.day_whole.pk


class DayOverallSpanish(models.Model):
    day_whole = models.OneToOneField(DayOverall, on_delete=models.CASCADE)

    text = models.TextField(max_length=1200)
    quote = models.TextField(max_length=400)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.day_whole.pk


class DayOverallChinese(models.Model):
    day_whole = models.OneToOneField(DayOverall, on_delete=models.CASCADE)

    text = models.TextField(max_length=1200)
    quote = models.TextField(max_length=400)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.day_whole.pk


class DayOverallArabic(models.Model):
    day_whole = models.OneToOneField(DayOverall, on_delete=models.CASCADE)

    text = models.TextField(max_length=1200)
    quote = models.TextField(max_length=400)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.day_whole.pk


class DayOverallPortuguese(models.Model):
    day_whole = models.OneToOneField(DayOverall, on_delete=models.CASCADE)

    text = models.TextField(max_length=1200)
    quote = models.TextField(max_length=400)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.day_whole.pk
