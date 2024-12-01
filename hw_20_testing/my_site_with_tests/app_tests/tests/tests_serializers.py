import pytest
from app_tests.serializers import TasksSerializer
from datetime import date, timedelta


class TestSerializers:

	def test_serializer_valid_data(self):
		valid_data = {
			"title": "test1",
			"description": "test1",
			"due_date": date.today() + timedelta(days=1)
		}

		serializer = TasksSerializer(data=valid_data)
		assert serializer.is_valid()
		assert serializer.validated_data['title'] == valid_data['title']

	def test_serializer_missing_field(self):
		invalid_data = {
			"description": "test1",
			"due_date": date.today() + timedelta(days=1)}

		serializer = TasksSerializer(data=invalid_data)

		assert not serializer.is_valid(), "Expected serializer to be invalid when title is missing"
		assert 'title' in serializer.errors

	def test_serializer_due_data_in_past(self):
		invalid_data = {
			"title": "test1",
			"description": "test1",
			"due_date": date.today() - timedelta(days=1)
		}

		serializer = TasksSerializer(data=invalid_data)

		assert not serializer.is_valid()
		assert 'due_date' in serializer.errors
		assert serializer.errors['due_date'][0] == "Due date must be in the future."


@pytest.mark.parametrize(
	"data, expected",
	[
		(
				{
					"title": "test1",
					"description": "test1",
					"due_date": date.today() + timedelta(days=1)
				},
				True
		),
		(
				{
					"description": "test1",
					"due_date": date.today() + timedelta(days=1)},
				False
		),
		(
				{
					"title": "test1",
					"description": "test1",
					"due_date": date.today() - timedelta(days=1)
				},
				False

		)

	]

)
def test_bulk_serializers(data, expected):
	serializer = TasksSerializer(data=data)
	assert serializer.is_valid() == expected


def test_valid_serializer_with_user(new_user):
	valid_data = {
			"title": "test1",
			"description": "test1",
			"due_date": date.today() + timedelta(days=1),
			"user": new_user
		}

	serializer = TasksSerializer(data=valid_data)
	assert serializer.is_valid()