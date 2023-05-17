from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from quiz.views import quizez, questions, university_view, homepage, major_group, major_detail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('almau/', TemplateView.as_view(template_name='almau/almau.html')),
    path('almau_first/', TemplateView.as_view(template_name='almau/almau_first.html')),
    path('almau_first_one/', TemplateView.as_view(template_name='almau/almau_first_one.html')),
    path('almau_first_two/', TemplateView.as_view(template_name='almau/almau_first_two.html')),
    path('almau_first_three/', TemplateView.as_view(template_name='almau/almau_first_three.html')),
    path('almau_first_four/', TemplateView.as_view(template_name='almau/almau_first_four.html')),
    path('almau_first_five/', TemplateView.as_view(template_name='almau/almau_first_five.html')),
    path('almau_first_six/', TemplateView.as_view(template_name='almau/almau_first_six.html')),
    path('almau_first_seven/', TemplateView.as_view(template_name='almau/almau_first_seven.html')),
    path('almau_first_eight/', TemplateView.as_view(template_name='almau/almau_first_eight.html')),
    path('1/', quizez),
    path('quizez/<int:pk>', questions),
    path('university/<str:url>', university_view),
    path('', homepage),
    path('university/<str:university>/majors', major_group),
    path('university/<str:university>/majors/<str:pk>', major_detail)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



