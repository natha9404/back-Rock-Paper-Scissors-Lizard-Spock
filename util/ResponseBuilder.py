from util.Cross import Cross
from rest_framework.response import Response
from config.errorMessages import ErrorMsg
__author__ = 'nbedoya'

headers = Cross()
ErrorMSG = ErrorMsg()


class Response_Builder:

    def __init__(self):
        self._response_data = {}

    @staticmethod
    def valid_status(status):
        return True if status in ErrorMSG.codes else False

    @classmethod
    def validate_params(cls, data):
        _data = {}
        if isinstance(data, list):
            _data["info"] = data
        elif isinstance(data, dict):
            _data = data
        else:
            _data['info'] = data
        return _data

    def send_response(self, _status, _msg=None, _data=None):
        status = _status if self.valid_status(_status) else 200
        msg = _msg if _msg is not None else ErrorMSG.get_msg(_status)
        self._response_data['status'] = status
        self._response_data['message'] = msg
        self._response_data['data'] = self.validate_params(_data) if _data is not None else {}
        return Response(self._response_data, status=_status, headers=headers.get_headers())

    def send_xml_response(self, _status, _msg=None, _data=None):
        return Response(data=_data, status=_status, content_type='text/xml')