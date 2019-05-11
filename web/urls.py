from django.conf.urls import include, url

from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
	
	
	# path('login/', auth_views.LoginViews.as_view(template_name='web/login.html'), name="login"),
	# path('logout/', auth_views.LoginViews.as_view(template_name='web/index.html'), name="logout"),
    ]
