from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
	return render(request, 'home.html')
def app(request):
	return render(request, 'app.html')
def credits(request):
	return render(request, 'credits.html')
def count(request):
	fulltext = request.GET['fulltext']
	wordlist = fulltext.split()
	worddict = {}
	for word in wordlist:
		if word in worddict:
			worddict[word] += 1
		else:
			worddict[word] = 1
	sortedwords = sorted(worddict.items(), key = operator.itemgetter(1), reverse = True)
	return render(request, 'count.html', {'fulltext':fulltext, 'count': len(wordlist), 'sortedwords':sortedwords})