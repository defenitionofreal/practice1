from ..users import apiviews
from rest_framework import routers

app_name = 'users'

router = routers.DefaultRouter()
router.register(r'certificate', apiviews.СertificateViewSet, basename='certificate')
router.register(r'jwt-token', apiviews.JwtTokenViewSet, basename='jwt-token')
router.register(r'nonce', apiviews.NonceViewSet, basename='nonce')

urlpatterns = [

]
urlpatterns += router.urls