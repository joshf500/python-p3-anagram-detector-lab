class Anagram:

    def __init__(self, word):
        self.word = word
    # ["listen", "poison", "hello"]
    #takes in a word_list that must be a list datatype and returns a list datatype
    def match(self, word_list: list) -> list:
    #declares empty matched_words array
        matched_words = []
    # for each element in the inputted word_list array, add it to the matched_words array if
    # the sorted version of it matches the sorted version of the initially inputted self.word
        for word in word_list:
            matched_words.append(word) if sorted(word) == sorted(self.word) else None
        return matched_words