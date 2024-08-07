import redis from 'redis';
const client = redis.createClient();

client.on('connect', function() {
    console.log(`Redis client connected to the server`);
});

client.on('error', function(error) {
    console.error(`Redis client not connected to the server: ${error.message}`);
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
    const valu_find = client.get(schoolName, redis.print);
    console.log(valu_find);
}

displaySchoolValue("Holberton");
setNewSchool("Holberton", '100');
displaySchoolValue("HolbertonSanFrancisco");
