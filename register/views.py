
from django.template import RequestContext
from django.template import Context, loader
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from register.models import User, Card, Statement, BankDetails, EmploymentDetails, PersonalDetails


def index(request):
    return render_to_response('register/index.html',  context_instance=RequestContext(request))


def process(request):
	try:
		ld_uname = request.POST['USER_NAME']
		ld_pswd = request.POST['PASSWORD']
		
		pd_firstname = request.POST['FIRST_NAME']
		pd_lastname = request.POST['LAST_NAME']
		pd_gender = request.POST['GENDER']
		pd_education = request.POST['EDUCATION']
		pd_fathername = request.POST['FATHER_NAME']
		pd_mothername = request.POST['MOTHER_NAME']
		pd_currentaddress = request.POST['CURRENT_ADDRESS']
		pd_city = request.POST['PD_CITY']
		pd_pincode = request.POST['PD_PINCODE']
		pd_permanentaddress = request.POST['PERMANENT_ADDRESS']
		pd_telephone = request.POST['TELEPHONE']
		pd_mobile = request.POST['MOBILE']

		ed_companytype = request.POST['COMPANY_TYPE']
		ed_designation = request.POST['DESIGNATION']
		ed_income = request.POST['INCOME']
		ed_workyears = request.POST['WORK_YEARS']
		ed_name = request.POST['NAME']
		ed_officeaddress = request.POST['OFFICE_ADDRESS']
		ed_city = request.POST['ED_CITY']
		ed_pincode = request.POST['ED_PINCODE']
		ed_emailid = request.POST['EMAIL_ID']
				
		bd_account_number = request.POST['ACCOUNT_NUMBER']
		bd_bankname = request.POST['BANK_NAME']
		bd_branch_address = request.POST['BRANCH_ADDRESS']
		bd_account_type = request.POST['ACCOUNT_TYPE']
	
		cd_cardtype = request.POST['CARD_TYPE']

	except (KeyError):
		return HttpResponse("ERROR ")
	else:
		usr = User.objects.create(user_name=ld_uname, password=ld_pswd, verification_flag='Not Verified')
		usr.save()

		pd = PersonalDetails(first_name=pd_firstname, last_name=pd_lastname, gender=pd_gender, education=pd_education, father_name=pd_fathername, mother_name=pd_mothername, current_address=pd_currentaddress, city=pd_city, pincode=pd_pincode, permanent_address=pd_permanentaddress, telephone=pd_telephone, mobile=pd_mobile, user=usr)				
		pd.save()
		
		ed = EmploymentDetails(company_type=ed_companytype, designation=ed_designation, income=ed_income, work_years=ed_workyears, name=ed_name, office_address=ed_officeaddress, city=ed_city, pincode=ed_pincode, email_id=ed_emailid, user=usr)
		ed.save()
		
		bd = BankDetails(account_number=bd_account_number, bankname=bd_bankname, branch_address=bd_branch_address, account_type=bd_account_type, user=usr)
		bd.save()
		
		cd = Card(card_type=cd_cardtype, interest = 343, credited_amount=9078, user=usr)	
		cd.save()
		
		return render_to_response('register/success.html', {'USR': usr})
		
				
