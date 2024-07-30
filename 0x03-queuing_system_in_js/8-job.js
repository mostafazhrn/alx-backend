export default function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) throw new Error('Jobs is not an array');
    jobs.forEach((job) => {
        const job_data = {
            phoneNumber: job.phoneNumber,
            message: job.message
        };
        const new_job = queue.create('push_notification_code', job_data).save((err) => {
            if (!err) console.log(`Notification job created: ${new_job.id}`);
        });
        new_job.on('complete', () => console.log(`Notification job ${new_job.id} completed`));
        new_job.on('failed', (error) => console.log(`Notification job ${new_job.id} failed: ${error}`));
        new_job.on('progress', (progress) => console.log(`Notification job ${new_job.id} ${progress}% complete`));
    });
}

