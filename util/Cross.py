__author__ = 'nbedoya'


class Cross:
    def set_headers(self, response):
        response['Access-Control-Allow-Origin'] = '*'
        return response

    def get_headers(self,):
        HEADERS_OPTIONS = {
            # Dictionary headers into response pass method
            "Access-Control-Allow-Headers": "Content-Type, x-requested-with, Authorization",
            "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Max-Age": 1,
            "Allow": "GET, HEAD, POST, PUT, DELETE, TRACE, OPTIONS, PATCH"
        }
        return HEADERS_OPTIONS