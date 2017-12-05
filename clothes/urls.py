from django.conf.urls import url
from clothes import views

urlpatterns = [
    url(r'^clothes/outfit/(?P<gender>.+)/page/(?P<page>.+)/$', views.OutfitPage.as_view()),
    url(r'^outfititems/(?P<pk>[0-9]+)/$', views.OutfitItemsDetail.as_view()),
    url(r'^clothes/$', views.OutfitList.as_view()),
    url(r'^clothes/(?P<pk>[0-9]+)/$', views.OutfitDetail.as_view()),
    url(r'^clothes/items/$', views.ItemList.as_view()),
    url(r'^clothes/items/(?P<pk>[0-9]+)/$', views.ItemDetail.as_view()),
    url(r'^clothes/itemimg/$', views.ItemImgList.as_view()),
    url(r'^clothes/itemimg/(?P<pk>[0-9]+)/$', views.ItemImgDetail.as_view()),



]