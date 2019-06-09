__author__ = 'nbedoya'


class ErrorMsg:
    def __init__(self):
        pass


    _codes = {
        # Simple Codes
        200: "OK",
        201: "Create",
        204: "No Content",
        206: "Partial Content",

        400: "Bad Request",
        401: "Unauthorized",
        404: "Not Found",

        500: "Internal Server Error",
        503: "Service Unavailable",
        
    }

    @property
    def codes(self):
        return self._codes

    def get_msg(self, code):
        return self._codes.get(code, "message not found")