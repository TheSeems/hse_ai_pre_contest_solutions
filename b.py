def is_plagiat(word1: str, word2: str) -> bool:
    word1_letters = set(word1.lower())
    word2_letters = set(word2.lower())
    return len(word2_letters - word1_letters) <= 1

if __name__ == "__main__":
    word1, word2 = input(), input()
    print(is_plagiat(word1, word2))