from rest_framework import routers, urlpatterns
from .viewsets import tasksViewSet


router = routers.SimpleRouter()
router.register('tasks', tasksViewSet)

urlpatterns = router.urls