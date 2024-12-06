const WebSocket = require('ws');

const wsServer = process.argv[2];
const numClients = parseInt(process.argv[3], 10) || 1; // Default to 1 client if not provided

if (!wsServer) {
    console.error('WebSocket server address is missing. Usage: node c.js <wsServer>');
    process.exit(1);
  }

  let clientCounter = 0; // To keep track of the number of connected clients
const clients = new Map(); // To store client-specific information

  function createWebSocketClient(clientId) {
  
    // Create a WebSocket instance
const ws = new WebSocket(wsServer);


ws.on('open', function open() {
  clientCounter++;
    const clientId = clientCounter;
  clients.set(ws, clientId);
  console.log(`client${clientId} connected; total clients: ${clients.size}`);

  // Close the connection after 5 seconds
  setTimeout(() => {
    clients.delete(ws);
    clientCounter--;
    ws.close();
    console.log(`client${clientId} connection closed after 5 seconds`);
  }, 5000); // 5000 milliseconds = 5 seconds
});

// WebSocket close event
ws.on('close', (code, reason) => {
    console.log(`Disconnected from WebSocket server; code: ${code} and reason: ${reason}`);
});

// WebSocket error event
ws.on('error', function error(err) {
  console.error('WebSocket error:', err.message);
});

}



for (let i = 1; i <= numClients; i++) {
    createWebSocketClient(i);
  }