from django.urls import path, include
from rest_framework import DefaultRouter
from API.users import views as userViews

router = DefaultRouter()
router.register(r'users', userViews.UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]