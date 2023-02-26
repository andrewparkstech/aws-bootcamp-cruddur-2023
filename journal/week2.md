# Week 2 — Distributed Tracing

## Intro
Wow! The bootcamp is going full steam ahead and not looking back! That's a good thing as it's forcing me to think and learn. On Week 0, I thought oh this will be easy, I probably won't learn anything. HA! Not so, and again that is a good thing.

## Issues
### Gitpod
Last week I had started using a custom gitpod workspace, but it was just taking too long to load the CDE due to build times and I know that would annoy not only myself but Andrew as well (and whoever assists grading) so I reverted back to using just the gitpod.yml statements to install AWS CLI, etc. I changed the AWS install to a "before" statement insetad of an init statement, and also added a line to remove the zip file when done, after I realized that upon starting the environment, it was getting stuck on a prompt asking if I wanted to overwrite the AWS zip file.

## Homework
So far I have the code from the Week2 main video completed. Next in line is:
- Video: observability vs monitoring
- Video: CloudWatch
- Homework: other homework that may show up once Week2 portal opens

### AWS X-Ray
After adding the X-Ray code, my backend was not starting up. I went to the Docker extension in GitPod, and checked the logs for the backend container. It was showing an error: `NameError: name 'app' is not defined`. I went back to app.py to check, and noticed I had the X-Ray code before the definition `app = Flask(__name__)`. I moved the X-Ray code to be after this and the container starts up.
