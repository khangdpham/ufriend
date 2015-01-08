from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views

urlpatterns = patterns('',
	#url(r'^login/$','authen.views.login_user'),
	url(r'^login/$', 'django.contrib.auth.views.login'),
	url(r'^logout/$', 'django.contrib.auth.views.logout',
		{'next_page': 'home.views.index'}),
	url(r'^$','home.views.index'),
    url(r'^admin/', include(admin.site.urls)),
)
