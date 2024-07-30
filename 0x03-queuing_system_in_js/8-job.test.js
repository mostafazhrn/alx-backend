import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue();

const lst = [
    {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
    }
];

