from django.conf import settings
from django.conf.urls import url, include

from seimas.website import admin
from seimas.website import views

slug = r'?P<slug>[a-z0-9-]+'

urlpatterns = [
    url(r'^$', views.topic_list, name='topic-list'),
    url(r'^temos/nauja-tema/$', views.topic_form, name='topic-create'),
    url(r'^temos/(%s)/$' % slug, views.topic_details, name='topic-details'),
    url(r'^temos/(%s)/add-voting/$' % slug, views.voting_form, name='add-voting'),
    url(r'^temos/(%s)/add-news/$' % slug, views.news_form, name='add-news'),
]

urlpatterns += [
    url(r'^accounts/', include('seimas.accounts.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('seimas.prototype.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(url(r'^__debug__/', include(debug_toolbar.urls)))
