from django.urls import path
from ..codes import apiviews
from rest_framework import routers

app_name = 'codes'

router = routers.DefaultRouter()
router.register(r'product', apiviews.ProductViewSet, basename='product')
router.register(r'marking-code', apiviews.MarkingCodeViewSet, basename='marking-code')

urlpatterns = [

]
urlpatterns += router.urls
