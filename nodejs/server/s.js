const WebSocket = require('ws');
const http = require('http');

const server = http.createServer();
const wss = new WebSocket.Server({
    server
});

// let clientCounter = 0;
// const clients = new Map();

wss.on('connection', function connection(ws) {
    // clientCounter++;
    // const clientId = clientCounter;
    // clients.set(ws, clientId);
    // console.log(`client${clientId} connected; total clients: ${clients.size}`);

    // const pingInterval = setInterval(() => {
    //     if (ws.readyState === WebSocket.OPEN) {
    //         ws.ping();
    //     }
    // }, 1000); // 1 seconds

    // ws.on('pong', () => {
    //     console.log(`pong from client${clientId}`);
    // });

    // ws.on('message', function incoming(message) {
    //     console.log(`client${clientId} sent -> ${message.toString()}`);
    //     ws.send(`client sent -> ${message}`);
    // });

    ws.on('close', (code, reason) => {
        console.log(`client disconnected`);
        // clearInterval(pingInterval);
        // // clientCounter--;
        // clients.delete(ws);

        // if (reason == "") {
        //     reason = "No reason received";
        // }
        // console.log(`client${clientId} disconnected - code: ${code} and reason: ${reason}`);
    });

    ws.on('error', (err) => {
        console.error(`Error occurred: ${err.message}`);
    });

    console.log(`client connected`);
});

const port = 8011;
const host = 'localhost';
server.listen(port, host, () => {
    console.log(`WebSocket server is running on ws://${host}:${port}`);
});