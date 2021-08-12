from django.conf import settings
import grpc
import time
import os
CASH_GRPC_SERVICE_HOST = {
    "DEMO": os.getenv("CASH_GRPC_SERVICE_DEMO", "127.0.0.1:50052")
}


class BaseGrpcClient:
    client = None
    pb = None
    pb_grpc = None
    channel = None
    stub = None
    uid = None
    retry_iterator = 0

    def __init__(self, uid=None):
        self.uid = uid

    def set_pb(self, pb):
        self.pb = pb

    def set_pb_grpc(self, pb_grpc):
        self.pb_grpc = pb_grpc

    def set_channel(self, channel_uri):
        self.channel = grpc.insecure_channel(
            target=channel_uri, options=[
                ('grpc.enable_retries', 1),
                ('grpc.keepalive_timeout_ms', 10000)]
        )
        return self.channel

    def set_stub(self, stub):
        self.stub = stub

    def get_stub(self):
        return self.stub

    def get_pb_grpc(self):
        return self.pb_grpc

    def get_pb(self):
        return self.pb
