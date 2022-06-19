from django.contrib import admin
from django.urls import path,include
from Api import views
from rest_framework.routers import DefaultRouter
from knox import views as knox_views
from Api.views import RegisterAPI
from Api.views import LoginAPI
from Api.views import TeacherLoginAPI
from django.conf.urls.static import static
from django.conf import settings



routers=DefaultRouter()
routers.register('teacher',             views.TeacherViewset,basename='teacher')
routers.register('student',             views.StudentViewset,basename='student')
routers.register('search_student',      views.SearchClassStudentsViewset,basename='search_student')
routers.register('class',               views.ClassViewset,basename='class')
routers.register('quiz',                views.QuizViewset,basename='quiz')
routers.register('post_quiz',           views.PostQuizViewset,basename='post_quiz')
routers.register('result',              views.ResultViewset,basename='result')
routers.register('post_result',         views.PostResultViewset,basename='post_result')
routers.register('assignment_two',      views.AssignmentViewset,basename='assignment_two')
routers.register('post_assignment_two', views.PostAssignmentViewsetTwo,basename='post_assignment_two')
routers.register('post_assignment',     views.PostAssignmentViewset,basename='post_assignment')
routers.register('notifications',       views.NotificationViewset,basename='notifications')
routers.register('contact',             views.ContactViewsetTwo,basename='contact')
urlpatterns = [

    path('admin/',                          admin.site.urls),
    path('api/',                            include(routers.urls),),
    path('api/update_assignment/<int:pk>/', views.up_assign),
    path('api/update_quiz/<int:pk>/',       views.up_quiz),
    ##knox Authenticaation
    path('api/register/',                   RegisterAPI.as_view(), name='register'),
    path('api/login/',                      LoginAPI.as_view(), name='login'),
    path('api/teacherlogin/',               TeacherLoginAPI.as_view(), name='teacherlogin'),
    path('api/logout/',                     knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/',                  knox_views.LogoutAllView.as_view(), name='logoutall'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
