

class middleCore:
    def __init__(self, get_response):
        self.get_response = get_response
        pass

    def __call__(self, request):
        response = self.get_response(request)
        return response
