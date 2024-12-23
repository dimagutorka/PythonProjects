from django.urls import path
from users.views import *


app_name = "users"
urlpatterns = [
	path('registration/', registration_view, name='registration'),
	path('login/', login_view, name='login'),
	path('logout/', logout_view, name='logout'),
	path('profile/<int:user_id>', profile, name='profile'),

]