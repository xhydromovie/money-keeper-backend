from rest_framework import routers
from collection import api_views as collection_views

router = routers.DefaultRouter()
router.register(r'collections', collection_views.CollectionViewset)
