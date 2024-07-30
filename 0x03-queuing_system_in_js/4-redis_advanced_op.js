import redis from 'redis';
const { promisify } = require('util');

const client = redis.createClient();
const hgetall = promisify(client.hgetall).bind(client);


async function main() {
    const hashes = {
        Portland: 50,
        Seattle: 80,
        'New York': 20,
        Bogota: 20,
        Cali: 40,
        Paris: 2
    };

    for (const key in hashes) {
        client.hset('HolbertonSchools', key, hashes[key], redis.print);
    }

    const response = await hgetall('HolbertonSchools');
    console.log(response);
}
main();

