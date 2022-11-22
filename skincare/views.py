from django.shortcuts import render
from .models import Issue
from django.http import JsonResponse
from django.core import serializers
import json
# Create your views here.


def issue_search(request):
    if request.method == "POST":
        issue_id = request.POST['issueselect']
        issue = Issue.objects.get(id=issue_id)
        return render(request, 'skin_care.html', {'issue': issue})
    return render(request, 'skin_care.html', {})


def skin_issues(request):
    data = request.POST['skin_type']
    if data == 'oily':
        skin_type = 'OILY SKIN'
    elif data == 'normal':
        skin_type = 'NORMAL SKIN'
    elif data == 'dry':
        skin_type = 'DRY SKIN'
    issues = Issue.objects.filter(skin_type=skin_type)
    data = serializers.serialize('json', issues, fields=('name', 'id'))
    return JsonResponse({'issuess': data})
