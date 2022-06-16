from django.urls import path
from api.views import SkillList, SkillCreate, SkillView,ProjectList,ProjectCreate,ProjectCreate,PredictionView,SendEmailView,ContactCreate,ContactList




urlpatterns=[
    path('skills/', SkillList.as_view()),
    path('skills/create/', SkillCreate.as_view()),
    path('skills/<int:pk>/', SkillView.as_view()),
    path('projects/', ProjectList.as_view()),
    path('projects/create/', ProjectCreate.as_view()),
    path('projects/<int:pk>/', ProjectCreate.as_view()),
    path('predict', PredictionView.as_view()),
    path('email', SendEmailView.as_view()),
    path('contacts/create', ContactCreate.as_view()),
    path('contacts', ContactList.as_view()),
]