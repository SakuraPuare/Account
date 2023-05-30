# coding=utf-8
from fastapi import HTTPException


# Success

class StatusCode(HTTPException):
    """Base class for all status codes"""

    def __init__(self, status_code: int, message: str):
        Exception.__init__(self)
        super().__init__(status_code, message)

    def __bool__(self):
        return False


# Informational


class Continue(StatusCode):
    """100 Continue"""

    def __init__(self, message: str = 'Continue'):
        StatusCode.__init__(self, 100, message)


class SwitchingProtocols(StatusCode):
    """101 Switching Protocols"""

    def __init__(self, message: str = 'Switching Protocols'):
        StatusCode.__init__(self, 101, message)


class Processing(StatusCode):
    """102 Processing"""

    def __init__(self, message: str = 'Processing'):
        StatusCode.__init__(self, 102, message)


class EarlyHints(StatusCode):
    """103 Early Hints"""

    def __init__(self, message: str = 'Early Hints'):
        StatusCode.__init__(self, 103, message)


# Success

class OK(StatusCode):
    """200 OK"""

    def __init__(self, message: str = 'OK'):
        StatusCode.__init__(self, 200, message)


class Created(StatusCode):
    """201 Created"""

    def __init__(self, message: str = 'Created'):
        StatusCode.__init__(self, 201, message)


class Accepted(StatusCode):
    """202 Accepted"""

    def __init__(self, message: str = 'Accepted'):
        StatusCode.__init__(self, 202, message)


class NonAuthoritativeInformation(StatusCode):
    """203 Non-Authoritative Information"""

    def __init__(self, message: str = 'Non-Authoritative Information'):
        StatusCode.__init__(self, 203, message)


NoContent = HTTPException(status_code=204)


class ResetContent(StatusCode):
    """205 Reset Content"""

    def __init__(self, message: str = 'Reset Content'):
        StatusCode.__init__(self, 205, message)


class PartialContent(StatusCode):
    """206 Partial Content"""

    def __init__(self, message: str = 'Partial Content'):
        StatusCode.__init__(self, 206, message)


class MultiStatus(StatusCode):
    """207 Multi-Status"""

    def __init__(self, message: str = 'Multi-Status'):
        StatusCode.__init__(self, 207, message)


class AlreadyReported(StatusCode):
    """208 Already Reported"""

    def __init__(self, message: str = 'Already Reported'):
        StatusCode.__init__(self, 208, message)


class IMUsed(StatusCode):
    """226 IM Used"""

    def __init__(self, message: str = 'IM Used'):
        StatusCode.__init__(self, 226, message)


# Redirection

class MultipleChoices(StatusCode):
    """300 Multiple Choices"""

    def __init__(self, message: str = 'Multiple Choices'):
        StatusCode.__init__(self, 300, message)


class MovedPermanently(StatusCode):
    """301 Moved Permanently"""

    def __init__(self, message: str = 'Moved Permanently'):
        StatusCode.__init__(self, 301, message)


class Found(StatusCode):
    """302 Found"""

    def __init__(self, message: str = 'Found'):
        StatusCode.__init__(self, 302, message)


class SeeOther(StatusCode):
    """303 See Other"""

    def __init__(self, message: str = 'See Other'):
        StatusCode.__init__(self, 303, message)


class NotModified(StatusCode):
    """304 Not Modified"""

    def __init__(self, message: str = 'Not Modified'):
        StatusCode.__init__(self, 304, message)


class UseProxy(StatusCode):
    """305 Use Proxy"""

    def __init__(self, message: str = 'Use Proxy'):
        StatusCode.__init__(self, 305, message)


class TemporaryRedirect(StatusCode):
    """307 Temporary Redirect"""

    def __init__(self, message: str = 'Temporary Redirect'):
        StatusCode.__init__(self, 307, message)


class PermanentRedirect(StatusCode):
    """308 Permanent Redirect"""

    def __init__(self, message: str = 'Permanent Redirect'):
        StatusCode.__init__(self, 308, message)


# Client Error

class BadRequest(StatusCode):
    """400 Bad Request"""

    def __init__(self, message: str = 'Bad Request'):
        StatusCode.__init__(self, 400, message)


class Unauthorized(StatusCode):
    """401 Unauthorized"""

    def __init__(self, message: str = 'Unauthorized'):
        StatusCode.__init__(self, 401, message)


class PaymentRequired(StatusCode):
    """402 Payment Required"""

    def __init__(self, message: str = 'Payment Required'):
        StatusCode.__init__(self, 402, message)


class Forbidden(StatusCode):
    """403 Forbidden"""

    def __init__(self, message: str = 'Forbidden'):
        StatusCode.__init__(self, 403, message)


class NotFound(StatusCode):
    """404 Not Found"""

    def __init__(self, message: str = 'Not Found'):
        StatusCode.__init__(self, 404, message)


class MethodNotAllowed(StatusCode):
    """405 Method Not Allowed"""

    def __init__(self, message: str = 'Method Not Allowed'):
        StatusCode.__init__(self, 405, message)


class NotAcceptable(StatusCode):
    """406 Not Acceptable"""

    def __init__(self, message: str = 'Not Acceptable'):
        StatusCode.__init__(self, 406, message)


class ProxyAuthenticationRequired(StatusCode):
    """407 Proxy Authentication Required"""

    def __init__(self, message: str = 'Proxy Authentication Required'):
        StatusCode.__init__(self, 407, message)


class RequestTimeout(StatusCode):
    """408 Request Timeout"""

    def __init__(self, message: str = 'Request Timeout'):
        StatusCode.__init__(self, 408, message)


