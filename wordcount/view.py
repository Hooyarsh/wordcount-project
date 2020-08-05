from django.http import HttpResponse

from django.shortcuts import render

import operator



def home(request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

def hooyar(request):
	return HttpResponse('<h1>Admin = hooyar</h1>')

def count(request):
	TEXT = request.GET['TEXT']

	wordlist = TEXT.split()

	worddictionary = {}

	for word in wordlist:
		if word in worddictionary:
			#increase
			worddictionary[word] += 1
		else:
			#add
			worddictionary[word] = 1

	print(TEXT)

	sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

	return render(request, 'count.html',{'TEXT':TEXT, 'count':len(wordlist), 'sortedwords':sortedwords})