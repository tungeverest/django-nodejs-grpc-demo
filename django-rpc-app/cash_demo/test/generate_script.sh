/home/tungfit/.venv/cash-demo/bin/python3 -m grpc_tools.protoc -I./protos --python_out=./services/demo --grpc_python_out=./services/demo ./protos/demo.proto

# cd /home/tungfit/Dropbox/internetofmoney/cash-demo/cash_demo/cash_demo
# ./generate_script.sh
# import services.demo.demo_pb2 as demo__pb2