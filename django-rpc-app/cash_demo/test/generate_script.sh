python -m grpc_tools.protoc -I./protos --python_out=./services/demo --grpc_python_out=./services/demo ./protos/demo.proto

# cd .../django-rpc-app/cash_demo/test
# ./generate_script.sh
# edit file demo_pb2_grpc.py: import demo_pb2 as demo__pb2 => import services.demo.demo_pb2 as demo__pb2