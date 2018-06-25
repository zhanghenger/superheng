"""py URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . views1 import views,huiyuanviews,fenlieviews

urlpatterns = [
		



         # 后台de首页
	url(r'^$', views.index,name='myadmin_index'),


	  # 会员管理
    url(r'^user/add/$',huiyuanviews.add,name='myadmin_user_add'),
    url(r'^user/index/$',huiyuanviews.index,name='myadmin_user_list'),
    url(r'^user/delete/$',huiyuanviews.delete,name='myadmin_user_delete'),
    url(r'^user/edit/$',huiyuanviews.edit,name='myadmin_user_edit'),





      #商品分类管理
    url(r'^types/add$',fenlieviews.add,name='myadmin_types_add'),
    url(r'^types/index$',fenlieviews.index,name='myadmin_types_list'),
    url(r'^types/delete$',fenlieviews.add,name='myadmin_types_delete'),
    url(r'^types/edit$',fenlieviews.add,name='myadmin_types_edit'),
]
