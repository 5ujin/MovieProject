from django.urls import path

from . import views


urlpatterns = [
    path('', views.review_list_create),
    path('<int:review_pk>/', views.review_detail_update_delete),
    path('<int:review_pk>/comments/', views.comment_create),
    path('comments/<int:comment_pk>/', views.comment_delete),
]
