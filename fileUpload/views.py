from django.shortcuts import render

from .forms import PersonForm
from .models import PersonPhoto
def home(request):
	form = PersonForm

	if request.method == 'POST':
		form = PersonForm(request.POST, request.FILES)
		if form.is_valid():
			person = form.save()
			files = request.FILES.getlist('photos')
			if files:
				for f in files:
					PersonPhoto.objects.create(person=person, photo=f)


	context = {
		'title': 'Multiple File Upload | Home',
		'form': form
	}
	return render(request, 'home.html', context)