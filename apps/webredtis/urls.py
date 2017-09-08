from django.conf.urls import url, include
from apps.webredtis.views import inicio
from apps.webredtis.views import proyecto

urlpatterns = [ 
	url(r'^$', inicio, name='inicio'),
	url(r'^', proyecto, name='proyecto'),

	
]