class Conflict(StatusCode):
    """409 Conflict"""

    def __init__(self, message: str = 'Conflict'):
        StatusCode.__init__(self, 409, message)


class Gone(StatusCode):
    """410 Gone"""

    def __init__(self, message: str = 'Gone'):
        StatusCode.__init__(self, 410, message)


class LengthRequired(StatusCode):
    """411 Length Required"""

    def __init__(self, message: str = 'Length Required'):
        StatusCode.__init__(self, 411, message)


class PreconditionFailed(StatusCode):
    """412 Precondition Failed"""

    def __init__(self, message: str = 'Precondition Failed'):
        StatusCode.__init__(self, 412, message)


class PayloadTooLarge(StatusCode):
    """413 Payload Too Large"""

    def __init__(self, message: str = 'Payload Too Large'):
        StatusCode.__init__(self, 413, message)


class URITooLong(StatusCode):
    """414 URI Too Long"""

    def __init__(self, message: str = 'URI Too Long'):
        StatusCode.__init__(self, 414, message)


class UnsupportedMediaType(StatusCode):
    """415 Unsupported Media Type"""

    def __init__(self, message: str = 'Unsupported Media Type'):
        StatusCode.__init__(self, 415, message)


class RangeNotSatisfiable(StatusCode):
    """416 Range Not Satisfiable"""

    def __init__(self, message: str = 'Range Not Satisfiable'):
        StatusCode.__init__(self, 416, message)


class ExpectationFailed(StatusCode):
    """417 Expectation Failed"""

    def __init__(self, message: str = 'Expectation Failed'):
        StatusCode.__init__(self, 417, message)


class ImATeapot(StatusCode):
    """418 I'm a teapot"""

    def __init__(self, message: str = "I'm a teapot"):
        StatusCode.__init__(self, 418, message)


class MisdirectedRequest(StatusCode):
    """421 Misdirected Request"""

    def __init__(self, message: str = 'Misdirected Request'):
        StatusCode.__init__(self, 421, message)


class UnprocessableEntity(StatusCode):
    """422 Unprocessable Entity"""

    def __init__(self, message: str = 'Unprocessable Entity'):
        StatusCode.__init__(self, 422, message)


class Locked(StatusCode):
    """423 Locked"""

    def __init__(self, message: str = 'Locked'):
        StatusCode.__init__(self, 423, message)


class FailedDependency(StatusCode):
    """424 Failed Dependency"""

    def __init__(self, message: str = 'Failed Dependency'):
        StatusCode.__init__(self, 424, message)


class TooEarly(StatusCode):
    """425 Too Early"""

    def __init__(self, message: str = 'Too Early'):
        StatusCode.__init__(self, 425, message)


class UpgradeRequired(StatusCode):
    """426 Upgrade Required"""

    def __init__(self, message: str = 'Upgrade Required'):
        StatusCode.__init__(self, 426, message)


class PreconditionRequired(StatusCode):
    """428 Precondition Required"""

    def __init__(self, message: str = 'Precondition Required'):
        StatusCode.__init__(self, 428, message)


class TooManyRequests(StatusCode):
    """429 Too Many Requests"""

    def __init__(self, message: str = 'Too Many Requests'):
        StatusCode.__init__(self, 429, message)


class RequestHeaderFieldsTooLarge(StatusCode):
    """431 Request Header Fields Too Large"""

    def __init__(self, message: str = 'Request Header Fields Too Large'):
        StatusCode.__init__(self, 431, message)


class UnavailableForLegalReasons(StatusCode):
    """451 Unavailable For Legal Reasons"""

    def __init__(self, message: str = 'Unavailable For Legal Reasons'):
        StatusCode.__init__(self, 451, message)


# Server Error

class InternalServerError(StatusCode):
    """500 Internal Server Error"""

    def __init__(self, message: str = 'Internal Server Error'):
        StatusCode.__init__(self, 500, message)


class NotImplemented(StatusCode):
    """501 Not Implemented"""

    def __init__(self, message: str = 'Not Implemented'):
        StatusCode.__init__(self, 501, message)


class BadGateway(StatusCode):
    """502 Bad Gateway"""

    def __init__(self, message: str = 'Bad Gateway'):
        StatusCode.__init__(self, 502, message)


class ServiceUnavailable(StatusCode):
    """503 Service Unavailable"""

    def __init__(self, message: str = 'Service Unavailable'):
        StatusCode.__init__(self, 503, message)


class GatewayTimeout(StatusCode):
    """504 Gateway Timeout"""

    def __init__(self, message: str = 'Gateway Timeout'):
        StatusCode.__init__(self, 504, message)


class HTTPVersionNotSupported(StatusCode):
    """505 HTTP Version Not Supported"""

    def __init__(self, message: str = 'HTTP Version Not Supported'):
        StatusCode.__init__(self, 505, message)


class VariantAlsoNegotiates(StatusCode):
    """506 Variant Also Negotiates"""

    def __init__(self, message: str = 'Variant Also Negotiates'):
        StatusCode.__init__(self, 506, message)


class InsufficientStorage(StatusCode):
    """507 Insufficient Storage"""

    def __init__(self, message: str = 'Insufficient Storage'):
        StatusCode.__init__(self, 507, message)


class LoopDetected(StatusCode):
    """508 Loop Detected"""

    def __init__(self, message: str = 'Loop Detected'):
        StatusCode.__init__(self, 508, message)


class NotExtended(StatusCode):
    """510 Not Extended"""

    def __init__(self, message: str = 'Not Extended'):
        StatusCode.__init__(self, 510, message)


class NetworkAuthenticationRequired(StatusCode):
    """511 Network Authentication Required"""

    def __init__(self, message: str = 'Network Authentication Required'):
        StatusCode.__init__(self, 511, message)
