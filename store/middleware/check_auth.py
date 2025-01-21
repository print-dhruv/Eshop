from django.shortcuts import redirect

# middleware are called before any request
# writing middleware in settings.py, will make it call in every request
# we can apply middleware in views class methods, but more better approch to apply in url.py of a store
def check_authorization(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        return_url = request.META['PATH_INFO']

        if not request.session.get('session_customer_id'):
            return redirect(f'/login?return_url={return_url}') #this will be shown on the link of login when redirected through middleware

        response = get_response(request) # pass to the view

        # Code to be executed for each request/response after
        # the view is called.
        return response
    return middleware