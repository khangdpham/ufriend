from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from ufriend import settings
from django.contrib.auth import views


admin.autodiscover()
urlpatterns = patterns('',
	#url(r'^login/$','authen.views.login_user'),
	url(r'^login/$', 'django.contrib.auth.views.login',name='u_login'),
	url(r'^signup/$', 'authen.views.register',name='signup'),
	url(r'^logout/$', 'django.contrib.auth.views.logout',
		{'next_page': 'home.views.index'}),
	#url(r'^$','home.views.index',name='home'),
	url(r'^$','events.views.display_current_events',name='current_events'),
	url(r'^$','events.views.display_current_events',name='home'),
	url(r'^profile/$','user_profile.views.view_profile',name='profile'),
	url(r'^view/(?P<event_id>\w+)/$',
		'events.views.view_event',
		name='event_view'),
	url(r'^post_event/$','events.views.create',name='create_new_post'),
	url(r'^about/$','home.views.index',name='nav_about'),
	url(r'^contact/$','home.views.index',name='nav_contact'),
	url(r'^admin/', include(admin.site.urls)),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
