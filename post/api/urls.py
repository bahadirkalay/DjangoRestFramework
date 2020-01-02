
from django.urls import path,include

from post.api.views import (PostApiView,
                            PostDetailAPIView,
                            PostUpdateAPIView,
                            PostCreateAPIView,)
app_name = 'post'
urlpatterns = [
    path('list',PostApiView.as_view(), name='list'),
    path('detail/<slug>', PostDetailAPIView.as_view(), name= "detail"),
    path('update/<slug>', PostUpdateAPIView.as_view(), name="update"),
    path('create/', PostCreateAPIView.as_view(), name="create"),

]
