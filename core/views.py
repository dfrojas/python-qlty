import json
import random
import string
import datetime

from subprocess import PIPE, run

from pylint import epylint as lint

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View, DetailView, TemplateView

from core.models import Snippet


class Editor(TemplateView):
    template_name = "editor.html"


class Process(View):
	"""
	Executes Pylint
	"""

	def post(self, request, *args, **kwargs):
		code = request.POST['code']
		file = open('testfile.py', 'w')
		file.write(code)
		file.close()
		command = run('pylint --output-format=json testfile.py', stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
		result_json = json.loads(command.stdout)
		return render(request, 'result.html', context={'result': result_json, 'code':code})


class Share(View):
	"""
    Make all logic for share function
	"""

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
	    return super(Share, self).dispatch(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		"""
		We use more secure random generator:
		https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python/23728630#23728630
		"""
		code = request.POST['code']
		result = request.POST['result']
		share_code = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(6))
		check = Snippet.objects.filter(share_code=share_code).exists()
		while check:
		    pass
		result = json.loads(result)
		create_code = Snippet.objects.create(share_code=share_code,
			                                    date=datetime.datetime.now(),
			                                    result=result, code=code)
		return JsonResponse({'sucess': True, 'share_code': create_code.share_code})


class SharedCode(DetailView):
	"""
	TODO: Report bug to Django,
	when remove iexact filter and then add again generates error
	"""
	model = Snippet
	template_name = 'shared.html'
	slug_field = 'share_code'
	slug_url_kwarg = 'share_code'


# Add anything
