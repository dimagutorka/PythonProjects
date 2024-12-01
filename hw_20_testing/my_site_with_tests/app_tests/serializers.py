from rest_framework import serializers
from app_tests.models import Tasks
from datetime import date


class TasksSerializer(serializers.ModelSerializer):
	title = serializers.CharField(max_length=100, required=True)
	description = serializers.CharField(max_length=100, required=True)
	due_date = serializers.DateField()

	class Meta:
		model = Tasks
		fields = '__all__'

	def validate_due_date(self, value):
		if value < date.today():
			raise serializers.ValidationError("Due date must be in the future.")
		return value
