from django.urls import path

from . import views


# "/" is -> /api/products/
urlpatterns = [
    path('', views.product_list_create_view),
    path('<int:pk>/update/', views.product_update_view),
    path('<int:pk>/delete/', views.product_destroy_view),
    path('<int:pk>/', views.product_detail_view)
]


#when it was all in one function-based view:
# urlpatterns = [
#     path('', views.product_alt_view),
#     path('<int:pk>/', views.product_alt_view),