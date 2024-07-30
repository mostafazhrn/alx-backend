import redis from 'redis';
const subs = redis.createClient();

subs.on('connect', function() {
    console.log(`Redis client connected to the server`);
});

subs.on('error', function(error) {
    console.error(`Redis client not connected to the server: ${error.message}`);
});

subs.subscribe('holberton school channel');

subs.on('message', function(channel, message) {
    console.log(message);
    if (message === 'KILL_SERVER') {
        subs.unsubscribe('channel');
        subs.quit();
    }
});

