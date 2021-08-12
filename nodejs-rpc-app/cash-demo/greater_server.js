console.log('server start');
var grpc = require('grpc');
var protoLoader = require('@grpc/proto-loader');
const server = new grpc.Server();
const address = '127.0.0.1:50052'
var PROTO_PATH = __dirname + '/protos/demo.proto';
// Suggested options for similarity to existing grpc.load behavior
var packageDefinition = protoLoader.loadSync(
    PROTO_PATH,
    {
        keepCase: true,
        longs: String,
        enums: String,
        defaults: true,
        oneofs: true
    });
var protoDescriptor = grpc.loadPackageDefinition(packageDefinition);
// The protoDescriptor object has the full package hierarchy
var demo = protoDescriptor.hello;
function SayHello(call, callback) {
    callback(null, { message: 'Nodejs Server say: ' + call.request.name });
}

function SayHelloAgain(call, callback) {
    callback(null, { message: 'Nodejs Server say: again, ' + call.request.name });
}
server.addProtoService(
    demo.Greeter.service,
    { sayHello: SayHello, sayHelloAgain: SayHelloAgain }
);
server.bind(address, grpc.ServerCredentials.createInsecure());
server.start();

