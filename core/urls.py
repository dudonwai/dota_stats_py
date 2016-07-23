import core.views as coreviews

urlpatterns = [
	url(r'^$', coreviews.LandingView.as_view()),
	]