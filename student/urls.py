from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views

urlpatterns = [
    path('student/',StudentAPI.as_view()),
    path('log/',LogAPI.as_view()),
    path('tasks/',TaskAPI.as_view()),
    path('overduetask/',OverdueTaskAPI.as_view()),
    path('members/',MembersAPI.as_view()),
    path('memberdetails/<int:memberId>/',MemberDetailsAPI.as_view()),
    path('loans/<int:memberid>/',LoanDetailsAPI.as_view()),
    path('api-token-auth/', views.obtain_auth_token)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)