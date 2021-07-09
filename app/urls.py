from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('details',views.details, name='details'),
    path('tags/<slug:tag_slug>/',views.TagIndexView.as_view(),name='tagdetails')
]