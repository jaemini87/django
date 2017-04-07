from django.conf.urls import url
from . import views
urlpatterns = [
#url(r'^$', views.current_datetime ,name='current_datetime'),
#url(r'^$', views.test_matplotlib ,name='test_matplotlib'),
#url(r'^admins/', views.post_list_admin ,name='post_list_admin'),
url(r'^$', views.top ,name='top'),
url(r'^picks$',     views.picks ,       name='picks'),
url(r'^tk$', views.tk_top ,name='tk_top'),
url(r'^tk_picks$',     views.tk_picks ,       name='tk_picks'),
#url(r'^$', views.simple ,name='simple'),
#url(r'^$', views.gen_graph ,name='gen_graph'),
    ]

