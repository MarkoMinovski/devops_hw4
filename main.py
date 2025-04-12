
if __name__ == "__main__":
    words = ["ox", "twilight", "glimmering", "quasar", "spaghettification", "macedonia", "france"]
    longest_len = 0
    longest_word = words[0]

    for word in words:
        if len(word) > longest_len:
            longest_word = word
            longest_len = len(word)

    print(longest_word)
