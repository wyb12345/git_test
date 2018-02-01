from django.shortcuts import render, get_object_or_404
from blog.models import BlogArticles
# Create your views here.
def blog_title(request):
	blogs = BlogArticles.objects.all()
	return render(request, "blog/titles.html", {"blogs": blogs})

def blog_article(request, article_id):
	article = get_object_or_404(BlogArticles, id = article_id)
	pub = article.publish
	return render(request, "blog/content.html", {"article": article, "publish": pub})
#相应函数的返回参数：request， 对应的html文件（前面可以架上相应的路径），对应的处理后的参数（格式为：html中变量的名字： 当前函数中处理后的变量名字）


