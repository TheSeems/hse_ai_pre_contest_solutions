def log_plagiat_check():
    def decorator(func):
        def wrapper(word1: str, word2: str):
            result = func(word1, word2)
            print(f"Check '{word1}' vs '{word2}' -> {result}")
            return result

        return wrapper

    return decorator


@log_plagiat_check()
def is_plagiat(word1: str, word2: str) -> bool:
    word1_letters = set(word1.lower())
    word2_letters = set(word2.lower())
    return len(word2_letters - word1_letters) <= 1


if __name__ == "__main__":
    with open("words.txt", "rt") as fd:
        for line in fd.readlines():
            word1, word2 = line.strip().split(maxsplit=2)
            is_plagiat(word1, word2)
