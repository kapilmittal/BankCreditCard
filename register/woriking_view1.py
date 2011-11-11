
from django.template import RequestContext
from django.template import Context, loader
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from register.models import User, Card, Statement, BankDetails, EmploymentDetails, PersonalDetails


def index(request):
	#return HttpResponse("You're looking at ")
    return render_to_response('register/index.html',  context_instance=RequestContext(request))


def success(request):
	#return HttpResponse("ERROR ")
	
#render_to_response('register/success.html')	

#return HttpResponse("You're looking at ")
	try:
		uname = request.POST['USERNAME']
		pswd = request.POST['PASSWORD']
		#p = User.objects.create(username='hey')
		#p.save()
	except (KeyError):
		return HttpResponse("ERROR ")
	else:
	    
		p = User.objects.create(username=uname, password=pswd, verificationflag='Not Verified')
		p.save()
		pd = PersonalDetails(firstname='mugembo', user=p)
		pd.save()
		return render_to_response('register/success.html')
				