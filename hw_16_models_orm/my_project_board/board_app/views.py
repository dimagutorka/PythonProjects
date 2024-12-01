from django.shortcuts import render
from board_app.models import Category, Ad, Comment, User
from django.http import HttpResponse
from datetime import datetime, timedelta

#
# def ads_for_last_month(request):
# 	thirty_days = datetime.now() - timedelta(days=30)
# 	all_ads_last_month = Ad.objects.filter(created_at__gte=thirty_days)
# 	return HttpResponse(all_ads_last_month)
#
#
# def ads_per_category(request):
# 	ads_in_category = Ad.objects.filter(category_id=1).filter(is_active=True)
# 	return HttpResponse(ads_in_category)
#
#
# def comments_in_ads(request):
# 	ads_id = [ad_id.pk for ad_id in Ad.objects.filter(is_active=True)]
# 	comment_for_ad = {i: len(Comment.objects.filter(ad_id=i)) for i in ads_id}
# 	return HttpResponse(comment_for_ad.items())
#
#
# def ads_per_user(request):
# 	all_users_ads = Ad.objects.filter(user_id=4)
# 	amount_of_ads = len(all_users_ads)
# 	return HttpResponse(amount_of_ads)
