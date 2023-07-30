# Week 6 — Deploying Containers

## Intro
- Week 6 in progress...

## Progress
- 7/29/23
    - Working on ECS / Fargate. I noticed the Role we created was named "Policy" on the end so I remamed it to Role: CruddurServiceExecutionRole (after I wrote this I saw Andrew realize it in the video)
    - To get all the values I needed into backend-flask.json, I first put a "$" in front of all the environment variable references, then wrote a script that replaces all those instanced with the actual values from my environment variables