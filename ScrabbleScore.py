def makeScrabbleDict():
    d = {}
    d[1] = "AEIOULNSTR"
    d[2] = "DG"
    d[3] = "BCMP"
    d[4] = "FHVWY"
    d[5] = "K"
    d[8] = "JX"
    d[10] = "QZ"

    scoreDict = {}
    for k,v in d.items():
        for letter in v:
            scoreDict[letter] = k
    return scoreDict

def scoreWord(word):
    word = word.upper()
    sd = makeScrabbleDict()
    score = 0
    for letter in word:
        score += sd[letter]

    return score

print(scoreWord("lovely"))


# Note - add your code here if you completed the "Competency" option on the quiz
def topNWords(length, numWords):
    topscoringwords = {}
    with open("Scrabble.txt") as f:
        for line in f:
            word = line.strip()
            if len(word) == length:
                score = scoreWord(word)
                topscoringwords[word] = score
    sortedWords = sorted(topscoringwords.items(), key=lambda x: x[1], reverse=True)
    return sortedWords[:numWords]
print(topNWords(7, 10))
