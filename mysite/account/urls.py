from django.conf.urls import url
from . import views
from django.conf import settings  #?
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$', auth_views.login, name="user_login"),
    url(r'^register/$', views.register, name="user_register"),
    url(r'^logout/$', auth_views.logout, {"template_name":"account/logout.html"}, name="user_logout"),
    url(r'^new_login/$', auth_views.login, {"template_name":"account/login.html"}),
    url(r'^password-change/$', auth_views.password_change, {"post_change_redirect": "/account/password-change-done"},
        name='password_change'),
    url(r'^password-change-done/$', auth_views.password_change_done, name='password_change_done'),
    url(r'^password-reset/$', auth_views.password_reset, {"template_name": "account/password_reset_form.html",
                                                          "email_template_name": "account/password_reset_email.html",
                                                          "subject_template_name":"account/password_reset_subject.txt",
                                                          "post_reset_redirect": "/account/password-reset-done"},
        name="password_reset"),
    url(r'^password-reset-done/$', auth_views.password_reset_done,
        {"template_name": "account/password_reset_done.html"}, name="password_reset_done"),
    url(r'^password-reset-confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', auth_views.password_reset_confirm,
        {"template_name": "account/password_reset_confirm.html",
         "post_reset_redirect": "/account/password-reset-complete"}, name="password_reset_confirm"),
    url(r'^password-reset-complete/$', auth_views.password_reset_complete,
        {"template_name": "account/password_reset_complete.html"}, name="password_reset_complete"),
    url(r'^my-information/$', views.myself, name="my_information"),
    url(r'^edit-my-information/$', views.myself_edit, name="edit_my_information"),
    url(r'^my-image/$', views.my_image, name = "my_image"),
] #相应的三个参数：正则表达式(表示是从浏览器中进行的网址匹配)， 映射后的响应方法，对应网页的标题（在其它地方可以用的超链接名字）