# 0x19-postmortem
### Postmortem: When Our Database Took a Power Nap (And Took the Website Down With It)  

**Issue Summary**  
**Duration:** August 12, 2024, 10:30 AM - 1:45 PM UTC (3 hours 15 minutes)  
**Impact:** The main web app decided it was time for a siesta—85% of users experienced the kind of page load times that make you question your life choices. Another 15% couldn't access the site at all, and probably thought we had disappeared like a magician's rabbit.  
**Root Cause:** Our database connection pool had a midlife crisis and forgot how to handle high traffic. 


### Timeline: The Adventure in Bullet Points

- **10:30 AM UTC**: Our monitoring system went into panic mode—alerts were flying about slow responses and errors.
- **10:32 AM UTC**: The on-call engineer, fueled by too much coffee, jumped in, suspecting a DDoS attack (because why not assume the worst?).
- **10:40 AM UTC**: Network traffic analysis: No suspicious spikes. DDoS theory goes to the trash.
- **10:50 AM UTC**: Backend team gets a call: “The database is misbehaving, figure it out.”
- **11:00 AM UTC**: Backend team inspects the database, expecting chaos, but finds nothing—leading to a brief existential crisis.
- **11:30 AM UTC**: Someone finally realizes the connection pool is the bottleneck, like a single-lane road during rush hour.
- **12:00 PM UTC**: Aha! The connection pool’s maximum limit is set too low. Facepalms ensue.
- **12:30 PM UTC**: Connection pool limits are increased, and the app is restarted. Users begin to see daylight again.
- **1:45 PM UTC**: Full service restored. Everyone breathes a sigh of relief, followed by a group high-five.


### Root Cause and Resolution: A Tale of a Tired Database

Our database connection pool was having a bad day, with a maximum connection limit set so low it could barely handle a dinner party, let alone a traffic surge. When too many users showed up, the pool got overwhelmed, leading to massive delays and timeouts.

**Fix:** We pumped up the connection pool limits like a bodybuilder on protein shakes. After a quick restart, our app was back in action, serving users faster than ever. 


### Corrective and Preventative Measures: Lessons Learned and To-Do List

**Things to Fix:**
- **Connection Pool Gym Time:** Review and optimize the connection pool settings to handle even the rowdiest traffic surges.
- **Monitoring Makeover:** Add shiny new metrics to monitor connection pool usage, so we can catch issues before they explode.
- **Traffic Torture Tests:** Regular load testing to make sure our system can handle peak times like a pro.

**To-Do List:**
- [ ] **Boost Connection Pool Limits:** Adjust settings to handle more connections simultaneously.
- [ ] **Install Connection Pool Metrics Dashboard:** So we can watch those connections like a hawk.
- [ ] **Schedule Load Testing:** Let’s stress test this baby quarterly to avoid future surprises.
- [ ] **Update Incident Response Playbook:** Because who doesn’t love a good playbook upgrade?


By injecting a little humor and adding some visuals, we hope this postmortem keeps you awake and informed. After all, our database took a nap so you don’t have to!
