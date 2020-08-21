from django.urls import path


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:TITLE>", views.entryPage,name="entryPage"),
    path("search",views.search,name="search"),
    path("newpage",views.newPage,name="newPage"),
    path("editpage/<str:TITLE>",views.editPage,name="editPage"),
    path("randompage",views.randompage,name="randompage")
]
