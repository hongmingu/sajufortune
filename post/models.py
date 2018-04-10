from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
# 어차피 데이터베이스에 들어간 년도 숫자 월 숫자 일 숫자 다 더하고 오전과 오후 나눠서 0과 1 주고 나눠서 나머지로 가
# 애드센스 에이잭스 안되고 목록에 같이 애드센스 있는 것처럼 가는 것이 클릭률 높이기에 좋을 것 같다. 막연한 예측 운세면 내일운세, 며칠 후 운세 보기 아래에 목록 만들고 그 사이에 넣기
# 톡스위버는 목록에 하나놓고 글 시작할 때 채팅창 처음에 애드센스 넣고 맨위나 아래에 애드센스 등장하게 구성.
# 페이스북 트위터 텀블러 핀터레스트 모두 다 퍼가기 쉽게 만들어야 한다. 레딧도 가능하면 하고 .
# 2000로 채우면 대부분, 데일리는 1000byte 안에 다 들어갈 것이다.


class Post(models.Model):
    celebrity = models.ForeignKey('celebrity.Celebrity', on_delete=models.CASCADE, null=True, blank=True)
    title = models.TextField(max_length=200, null=True, blank=True)

    target_year = models.CharField(max_length=4, null=True, blank=True)
    target_month = models.CharField(max_length=2, null=True, blank=True)
    target_day = models.CharField(max_length=2, null=True, blank=True)

    photo = models.ImageField(null=True, blank=True, upload_to="photo/%Y/%m/%d")

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        celebrity_name = None
        try:
            celebrity_name = self.celebrity.name
        except:
            celebrity_name = 'noname'

        return "name: %s, title: %s,  target_date: %s %s %s" % (celebrity_name,
                                                                self.title,
                                                                self.target_year,
                                                                self.target_month,
                                                                self.target_day)


class PostEnglish(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)

    title = models.TextField(max_length=200)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "name: %s, target_date: %s %s %s, post_pk: %s" % (self.post.celebrity.name,
                                                                 self.post.target_year,
                                                                 self.post.target_month,
                                                                 self.post.target_day,
                                                                 self.post.pk)


class PostSpanish(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)

    title = models.TextField(max_length=200)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "name: %s, target_date: %s %s %s, post_pk: %s" % (self.post.name,
                                                                 self.post.target_year,
                                                                 self.post.target_month,
                                                                 self.post.target_day,
                                                                 self.post.pk)


class PostChinese(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)

    title = models.TextField(max_length=200)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "name: %s, target_date: %s %s %s, post_pk: %s" % (self.post.name,
                                                                 self.post.target_year,
                                                                 self.post.target_month,
                                                                 self.post.target_day,
                                                                 self.post.pk)


class PostArabic(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)

    title = models.TextField(max_length=200)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "name: %s, target_date: %s %s %s, post_pk: %s" % (self.post.name,
                                                                 self.post.target_year,
                                                                 self.post.target_month,
                                                                 self.post.target_day,
                                                                 self.post.pk)


class PostPortuguese(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)

    title = models.TextField(max_length=200)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "name: %s, target_date: %s %s %s, post_pk: %s" % (self.post.name,
                                                                 self.post.target_year,
                                                                 self.post.target_month,
                                                                 self.post.target_day,
                                                                 self.post.pk)

