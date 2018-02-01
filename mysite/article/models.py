from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.urlresolvers import reverse
from slugify import  slugify#将对应的标题内容转换（或翻译）成制定格式的英文拼写形式



class ArticleColumn(models.Model):
    user = models.ForeignKey(User, related_name='article_column')#定义了一种在Djaogo中一对多的关系，其中的 一 是User， 多 是article_column
    column = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.column

class ArticlePost(models.Model):
    author = models.ForeignKey(User, related_name="article")#related_name 对应与由user来查找相应的ArticlePost所对应的名字
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=500)
    column = models.ForeignKey(ArticleColumn, related_name="article_column")
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now())
    updated = models.DateTimeField(auto_now=True)

    class Meta:#对id，slug建立索引便于快速搜索
        ordering = ('-updated',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.title

    def save(self, *args, **kargs):#对模型内的save函数进行重写，为的是将标题通过slugify翻译后保存到相应的slug属性中
        self.slug = slugify(self.title)
        super(ArticlePost, self).save(*args, **kargs)

    def get_absolute_url(self):
        return reverse("article:article_detail", args=[self.id, self.slug])

    def get_url_path(self):
        #return "/article/read-article/{0}/{1}".format(self.id, self.slug)
        return reverse("article:list_article_detail", args=[self.id, self.slug])


