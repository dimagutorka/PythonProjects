class MessageSender:
	"""Abstract class for sending messages."""

	def send_message(self, message: str) -> None:
		"""Send a message.

		Args:
			message (str): The message to be sent.
		"""
		pass


class SMSService:
	"""Class for sending SMS messages."""

	def send_sms(self, phone_number: str, message: str) -> None:
		"""Sends an SMS to the specified phone number.

		Args:
			phone_number (str): The phone number to send the SMS to.
			message (str): The message content.
		"""
		print(f"Send SMS to {phone_number}: {message}")


class EmailService:
	"""Class for sending email messages."""

	def send_email(self, email_address: str, message: str) -> None:
		"""Sends an email to the specified email address.

		Args:
			email_address (str): The email address to send the email to.
			message (str): The message content.
		"""
		print(f"Send Email to {email_address}: {message}")


class PushService:
	"""Class for sending push notifications."""

	def send_push(self, device_id: str, message: str) -> None:
		"""Sends a push notification to the specified device.

		Args:
			device_id (str): The device ID to send the push notification to.
			message (str): The message content.
		"""
		print(f"Send Push-notification to {device_id}: {message}")


class SMSAdapter(MessageSender):
	"""Adapter class for SMS service."""

	def __init__(self, old_sms_sender: SMSService, phone_number: str) -> None:
		"""Initializes the SMS adapter.

		Args:
			old_sms_sender (SMSService): The SMS service instance.
			phone_number (str): The phone number to send SMS to.
		"""
		self.old_sms_sender = old_sms_sender
		self.phone_number = phone_number

	def send_message(self, message: str) -> None:
		"""Sends a message via SMS.

		Args:
			message (str): The message to be sent.
		"""
		self.old_sms_sender.send_sms(self.phone_number, message)


class EmailAdapter(MessageSender):
	"""Adapter class for Email service."""

	def __init__(self, old_email_sender: EmailService, email_address: str) -> None:
		"""Initializes the Email adapter.

		Args:
			old_email_sender (EmailService): The email service instance.
			email_address (str): The email address to send the email to.
		"""
		self.old_email_sender = old_email_sender
		self.email_address = email_address

	def send_message(self, message: str) -> None:
		"""Sends a message via Email.

		Args:
			message (str): The message to be sent.
		"""
		self.old_email_sender.send_email(self.email_address, message)


class PushAdapter(MessageSender):
	"""Adapter class for Push notification service."""

	def __init__(self, old_push_sender: PushService, device_id: str) -> None:
		"""Initializes the Push adapter.

		Args:
			old_push_sender (PushService): The push notification service instance.
			device_id (str): The device ID to send the push notification to.
		"""
		self.old_push_sender = old_push_sender
		self.device_id = device_id

	def send_message(self, message: str) -> None:
		"""Sends a message via Push notification.

		Args:
			message (str): The message to be sent.
		"""
		self.old_push_sender.send_push(self.device_id, message)


# Example usage
message = "Test message"

sms_service = SMSService()
email_service = EmailService()
push_service = PushService()

sms_adapter = SMSAdapter(sms_service, "+123456789")
email_adapter = EmailAdapter(email_service, "dima@gmail.com")
push_adapter = PushAdapter(push_service, "A-52")

# Sending messages
sms_adapter.send_message(message)
email_adapter.send_message(message)
push_adapter.send_message(message)
