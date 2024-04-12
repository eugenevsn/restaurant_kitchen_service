from django.urls import path

from .views import (
    index,
    DishTypeListView,
    DishTypeDetailView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    assign_dish,
    DishListView,
    DishDetailView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    CookListView,
    CookDetailView,
    CookCreateView,
    CookUpdateView,
    CookDeleteView,
    AssignView,
)

urlpatterns = [
    path("", index, name="index"),
    path("dishtype/", DishTypeListView.as_view(), name="dishtype-list"),
    path("dishtype/<int:pk>/", DishTypeDetailView.as_view(), name="dishtype-detail"),
    path("dishtype/create/", DishTypeCreateView.as_view(), name="dishtype-create"),
    path("dishtype/<int:pk>/update/", DishTypeUpdateView.as_view(), name="dishtype-update"),
    path("dishtype/<int:pk>/delete/", DishTypeDeleteView.as_view(), name="dishtype-delete"),

    path("dish/", DishListView.as_view(), name="dish-list"),
    path("dish/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dish/create/", DishCreateView.as_view(), name="dish-create"),
    path("dish/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("dish/<int:pk>/assigned/", AssignView.as_view(), name="dish-assign"),
    path("dish/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),
    path("dish/<int:pk>/assign/", assign_dish, name="assign-dish"),

    path("cook/", CookListView.as_view(), name="cook-list"),
    path("cook/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("cook/create/", CookCreateView.as_view(), name="cook-create"),
    path("cook/<int:pk>/update/", CookUpdateView.as_view(), name="cook-update"),
    path("cook/<int:pk>/delete/", CookDeleteView.as_view(), name="cook-delete"),
]

app_name = "kitchen"
