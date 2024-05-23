from django.shortcuts import render

from datetime import date

all_posts = [       #lista postów, każdy post będzie słownikiem
    {
        "slug": "hiking-the-mountains",
        "image": "mountains.jpg",
        "author": "Maximilian",
        "date": date(2024, 5, 23),
        "title": "Mountain Hiking",
        "exerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "contnet": """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam dapibus erat vel justo vulputate laoreet. Sed sagittis justo sodales pulvinar blandit. Donec sit amet sagittis augue. Aenean euismod faucibus arcu, at porta justo hendrerit nec. Fusce commodo lorem nec leo pulvinar, et semper tortor pretium. Nunc viverra nisi eu justo facilisis, id viverra sapien commodo. Cras vulputate, urna sed condimentum finibus, nisl nunc imperdiet lorem, interdum placerat dolor leo ut justo. Aenean non nunc nulla. Integer convallis fermentum aliquet. Quisque laoreet libero a nulla condimentum lobortis. Proin rutrum libero tortor, a vehicula elit feugiat et. Nam eu magna ac dui vulputate molestie ac vel lorem. Aliquam ac sagittis risus, et placerat magna.
            
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam dapibus erat vel justo vulputate laoreet. Sed sagittis justo sodales pulvinar blandit. Donec sit amet sagittis augue. Aenean euismod faucibus arcu, at porta justo hendrerit nec. Fusce commodo lorem nec leo pulvinar, et semper tortor pretium. Nunc viverra nisi eu justo facilisis, id viverra sapien commodo. Cras vulputate, urna sed condimentum finibus, nisl nunc imperdiet lorem, interdum placerat dolor leo ut justo. Aenean non nunc nulla. Integer convallis fermentum aliquet. Quisque laoreet libero a nulla condimentum lobortis. Proin rutrum libero tortor, a vehicula elit feugiat et. Nam eu magna ac dui vulputate molestie ac vel lorem. Aliquam ac sagittis risus, et placerat magna.
            
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam dapibus erat vel justo vulputate laoreet. Sed sagittis justo sodales pulvinar blandit. Donec sit amet sagittis augue. Aenean euismod faucibus arcu, at porta justo hendrerit nec. Fusce commodo lorem nec leo pulvinar, et semper tortor pretium. Nunc viverra nisi eu justo facilisis, id viverra sapien commodo. Cras vulputate, urna sed condimentum finibus, nisl nunc imperdiet lorem, interdum placerat dolor leo ut justo. Aenean non nunc nulla. Integer convallis fermentum aliquet. Quisque laoreet libero a nulla condimentum lobortis. Proin rutrum libero tortor, a vehicula elit feugiat et. Nam eu magna ac dui vulputate molestie ac vel lorem. Aliquam ac sagittis risus, et placerat magna.
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "mountains.jpg",
        "author": "Maximilian",
        "date": date(2024, 5, 21),
        "title": "Mountain Hiking",
        "exerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "contnet": """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam dapibus erat vel justo vulputate laoreet. Sed sagittis justo sodales pulvinar blandit. Donec sit amet sagittis augue. Aenean euismod faucibus arcu, at porta justo hendrerit nec. Fusce commodo lorem nec leo pulvinar, et semper tortor pretium. Nunc viverra nisi eu justo facilisis, id viverra sapien commodo. Cras vulputate, urna sed condimentum finibus, nisl nunc imperdiet lorem, interdum placerat dolor leo ut justo. Aenean non nunc nulla. Integer convallis fermentum aliquet. Quisque laoreet libero a nulla condimentum lobortis. Proin rutrum libero tortor, a vehicula elit feugiat et. Nam eu magna ac dui vulputate molestie ac vel lorem. Aliquam ac sagittis risus, et placerat magna.
            
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam dapibus erat vel justo vulputate laoreet. Sed sagittis justo sodales pulvinar blandit. Donec sit amet sagittis augue. Aenean euismod faucibus arcu, at porta justo hendrerit nec. Fusce commodo lorem nec leo pulvinar, et semper tortor pretium. Nunc viverra nisi eu justo facilisis, id viverra sapien commodo. Cras vulputate, urna sed condimentum finibus, nisl nunc imperdiet lorem, interdum placerat dolor leo ut justo. Aenean non nunc nulla. Integer convallis fermentum aliquet. Quisque laoreet libero a nulla condimentum lobortis. Proin rutrum libero tortor, a vehicula elit feugiat et. Nam eu magna ac dui vulputate molestie ac vel lorem. Aliquam ac sagittis risus, et placerat magna.
            
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam dapibus erat vel justo vulputate laoreet. Sed sagittis justo sodales pulvinar blandit. Donec sit amet sagittis augue. Aenean euismod faucibus arcu, at porta justo hendrerit nec. Fusce commodo lorem nec leo pulvinar, et semper tortor pretium. Nunc viverra nisi eu justo facilisis, id viverra sapien commodo. Cras vulputate, urna sed condimentum finibus, nisl nunc imperdiet lorem, interdum placerat dolor leo ut justo. Aenean non nunc nulla. Integer convallis fermentum aliquet. Quisque laoreet libero a nulla condimentum lobortis. Proin rutrum libero tortor, a vehicula elit feugiat et. Nam eu magna ac dui vulputate molestie ac vel lorem. Aliquam ac sagittis risus, et placerat magna.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "mountains.jpg",
        "author": "Maximilian",
        "date": date(2024, 5, 26),
        "title": "Mountain Hiking",
        "exerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "contnet": """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam dapibus erat vel justo vulputate laoreet. Sed sagittis justo sodales pulvinar blandit. Donec sit amet sagittis augue. Aenean euismod faucibus arcu, at porta justo hendrerit nec. Fusce commodo lorem nec leo pulvinar, et semper tortor pretium. Nunc viverra nisi eu justo facilisis, id viverra sapien commodo. Cras vulputate, urna sed condimentum finibus, nisl nunc imperdiet lorem, interdum placerat dolor leo ut justo. Aenean non nunc nulla. Integer convallis fermentum aliquet. Quisque laoreet libero a nulla condimentum lobortis. Proin rutrum libero tortor, a vehicula elit feugiat et. Nam eu magna ac dui vulputate molestie ac vel lorem. Aliquam ac sagittis risus, et placerat magna.
            
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam dapibus erat vel justo vulputate laoreet. Sed sagittis justo sodales pulvinar blandit. Donec sit amet sagittis augue. Aenean euismod faucibus arcu, at porta justo hendrerit nec. Fusce commodo lorem nec leo pulvinar, et semper tortor pretium. Nunc viverra nisi eu justo facilisis, id viverra sapien commodo. Cras vulputate, urna sed condimentum finibus, nisl nunc imperdiet lorem, interdum placerat dolor leo ut justo. Aenean non nunc nulla. Integer convallis fermentum aliquet. Quisque laoreet libero a nulla condimentum lobortis. Proin rutrum libero tortor, a vehicula elit feugiat et. Nam eu magna ac dui vulputate molestie ac vel lorem. Aliquam ac sagittis risus, et placerat magna.
            
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam dapibus erat vel justo vulputate laoreet. Sed sagittis justo sodales pulvinar blandit. Donec sit amet sagittis augue. Aenean euismod faucibus arcu, at porta justo hendrerit nec. Fusce commodo lorem nec leo pulvinar, et semper tortor pretium. Nunc viverra nisi eu justo facilisis, id viverra sapien commodo. Cras vulputate, urna sed condimentum finibus, nisl nunc imperdiet lorem, interdum placerat dolor leo ut justo. Aenean non nunc nulla. Integer convallis fermentum aliquet. Quisque laoreet libero a nulla condimentum lobortis. Proin rutrum libero tortor, a vehicula elit feugiat et. Nam eu magna ac dui vulputate molestie ac vel lorem. Aliquam ac sagittis risus, et placerat magna.
        """
    }
]

def get_date(post):
    return post['date']

# Create your views here.

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html")

def post_detail(request, slug):
    return render(request, "blog/post-detail.html")