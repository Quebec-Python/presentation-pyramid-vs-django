from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('pyddit_app.views',
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'home', name="home"),
    url(r'^vote_up/(?P<hash_url>.+)$', 'vote_up', name="vote_up"),
    url(r'^vote_down/(?P<hash_url>.+)$', 'vote_down', name="vote_down"),
    url(r'^add_post$', 'add_post', name="add_post"),
    url(r'^post/(?P<hash_url>.+)$', 'get_post', name="get_post"),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
