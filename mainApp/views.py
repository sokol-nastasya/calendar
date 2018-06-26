from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Entry
from .forms import EntryForm

def index(request):
	return render(request, 'mainApp/index.html')

def calendar(request):
	entries = Entry.objects.filter(author = request.user)
	args = {'entries':entries}
	return render(request, 'mainApp/calendar.html', args)

def details(request, pk):
	entries = Entry.objects.get(id = pk)
	args = {'entries':entries}
	return render(request, 'mainApp/details.html', args)

def add(request):
	if request.method == 'POST':
		form = EntryForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			date = form.cleaned_data['date']
			descriptions = form.cleaned_data['descriptions']

			Entry.objects.create(
				name = name,
				author = request.user,
				date = date,
				descriptions = descriptions,
				).save()
			return HttpResponseRedirect('/calendar')
	else:
		form = EntryForm()
	return render(request, 'mainApp/add_form.html', {'form':form})


def delete(request, pk):
	if request.method == 'DELETE':
		entry = get_object_or_404(Entry, pk = pk)
		entry.delete()

	return HttpResponseRedirect('/')