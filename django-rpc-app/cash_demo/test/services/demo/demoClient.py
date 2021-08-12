import logging
from django.conf import settings
import demo_pb2
import demo_pb2_grpc
from base_grpc import BaseGrpcClient
from base_grpc import CASH_GRPC_SERVICE_HOST


class NotificationTemplateClient(BaseGrpcClient):

    def __init__(self, channel_uri=CASH_GRPC_SERVICE_HOST['DEMO']):
        # print(CASH_GRPC_SERVICE_HOST['DEMO'])
        print(settings.CASH_GRPC_SERVICE_HOST)
        try:
            self.set_pb(demo_pb2)
            self.set_pb_grpc(demo_pb2_grpc)
            self.set_channel(channel_uri=channel_uri)
            stub = demo_pb2_grpc.GreeterStub(self.channel)
            self.set_stub(stub)

        except Exception as e:
            raise Exception(
                "Connect to currency service fail with reason : " + str(e))

    def runSayHello(self):

        response = self.get_stub().SayHello(
            self.get_pb().HelloRequest(name='PythonSayHello'))
        response2 = self.get_stub().SayHelloAgain(
            self.get_pb().HelloRequest(name='PythonSayHelloAgain'))
        print("Greeter client1 received: " + response.message)
        print("Greeter client2 received: " + response2.message)


run = NotificationTemplateClient()
# run.runSayHello()
