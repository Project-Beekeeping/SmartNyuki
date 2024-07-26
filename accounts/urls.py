from django.urls import path
from django.conf import settings as st
from .views import signup
from .views import signin
from .views import dashboard
from .views import hives
from .views import subscription
from .views import profile, profile1
from .views import save_fcm_token
from .views import logout
from .views import settings, firebase_messaging_sw_js
from .views import password_reset
from .views import send_test_notification, send_notification, send_notification_view
from .import views
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('home/', views.home, name='home'),
    path("signup/", signup, name="signup"),
    path('signin/', signin, name='signin'),
    path('dashboard/', dashboard, name='dashboard'),
    path('hives/', hives, name='hives'),
    path('subscription/', subscription, name='subscription'),
    path('profile/', profile, name='profile'),
    path('profile1/', profile1, name='profile1'),
    path('settings/', settings, name='settings'),
    path('logout/', logout, name='logout'),
    path('reset_password/', views.password_reset, name='reset_password'),
    path('save-token/', views.save_token, name='save_token'),
    path('api/initiate_payment/', views.initiate_payment, name='initiate_payment'),
    path('send-test-notification/', views.send_test_notification, name='send_test_notification'),
    path('send-notification/', views.send_notification, name='send_notification'),
    path('send-notification-view/', views.send_notification_view, name='send_notification_view'),
    path('firebase-messaging-sw.js', views.firebase_messaging_sw_js, name='firebase-messaging-sw.js'),
    path('save-fcm-token/', save_fcm_token, name='save_fcm_token'),
] 
