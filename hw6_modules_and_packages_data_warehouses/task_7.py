class MessageSender:
	def send_message(self, message: str):
		pass


class SMSService:
	def send_sms(self, phone_number, message):
		print(f"Send SMS on {phone_number}: {message}")


class EmailService:
	def send_email(self, email_address, message):
		print(f"Send Email on {email_address}: {message}")


class PushService:
	def send_push(self, device_id, message):
		print(f"Send Push-notification on {device_id}: {message}")


class SMSAdapter(MessageSender):
	def __init__(self, old_sms_sender, phone_number):
		self.old_sms_sender = old_sms_sender
		self.phone_number = phone_number

	def send_message(self, message: str):
		self.old_sms_sender.send_sms(self.phone_number, message)


class EmailAdapter(MessageSender):
	def __init__(self, old_email_sender, email_address):
		self.old_email_sender = old_email_sender
		self.email_address = email_address

	def send_message(self, message: str):
		self.old_email_sender.send_email(self.email_address, message)


class PushAdapter(MessageSender):
	def __init__(self, old_push_sender, device_id):
		self.old_push_sender = old_push_sender
		self.device_id = device_id

	def send_message(self, message: str):
		self.old_push_sender.send_push(self.device_id, message)


message = "Test message"

sms_service = SMSService()
email_service = EmailService()
push_service = PushService()

sms_adapter = SMSAdapter(sms_service, "+123456789")
email_adapter = EmailAdapter(email_service, "dima@gmail.com")
push_adapter = PushAdapter(push_service, "A-52")

sms_adapter.send_message(message)
email_adapter.send_message(message)
push_adapter.send_message(message)
