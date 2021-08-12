var grpc = require('grpc');

var protoLoader = require('@grpc/proto-loader');
const server = new grpc.Server();
const address = '127.0.0.1:50056'
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
function sayHello(call, callback) {
    callback(null, { message: 'Hello2 ' + call.request.name });
}

function sayHelloAgain(call, callback) {
    callback(null, { message: 'Hello2 again, ' + call.request.name });
}
server.addProtoService(
    demo.Greeter.service,
    { sayHello: sayHello, sayHelloAgain: sayHelloAgain }
);
server.bind(address, grpc.ServerCredentials.createInsecure());
server.start();
console.log('server start');

