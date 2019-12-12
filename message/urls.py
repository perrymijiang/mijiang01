from django.urls import path
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', MessageList.as_view(), name ='msg_list'),
    path('<int:pk>/', MessageDetail.as_view(), name ='msg_view'),
    path('create/', MessageCreate.as_view(), name ='msg_create'),
    path('delete/<int:pk>/', MessageDelete.as_view(), name ='msg_delete'),
    path('user/', include('django.contrib.auth.urls')),
]
