from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^info/', 'apps.soya.views.info', name='info'),
	url(r'^(?P<id>\d+)/$', 'apps.soya.views.moreinfo', name='moreinfo'),
	url(r'^product/', 'apps.soya.views.product', name='product'),
	url(r'^zakaz/', 'apps.soya.views.zakazat', name='zakazat'),
	url(r'^zakazi/', 'apps.soya.views.zakazi', name='zakazi'),
    # Examples:
    # url(r'^$', 'shop.views.home', name='home'),
)