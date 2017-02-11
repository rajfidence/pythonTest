def break_words(stuff):
	"""This function will break up the stuff."""
	words=stuff.split(' ')
	return words
def sort_words(words):
	"""sort the words."""
	return sorted(words)
def print_first_word(words):
	"""prnt the first word."""
	word = words.pop(0)
	print word
def print_last_word(words):
	word = words.pop(-1)
	print word
def sort_sentence(words):
	words = break_words(words)
	return sort_words(words)
def print_first_and_last(sentence):
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)
def print_first_and_last_sorted(sentence):
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
