from django.urls import path
from reviewsyetem import views



urlpatterns = [
    path("", views.home, name="home"),
    path("restaurant/<int:restaurant_id>/", views.details, name="details"),
    path("restaurant/<int:restaurant_id>/add_review/", views.add_review, name="add_review"),
    path("comment/<int:comment_id>/edit/", views.edit_comment, name="edit_comment"),
    path("comment/<int:comment_id>/delete/", views.delete_comment, name="delete_comment"),




    # Other URL patterns
]