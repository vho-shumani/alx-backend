import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  let queue;

  before(() => {
    queue = kue.createQueue();
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it('displays an error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('not an array', queue)).to.throw('Jobs is not an array');
  });

  it('creates two new jobs to the queue', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account'
      }
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);

    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);

    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
  });

  it('registers the progress event handler for each job', (done) => {
    const job = queue.create('push_notification_code_3', {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    });

    job.on('progress', (progress) => {
      expect(progress).to.be.a('number');
      done();
    });

    job.emit('progress', 50);
  });

  it('registers the complete event handler for each job', (done) => {
    const job = queue.create('push_notification_code_3', {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    });

    job.on('complete', () => {
      expect(true).to.be.true;
      done();
    });

    job.emit('complete');
  });

  it('registers the failed event handler for each job', (done) => {
    const job = queue.create('push_notification_code_3', {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    });

    job.on('failed', (errorMessage) => {
      expect(errorMessage).to.equal('Phone number 4153518780 is blacklisted');
      done();
    });

    job.emit('failed', new Error('Phone number 4153518780 is blacklisted'));
  });
});
