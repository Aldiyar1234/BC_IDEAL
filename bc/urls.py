from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from quiz.views import quizez, questions, university_view, homepage, major_group, major_detail, filters


urlpatterns = [
    path('admin/', admin.site.urls),
    path('1/', quizez),
    path('quizez/<int:pk>', questions),
    path('university/<str:url>', university_view),
    path('', homepage),
    path('university/<str:university>/majors', major_group),
    path('university/<str:university>/majors/<str:pk>', major_detail),
    path('search/',filters)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



