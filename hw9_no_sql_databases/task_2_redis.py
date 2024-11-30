import redis
import time
import uuid


class UserSession:
	def __init__(self, redis_host='localhost', redis_port=6379):
		self.client = redis.Redis(host=redis_host, port=redis_port, db=0)

	def create_session(self, user_id):
		session_token = str(uuid.uuid4())  # Generate a unique session token
		login_time = time.time()  # Store the current time as login time

		session_data = {
			'user_id': user_id,
			'session_token': session_token,
			'login_time': login_time
		}

		self.client.hset(f'session:{user_id}', mapping=session_data)
		self.client.expire(f'session:{user_id}', 1800)

		return session_token

	def get_session(self, user_id):
		session_data = self.client.hgetall(f'session:{user_id}')

		if not session_data:
			return None  # Session not found

		# Decode byte values to strings and return as a dictionary
		return {key.decode('utf-8'): value.decode('utf-8') for key, value in session_data.items()}

	def delete_session(self, user_id):
		self.client.delete(f'session:{user_id}')

	def delete_after_wait(self, user_id):
		if self.client.ttl(f'session:{user_id}') > 0:
			time.sleep(self.client.ttl(f'session:{user_id}'))
			self.client.delete(f'session:{user_id}')


if __name__ == '__main__':
	session = UserSession()

	user_id = 2
	session_token = session.create_session(user_id)
	print(f'Session created for user {user_id}. Session token: {session_token}')

	session_data = session.get_session(user_id)
	print(f'Session data for user {user_id}: {session_data}')

	session_data_after_wait = session.delete_after_wait(user_id)
	print(f'Session data after waiting: {session_data_after_wait}')

	session.delete_session(user_id)
	print(f'Session deleted for user {user_id}.')


