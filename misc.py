#!/usr/bin/python

def expansions(original, relatedWords):
    results = []
    strippedSentence = original.strip()
    words = strippedSentence.split(" ")
    if strippedSentence != "":
        firstWord = words[0]
        restOfSentence = " ".join(words[1:])
        subExpansions = expansions(restOfSentence, relatedWords)
        if len(subExpansions) > 0:
            for subExpansion in subExpansions:
                results.append(firstWord + " " + subExpansion)
                if firstWord in relatedWords:
                    for relatedWord in relatedWords[firstWord]:
                        results.append(relatedWord + " " + subExpansion)
        else:
            results.append(firstWord)
            if firstWord in relatedWords:
                for relatedWord in relatedWords[firstWord]:
                    results.append(relatedWord)
    return results

def main():
    original = "pictures of puppies"
    relatedWords = {"pictures": ["photos"], "puppies": ["dogs", "pets"]}
    for expansion in expansions(original, relatedWords):
        print expansion

if __name__ == '__main__':
    main()

