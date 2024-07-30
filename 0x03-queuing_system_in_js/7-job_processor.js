import kue from 'kue';
const q_ue = kue.createQueue();

const num_blacklist = ['4153518780', '4153518781'];

const sendNotification = (phoneNumber, message, job, done) => {
    if (num_blacklist.includes(phoneNumber)) {
        return done( new Error(`Phone number ${phoneNumber} is blacklisted`));
    }
    job.progress(0, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
}

