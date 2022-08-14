from django.urls import path

from . import views


urlpatterns = [
    # path("society/<str:pk>", views.SocietyDetailView.as_view()),
    # path("education/<str:pk>", views.EducationDetailView.as_view()),
    path("news/<str:pk>", views.NewsDetailView.as_view()),
    # path("event/<str:pk>", views.EventDetailView.as_view()),
    # path("protocols/<str:pk>", views.ProtocolsDetailView.as_view()),

    path("<str:language>/education/<str:category>", views.EducationNavigationView.as_view()),
    path("<str:language>/society/<str:category>", views.SocietyNavigationView.as_view()),
    path("<str:language>/protocols/<str:category>", views.ProtocolsNavigationView.as_view()),
    path("<str:language>/events/<str:category>", views.EventNavigationView.as_view()),

    path("<str:language>/news/", views.NewsListView.as_view()),

    path("<str:language>/index/<str:category>", views.IndexNavigationView.as_view()),

    path("<str:language>/society/", views.SocietyCategoriesView.as_view()),
    path("<str:language>/education/", views.EducationCategoriesView.as_view()),
    path("<str:language>/protocols/", views.ProtocolsCategoriesView.as_view()),
    path("<str:language>/events/", views.EventCategoriesView.as_view()),

    path("<str:language>/search/<str:search>", views.SearchDetailView.as_view(), name='search'),
]
