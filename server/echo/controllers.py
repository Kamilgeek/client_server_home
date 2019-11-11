from protocol import validate_request, make_response

def echo_controller(request):
    data = request.get('data')
    return make_response(request, 200, data)