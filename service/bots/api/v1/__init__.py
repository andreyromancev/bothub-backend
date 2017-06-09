from rest_framework import routers
from .bot_profile import BotProfileViewSet

router = routers.DefaultRouter()
router.register(r'bots', BotProfileViewSet)

urlpatterns = router.urls
