https://github.com/raynux/grpc-demo

gRPC samples

Super simple gRPC samples in Node.js and Python. Both version are compatible to each other.

More about gRPC, see http://www.grpc.io/
# Django

- Setup
Create new venv and activate:

pip install -r requirements.txt

- Generate Script:

python -m grpc_tools.protoc -I./protos --python_out=./services/demo --grpc_python_out=./services/demo ./protos/demo.proto

--or--

/.generate_script.sh

Edit file demo_pb2_grpc.py: import demo_pb2 as demo__pb2 => import services.demo.demo_pb2 as demo__pb2

- Server


# Node.js

- Setup
npm install
