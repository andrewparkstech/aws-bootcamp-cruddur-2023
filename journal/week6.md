# Week 6 — Deploying Containers

## Intro
- Week 6/7 completed

## Progress
- 7/29/23
   - Working on ECS / Fargate. I noticed the Role we created was named "Policy" on the end so I remamed it to Role: CruddurServiceExecutionRole (after I wrote this I saw Andrew realize it in the video)
   - To get all the values I needed into backend-flask.json, I first put a "$" in front of all the environment variable references, then wrote a script that replaces all those instanced with the actual values from my environment variables
   - CPU and RAM for backend-flask task definition had to go in the first block, as opposed to inside the container definition
   - Had an issue with message data not showing up - it was due to old user uuid being in the DB - updated with new data and it works
 - 7/30/23
   - worked on frontend
 - 7/31/23
   - worked on scripts
 - 8/5/23
   - Implemented token refresh
 - 8/6/23
   - Completed Container Insights video - Week6/7 completed!