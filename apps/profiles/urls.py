from django.urls import path


from . views import (
    AgentListAPIView,
    GetProfileAPIView, 
    UpdateProfileAPIView,
    TopAgentListAPIView
)


urlpatterns = [
    path('me/', GetProfileAPIView.as_view(), name="get-profile"),
    path("update/<str:username>/",UpdateProfileAPIView.as_view(), name="update-profile"),
    path("agents/all/", AgentListAPIView.as_view(), name="all-agents"),
    path("top-agents/all/", TopAgentListAPIView.as_view(), name="all-top-agents"),
] 
 