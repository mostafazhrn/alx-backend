import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
    phoneNumber: '4153518780',
    message: 'This is the code to verify your account'
};

const boulot = queue.create('push_notification_code', jobData).save((err) => {
    if (!err) console.log(`Notification job created: ${boulot.id}`);
});

boulot.on('complete', () => console.log('Notification job completed'));
boulot.on('failed', () => console.log('Notification job failed'));

