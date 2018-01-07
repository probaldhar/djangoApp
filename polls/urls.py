from django.urls import path

from . import views

# Namespacing URL names
app_name = 'polls'

urlpatterns = [

    # route for poll home
    path('', views.IndexView.as_view(), name='index'),

    # route for question detail page
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    # route for results page
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),

    # route for vote
    path('<int:question_id>/vote/', views.vote, name='vote'),
]