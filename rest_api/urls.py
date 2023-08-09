from django.urls import path, include
from .views import PostView, posts_detail, genericApiView, PostViewSet, PostsAPIVew, postDetailAPIView
from rest_framework import routers


router = routers.SimpleRouter()

router.register('posts', PostViewSet, basename='posts')

urlpatterns = [
    # path('posts/', PostView),
    # path('details/<int:pk>', posts_detail)

    #  path('postsApiView/', PostsAPIVew.as_view()),
    #  path('detailsApiView/<int:pk>', postDetailAPIView.as_view())
    path('genericApiView/<int:id>/', genericApiView.as_view()),
    path('', include(router.urls)),
]
