import random


CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'


def read_words(words_file):
    with open(words_file) as f:
        words = tuple([word.strip().capitalize() for word in f])
    return words


class CouponGenerator:
    def __init__(self):
        self.words = None
        self.random = random.Random()
        self.prefix = ''

    def random_seed(self, seed):
        self.random = random.Random(seed)

    def word_list(self, words_file):
        self.words = read_words(words_file)

    def set_prefix(self, prefix):
        self.prefix = prefix

    def random_words(self, amount):
        return self.random.choices(self.words, k=amount)

    def random_numbers(self, amount, digits=1):
        return [self.random.randrange(0, 10 ** digits) for _ in range(amount)]

    def random_chars(self, amount):
        return self.random.choices(CHARS, k=amount)

    def generate_coupon(self):
        #words = self.random_words(3)
        #nums = self.random_numbers(2, digits=1)
        chars = self.random_chars(6)
        return ''.join(chars)
        #return f'{self.prefix}{nums[0]}{nums[1]}{words[0]}{words[1]}{words[2]}'

