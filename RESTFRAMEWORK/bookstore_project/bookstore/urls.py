from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from .views import PerfumeViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'perfumes', PerfumeViewSet)

urlpatterns = router.urls