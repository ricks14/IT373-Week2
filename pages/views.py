from django.shortcuts import render

# Create your views here.
# Create your views here.
TBA = [
    {
        "id": 1,
        "title": "First Announcement, Creation",
        "content": (
            "We are excited to announce the launch of our new Announcement Website! "
            "This platform is designed to keep students, faculty, and the community informed "
            "about the latest news and updates. Over the next few weeks, we'll be rolling out "
            "new features, including improved navigation, a mobile-friendly interface, and a "
            "dedicated announcements section for upcoming events. "
            "Stay tuned for further updates, and thank you for supporting this project."
        )
    },
    {
        "id": 2,
        "title": "Second Announcement, Maintenance",
        "content": (
            "Our website maintenance schedule has been confirmed. "
            "Please be advised that the site will undergo scheduled maintenance this Saturday "
            "from 10:00 PM until 2:00 AM. During this time, certain features such as the announcement list "
            "and detail pages may be temporarily unavailable. We apologize for any inconvenience this may cause "
            "and appreciate your understanding as we continue to improve stability and performance. "
            "After maintenance, you can expect faster load times and better accessibility."
        )
    },
    {
        "id": 3,
        "title": "Third Announcement, Miscellaneous",
        "content": (
            "We are pleased to share that a new set of community-driven events has been added to our calendar. "
            "These events include workshops, student-led discussions, and online webinars designed to provide "
            "valuable skills and insights. Registration is free, but spaces are limited, so we encourage everyone "
            "to register early. Details about each event, including speakers, schedules, and requirements, "
            "can be found in the Announcements section. We look forward to your active participation!"
        )
    },
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