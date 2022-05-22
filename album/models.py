from django.db import models


# Create your models here.
class PostCategory(models.Model):
    name = models.CharField('カテゴリー', max_length=50)
    def __str__(self):
        return self.name

class AlbumM(models.Model):
    title = models.CharField('タイトル', max_length=50)
    category = models.ForeignKey(PostCategory, verbose_name='カテゴリー', on_delete=models.PROTECT)
    name = models.CharField('なまえ', max_length=20)
    age = models.IntegerField()
    explanation = models.TextField('情報', default="---")
    created_at = models.DateField('作成日', auto_now_add=True)
    updated_at = models.DateField('更新日', auto_now=True)

    def __str__(self):
        return str(self.category) + '(' + str(self.title) + ')'

class mkSelectM(models.Model):
    item_id=models.IntegerField('年代')
    memo_id = models.IntegerField('流れ')
    ko_id = models.IntegerField('Article')
