class StringProcessor:
	def __init__(self, string : str):
		self.string = string

	def reverse_string(self):
		return self.string[::-1]

	def capitalize_string(self):
		return self.string.capitalize()

	def count_vowel(self):
		vowels = "aeiouAEIOU"
		count = sum(self.string.count(vowel) for vowel in vowels)
		return count



