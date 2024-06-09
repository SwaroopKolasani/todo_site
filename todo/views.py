from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages

# import todo form and models

from .forms import todoForm
from .models import todo

###############################################


def index(request):

	item_list = todo.objects.order_by("-date")
	if request.method == "POST":
		form = todoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('todo')
	form = todoForm()

	page = {
		"forms": form,
		"list": item_list,
		"title": "TODO LIST",
	}
	return render(request, 'todo/index.html', page)


### function to remove item, it receive todo item_id as primary key from url ##
def remove(request, item_id):
	item = todo.objects.get(id=item_id)
	item.delete()
	messages.info(request, "item removed !!!")
	return redirect('todo')
