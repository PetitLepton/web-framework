from webob import Request, Response
from parse import parse


class API:
    def __init__(self):
        self.routes = {}

    def route(self, path):
        """Decorator to extract the routes ala Flask"""

        def wrapper(handler):
            self.routes[path] = handler
            return handler

        return wrapper

    def default_response(self, request, response):
        response.status = 404
        response.text = "Page not found"

    def find_handler(self, request_path):
        """Returns the handler corresponding to the requested path
        aswell as the keywords arguments. If the requested path does
        not exist, return the default 404 handler."""

        selected_handler = self.default_response
        kwargs = {}

        for path, handler in self.routes.items():
            parse_result = parse(path, request_path)
            if parse_result is not None:
                selected_handler = handler
                kwargs = parse_result.named

        return selected_handler, kwargs

    def handle_request(self, request):
        response = Response()
        handler, kwargs = self.find_handler(request_path=request.path)
        handler(request, response, **kwargs)
        return response

    def __call__(self, environ, start_response):
        request = Request(environ)
        response = self.handle_request(request)
        return response(environ, start_response)
