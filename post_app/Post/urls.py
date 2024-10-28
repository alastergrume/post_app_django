from django.urls import path
from . import views

urlpatterns = [
    # Обращается к функции home(), которая лежит в файле views
    # '' - это обозначает, кто обращение будет при входе на стартовую страницу
    path('', views.home, name='home'),

    # Для отображения новой формы
    path('post/create/', views.create_post, name='post-create'),

    # Следующая страница
    path('about/', views.about, name='about'),

    # Для проверки соединения
    # Здесь ссылка должна содержать цифру один
    path('end/', views.end, name='end'),
]
