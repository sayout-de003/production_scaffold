import logging
import time

logger = logging.getLogger("request_logger")


# pylint: disable=too-few-public-methods
class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        duration = int((time.time() - start_time) * 1000)

        logger.info(
            "",
            extra={
                "method": request.method,
                "path": request.path,
                "status": response.status_code,
                "duration": duration,
                "user_agent": request.META.get("HTTP_USER_AGENT", "-"),
            },
        )
        return response
