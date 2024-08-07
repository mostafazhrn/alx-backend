import redis from 'redis';
const pub = redis.createClient();

pub.on('connect', function() {
    console.log(`Redis client connected to the server`);
});

pub.on('error', function(error) {
    console.error(`Redis client not connected to the server: ${error.message}`);
});

function publishMessage(message, time) {
    setTimeout(() => {
        console.log(`About to send ${message}`);
        pub.publish('holberton school channel', message);
    }, time);
}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);

