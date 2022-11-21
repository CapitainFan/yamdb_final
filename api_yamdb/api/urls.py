from django.urls import include, path
from rest_framework import routers

from api.views import (CategoryViewSet, CommentViewSet,
                       ReviewViewSet, GenreViewSet,
                       SignupUserAPIView, TokenAuthApiView,
                       TitleViewSet, UserViewSet, )

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register(r'genres', GenreViewSet, basename='genre')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'titles', TitleViewSet)
router.register(
    r'titles/(?P<title_id>[\d]+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router.register(
    r'titles/(?P<title_id>[\d]+)/reviews/(?P<review_id>[\d]+)/comments',
    CommentViewSet,
    basename='comments',
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/token/', TokenAuthApiView.as_view()),
    path('v1/auth/signup/', SignupUserAPIView.as_view()),
]
