from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

#Router object
router=DefaultRouter()

#register router
router.register('blogs',views.BlogViewSet)
router.register('comments',views.CommentsViewSet)


urlpatterns = [
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls'))
]
