from rest_framework.routers import SimpleRouter

from goods.api import views

router = SimpleRouter()
router.register("catalog", views.CatalogViewSet)
router.register("trade_name", views.TradeNameViewSet)
router.register("maker", views.MakerViewSet)
router.register("packing", views.PackingViewSet)
router.register("unit", views.UnitViewSet)
router.register("original_packing", views.OriginalPackingViewSet)
router.register("dosage_packing", views.DosagePackingViewSet)
router.register("good", views.GoodViewSet)
router.register("good_image", views.GoodImageViewSet)


app_name = "goods-api"
urlpatterns = router.urls
