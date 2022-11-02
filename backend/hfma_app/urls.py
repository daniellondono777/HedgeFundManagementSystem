from django.urls import path
from hfma_app import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [

    path('auth/', obtain_auth_token),

    # ControlPanel 
    path('controlpanel/<int:pk>', views.get_control_panel),
    path('controlpanel/', views.get_control_panels),
    path('controlpanel/create/', views.ControlPanelCreateAPIView.as_view()),
    path('controlpanel/<int:pk>/update/', views.update_control_panel),
    path('controlpanel/<int:pk>/delete/', views.delete_control_panel),

    # Employee
    path('employee/', views.employee_list_view),
    path('employee/<int:pk>', views.employee_detail_view),
    path('employee/<int:pk>/update/', views.employee_update_view),
    path('employee/<int:pk>/delete/', views.employee_delete_view),
    path('employee/create/', views.employee_create_view),

    # Client
    path('client/', views.client_mixin_view),
    path('client/<int:pk>', views.client_mixin_view),
    path('client/create/', views.client_mixin_view),
    path('client/<int:pk>/update/', views.client_mixin_view),
    path('client/<int:pk>/delete/', views.client_mixin_view),

    # Asset
    path('asset/', views.asset_mixin_view),
    path('asset/<int:pk>', views.asset_mixin_view ),
    path('asset/create/', views.asset_mixin_view),
    path('asset/<int:pk>/update/', views.asset_mixin_view),
    path('asset/<int:pk>/delete/', views.asset_mixin_view)

   
]