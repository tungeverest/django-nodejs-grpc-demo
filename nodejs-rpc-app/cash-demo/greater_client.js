let grpc = require("grpc");
var protoLoader = require("@grpc/proto-loader");
var readline = require("readline");
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
const address = '127.0.0.1:50055'
var client = new demo.Greeter(address,
    grpc.credentials.createInsecure());
console.log(123333333333333333);

client.sayHello({ name: 'NodeJS Client. Hi!' }, function (err, response) {
    console.log('Greeting:', response.message);
});
setTimeout(() => {
    client.sayHelloAgain({ name: 'hi' }, function (err, response) {
        console.log('Greeting:', response.message);
    });

}, 2000);