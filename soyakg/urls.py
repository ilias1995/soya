from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'apps.soya.views.base', name='base'),
    url(r'^login', 'apps.soya.views.login', name='login'),
	url(r'^soya/', include('apps.soya.urls')),
    # Examples:
    # url(r'^$', 'soyakg.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
