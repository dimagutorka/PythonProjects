from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from users.views import registration_view, login_view, home, user_profile, logout_view, update_user_profile, change_password_view, no_account

urlpatterns = [
	path('registration/', registration_view, name='registration'),
	path('login/', login_view, name='login'),
	path('logout/', logout_view, name='logout'),
	path('home/', home, name='home'),
	path('profile/', user_profile, name='profile'),
	path('no_account/', no_account, name='no_account'),
	path('profile_update/', update_user_profile, name='profile_update'),
	path('change_password/', change_password_view, name='change_password'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
