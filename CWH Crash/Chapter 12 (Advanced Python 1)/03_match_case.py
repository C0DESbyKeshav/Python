# Match statement is similar to the switch statement found in other programming languages.
# The basic syntax of the match statement involves matching a variable against several cases using the case keyword.


def http_status(status):
    match status:
        case 100:
            return "Informational"
        case 101:
            return "Switching Protocols"
        case 200:
            return "Success"
        case 201:
            return "Created"
        case 202:
            return "Accepted"
        case 203:
            return "Non-Authoritative Information"
        case 204:
            return "No Content"
        case 205:
            return "Reset Content"
        case 206:
            return "Partial Content"
        case 300:
            return "Multiple Choices"
        case 301:
            return "Moved Permanently"
        case 302:
            return "Found"
        case 303:
            return "See Other"
        case 304:
            return "Not Modified"
        case 305:
            return "Use Proxy"
        case 307:
            return "Temporary Redirect"
        case 400:
            return "Bad Request"
        case 401:
            return "Unauthorized"
        case 402:
            return "Payment Required"
        case 403:
            return "Forbidden"
        case 404:
            return "Not Found"
        case 405:
            return "Method Not Allowed"
        case 406:
            return "Not Acceptable"
        case 407:
            return "Proxy Authentication Required"
        case 408:
            return "Request Timeout"
        case 409:
            return "Conflict"
        case 410:
            return "Gone"
        case _:
            return "Unknown Status Code"
        # This case is used to match any value not explicitly listed above.

        
print(http_status(404))
print(http_status(300))
print(http_status(202))
print(http_status(906472))
