from app_tests.forms import TaskForm
from datetime import date, timedelta
import pytest


class TestForms:
	def test_valid_form(self):
		form_data = {
			"title": "test 1",
			"description": "test 2",
			"due_date": date.today()
		}
		form = TaskForm(data=form_data)
		assert form.is_valid()

	def test_empty_form(self):
		form_data = {}
		form = TaskForm(data=form_data)
		assert not form.is_valid()
		assert 'title' in form.errors
		assert 'description' in form.errors
		assert 'due_date' in form.errors

	def test_invalid_form(self):
		form_data = {
			"title": "test 1",
			"description": "test 2",
			"due_date": date.today() - timedelta(days=1),
		}
		form = TaskForm(data=form_data)
		assert not form.is_valid()
		assert 'due_date' in form.errors
		assert form.errors['due_date'][0] == "Date must be in the future"

	def test_form_with_extra_fields(self):
		form_data = {
			"title": "test 1",
			"description": "test 2",
			"due_date": date.today(),
			'extra_field': 'extra_value'  # This field is not part of the form
		}
		form = TaskForm(data=form_data)
		assert form.is_valid(), "Extra fields in the data should be ignored by the form"
		assert 'extra_field' not in form.cleaned_data, "Extra fields should not be in cleaned_data"


@pytest.mark.parametrize(
	"data, expected",
	[
		(
				{
					"title": "test 1",
					"description": "test 2",
					"due_date": date.today()
				},
				True
		),
		(
				{
					"title": "test 1",
					"due_date": date.today()
				},
				False
		),
		(
				{
					"title": "test 1",
					"description": "test 2",
					"due_date": date.today() - timedelta(days=1),
				},
				False
		),
		({
			 "title": "test 1",
			 "description": "test 2",
			 "due_date": date.today(),
			 'extra_field': 'extra_value'  # This field is not part of the form
		 },
		 True

		)

	]

)
def test_bulk_check(data, expected):
	form = TaskForm(data=data)
	assert form.is_valid() == expected
