from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from.views import HomePageView,CreatePostView

urlpatterns=[
    path('',HomePageView.as_view(),name='home'),
    path('post',CreatePostView.as_view(),name='add_post'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)