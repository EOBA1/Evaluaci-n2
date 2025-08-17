const http = require('http');

const hostname = '0.0.0.0'; // Escucha en todas las interfaces de red
const port = 8888; // El puerto requerido

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('¡ mi aplicacion web simple!\n');
});

server.listen(port, hostname, () => {
  console.log(`El servidor esta corriendo en http://${hostname}:${port}/`);
});
