from werkzeug.wrappers import Request, Response
#示例
@Request.application
def hello(request):
    return Response('Hello World!我所同')

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 4000, hello)
