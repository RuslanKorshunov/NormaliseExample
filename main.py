import nltk

for dependency in ("brown", "names", "wordnet", "averaged_perceptron_tagger", "universal_tagset"):
    nltk.download(dependency)

from normalise import tokenize_basic, normalise


def tokenize(text):
    print(normalise(text, tokenizer=tokenize_basic, verbose=True))


def main():
    text = input("Enter text:")
    tokenize(text)


if __name__ == "__main__":
    main()
