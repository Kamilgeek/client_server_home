from functools import reduce
from protocol import make_response
from decorators import logged
from database import Session

from .models import Message

@logged
def echo_controller(request):
    data = request.get('data')
    session = Session()
    message =Message(data=data)
    session.add(message)
    session.commit()
    return make_response(request, 200, data)

@logged
def get_messages_controller(request):
    session = Session()
    messages = reduce(
        lambda  value, item: value + [{'data': item.data, 'created': item.created}],
        session.query(Message).all(),
        []
    )
    return make_response(request, 200, messages)
