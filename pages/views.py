from django.shortcuts import render

# Create your views here.
TBA = [
		{"id": 1, "title": "First Announcement", "content": "This is the full content of the first announcement."},
		{"id": 2, "title": "Second Announcement", "content": "This is the full content of the second announcement."},
		{"id": 3, "title": "Third Announcement", "content": "This is the full content of the third announcement."},
]

def home(request):
	context = {
		'title': 'Home',
		'features': [
			'Django',
			'Templates',
			'Static Files'
		]
	}
	return render(request, 'home.html', context)

def about(request):
	return render(request, 'about.html', {'title': 'About'})

def announcement_list(request):
	return render(request, 'announcement_list.html', {"announcements": TBA})

def announcement(request, id):
    announcement = next((a for a in TBA if a["id"] == id), None)
    return render(request, 'announcement.html', {"announcement": announcement})