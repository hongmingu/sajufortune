from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
# 어차피 데이터베이스에 들어간 년도 숫자 월 숫자 일 숫자 다 더하고 오전과 오후 나눠서 0과 1 주고 나눠서 나머지로 가
# 애드센스 에이잭스 안되고 목록에 같이 애드센스 있는 것처럼 가는 것이 클릭률 높이기에 좋을 것 같다. 막연한 예측 운세면 내일운세, 며칠 후 운세 보기 아래에 목록 만들고 그 사이에 넣기
# 톡스위버는 목록에 하나놓고 글 시작할 때 채팅창 처음에 애드센스 넣고 맨위나 아래에 애드센스 등장하게 구성.
# 페이스북 트위터 텀블러 핀터레스트 모두 다 퍼가기 쉽게 만들어야 한다. 레딧도 가능하면 하고 .
# 2000로 채우면 대부분, 데일리는 1000byte 안에 다 들어갈 것이다.


class Celebrity(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)

    birthday_year = models.CharField(max_length=4, null=True, blank=True)
    birthday_month = models.CharField(max_length=2, null=True, blank=True)
    birthday_day = models.CharField(max_length=2, null=True, blank=True)

    photo = models.ImageField(null=True, blank=True, upload_to="photo/%Y/%m/%d")

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "name: %s, birthday_date: %s %s %s" % (self.name, self.birthday_year, self.birthday_month, self.birthday_day)


class CelebrityEnglish(models.Model):
    celebrity = models.OneToOneField(Celebrity, on_delete=models.CASCADE)

    name = models.TextField(max_length=100)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "name: %s English" % self.celebrity.name


class CelebrityChinese(models.Model):
    celebrity = models.OneToOneField(Celebrity, on_delete=models.CASCADE)

    name = models.TextField(max_length=100)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "name: %s Chinese" % self.celebrity.name


class CelebrityArabic(models.Model):
    celebrity = models.OneToOneField(Celebrity, on_delete=models.CASCADE)

    name = models.TextField(max_length=100)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "name: %s Arabic" % self.celebrity.name


class CelebrityPortuguese(models.Model):
    celebrity = models.OneToOneField(Celebrity, on_delete=models.CASCADE)

    name = models.TextField(max_length=100)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "name: %s Portuguese" % self.celebrity.name


class CelebritySpanish(models.Model):
    celebrity = models.OneToOneField(Celebrity, on_delete=models.CASCADE)

    name = models.TextField(max_length=100)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "name: %s Spanish" % self.celebrity.name

