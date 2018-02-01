from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.blog_title, name="blog_title"),
    url(r'(?P<article_id>\d)/$', views.blog_article, name="blog_details"),
] #相应的三个参数：正则表达式， 映射后的响应方法，对应网页的标题