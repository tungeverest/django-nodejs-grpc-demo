from concurrent import futures
import time
import logging
import grpc

# import the generated classes
from services.demo import demo_pb2
from services.demo import demo_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Greeter(demo_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        return demo_pb2.HelloResponse(message='Python hello, %s!' % request.name)

    def SayHelloAgain(self, request, context):
        return demo_pb2.HelloResponse(message='Python hello again, %s!' % request.name)

# create a gRPC server
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # use the generated function `add_GreeterServicer_to_server`
    demo_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50055')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    logging.basicConfig()
    serve()