from django.contrib import admin
from django.urls import path
from .views import TodoListView, WelcomeView  # Ensure the correct import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', WelcomeView.as_view(), name='welcome'),
    path('todos/', TodoListView.as_view(), name='todo-list'),  # Use the correct view name
]
