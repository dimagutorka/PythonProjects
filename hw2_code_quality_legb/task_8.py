def create_user_settings():

	settings = {
		'theme': 'default',
		'language': 'en',
		'notifications': True
	}

	def manage_settings(setting_name=None, value=None):
		if setting_name is None:
			return settings
		elif value is None:
			return settings.get(setting_name, 'Setting not found')
		else:
			settings[setting_name] = value
			return f"Setting '{setting_name}' updated to '{value}'"

	return manage_settings


user_settings = create_user_settings()
print(user_settings())
print(user_settings('theme'))
print(user_settings('theme', 'Christmas'))
print(user_settings('language', 'zh'))
print(user_settings('theme'))
print(user_settings())
