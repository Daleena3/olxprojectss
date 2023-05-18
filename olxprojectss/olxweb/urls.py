from django.urls import path
from olxweb import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns= [
    path("signup",views.Signupview.as_view(),name="register"),
    path("",views.LoginView.as_view(),name="signin"),
    path("home",views.Indexview.as_view(),name="home"),
    path("signout",views.Signoutview.as_view(),name="signout"),
    path("profile/add",views.Userprofilecreateview.as_view(),name="profile-add"),
    path("profile",views.Profiledetailview.as_view(),name="profile-detail"),
    path("profile/<int:id>/change",views.Profileupdateview.as_view(),name="profile-change"),
    path("product/<int:id>",views.ProductDetailView.as_view(),name="product-detail"),
    path("productadd/",views.productAddView.as_view(),name="product-add"),
    path("products/<int:id>/carts/add",views.AddtocartView.as_view(),name="cart-add"),
    path("customer/carts/all",views.CartListView.as_view(),name="cart-list"),
    path("questions/<int:id>/add",views.AddquestionView.as_view(),name="add-question"),
    path("questions/<int:id>/answer/add",views.AddanswerView.as_view(),name="add-answer"),
    path("customer/order/all",views.OrderView.as_view(),name="order-list"),
    path("carts/<int:id>/change",views.CartRemoveview.as_view(),name="cart-change"),







]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)