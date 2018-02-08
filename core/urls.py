from django.urls import include, path

from core.views import Editor, Process, Share, SharedCode


urlpatterns = [
	path(r'', Editor.as_view()),
	path('check/', Process.as_view()),
	# path('result/', Result.as_view()),
	path('share/', Share.as_view()),
	# Overrind slug field kwarg by share_code when
	# URL is typed in lowercase.
	path('s/<slug:share_code>/', SharedCode.as_view()),
	path('s/<slug:slug>/', SharedCode.as_view()),

]
