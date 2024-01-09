from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import GetReviewList, ReviewDtl

urlpatterns = [
    path('review/', GetReviewList.as_view()),
    path('review/<int:pk>/', ReviewDtl.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

