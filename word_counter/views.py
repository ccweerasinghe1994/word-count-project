import operator

from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    wordList = fulltext.split()

    wordDictionary = {}

    for word in wordList:
        if word in wordDictionary:
            wordDictionary[word] += 1
        else:
            wordDictionary[word] = 1

    sortedWords = sorted(wordDictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html',
                  {'fulltext': fulltext, 'wordDictionary': sortedWords, 'count': len(wordList)})


def about(request):
    return render(request, 'about.html')
