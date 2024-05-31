from django.shortcuts import render
from .models import Category


def main(request):
    categories = Category.objects.all()
    if not categories:
        categories = [
            {'name': 'Example Category 1'},
            {'name': 'Example Category 2'},
            {'name': 'Example Category 3'}
        ]
    return render(request, 'main.html', context={'categories': categories})
