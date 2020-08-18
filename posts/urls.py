from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url(r'^$',views.index,name = 'index'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^image/(\d+)',views.image,name='image'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^new/post/$', views.new_post, name='new-post'),
    url(r'^profile/update$',views.update_profile,name='update-profile'),
    url(r'^comment/(\d+)/',views.new_comment,name='new-comment')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)