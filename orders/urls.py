from django.urls import path
from .views import  ListUsers, RetrieveUser, CreateCategory, CreateOrder, RetrieveDeleteCategory, GetCategoryForOrder
 



urlpatterns = [
    path('category/<int:pk>/', GetCategoryForOrder.as_view(), name='get_categories'),
    path('users/', ListUsers.as_view(), name='get_users'),
    path('users/<int:pk>/', RetrieveUser.as_view(), name='retrieve_user'),
    path('create/', CreateOrder.as_view(), name='create_orders'),
    path('create/categories', CreateCategory.as_view(), name='create_categories'),
    path('delete/categories/<int:pk>', RetrieveDeleteCategory.as_view(), name='delete_categories'),
]