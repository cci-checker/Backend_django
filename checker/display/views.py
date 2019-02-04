from django.shortcuts import render
from django.template.response import TemplateResponse
from data_api.models import User
from data_api.models import checkoff_list, Checklist_item, Room
from django.http import HttpResponse
from django.utils import timezone



def displayfunction(request):
	data = User.objects.all();
	actual_data = checkoff_list.objects.all();
	print (data);
	print (actual_data);
	sent_list=actual_data[2].task_list.all();
	print (timezone.localtime(timezone.now()));
	#sometext="I am in baby";
	#return HttpResponse(sometext);

	#use .url to get the url of the stored image
	return TemplateResponse(request, 'page/index.html', { "actual_data" : actual_data });

# Create your views here.
