from django.urls import path\

from . import views

urlpatterns = {
    path("", views.starting_page, name="starting-page"),
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.post_detail, name="post-detail-page")    #slug concept - slug to koncowka adresu, sluyg transformer (slug: sprawdza, czy ta część, ostatnia część ścieżki ma taki format: xxx-xxx-xxxxxxx-xxxxxxxxxx-xxxx-xxxxxxx)
}