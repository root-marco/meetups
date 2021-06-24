from django.shortcuts import render


def index(request):
    meetups = [
        {'title': 'First meetup', 'location': 'New York', 'slug': 'first-meetup'},
        {'title': 'Second meetup', 'location': 'Paris', 'slug': 'second-meetup'},
        {'title': 'Third meetup', 'location': 'Brasil', 'slug': 'third-meetup'}
    ],
    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups,
    })


def meetup_details(request, meetup_slug):
    print(meetup_slug)
    selected_meetup = {
        'title': 'A First Meetup',
        'description': 'This is the first meetup!',
    }
    return render(request, 'meetups/meetup-detail.html', {
        'meetup_title': selected_meetup['title'],
        'meetup_description': selected_meetup['description'],
    })
