from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from quiz.views import quizez, questions


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('aga/', TemplateView.as_view(template_name='agaaga/aga.html')),
    path('aga_first/', TemplateView.as_view(template_name='agaaga/aga_first.html')),
    path('1', quizez),
    path('quizez/<int:pk>', questions)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

