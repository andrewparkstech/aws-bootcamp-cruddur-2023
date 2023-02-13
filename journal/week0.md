# Week 0 — Billing and Architecture
## Intro
Thanks for this opportunity! I completed all the homework on the checklist. I've explained each item below.

## Setting up a billing alarm and budget
For the budget, I had an existing zero-spend budget I created previously but I liked the idea of creating the budget via CLI so I followed that through and now have a new budget named Budget_from_CLI. I then created an SNS topic and subscribed to it via CLI. I used a gmail address and the subscription confirmation email went into my spam folder, so you may want to check that if you don’t see the email show up pretty quick. I went on to create a CloudWatch billing alarm via the CLI. I also created an alarm via the GUI.

## Generating AWS Credentials
I created a new GitHub repository using the provided template. Using Andrew’s video from the official playlist, I installed the extension on FireFox that adds the GitPod button to GitHub. Next, I installed the AWS CLI in the GitPod terminal. I had an AWS user I set up previously with associated access credentials. I used this user’s access credentials when setting the environment variables on GitPod, per the instructions in the Week 0 video. I also edited the .gitpod.yml file with the provided code that will auto-install the AWS CLI each time the GitPod environment is launched. I did get an error when trying to do my first commit from GitPod, saying I did not have permission to push to the GitHub repo. I googled this to get answers. What you need to do is go to your GitPod User Settings and then Integrations. Select the 3 dots icon by your GitHub account and click Edit Permissions then check off public_repo so that GitPod has access to push to your public repo for this project.

## Using CloudShell
I opened up CloudShell and decided to figure out how to create an S3 bucket to make use of the shell. I used “aws s3 help” to find out how to do this. The command is “aws s3 mb s3://your-bucket-name”

## Conceptual Architecture Diagrams
#### My actual napkin design

![cruddur_napkin](https://user-images.githubusercontent.com/54210615/218597868-bf7837ff-50cb-47dd-80fe-8b9af53e4587.jpg)

#### My Lucid version of the high-level concept drawing:
[Conceptual Dragram Link](https://lucid.app/lucidchart/fe6f1a32-3b7e-477d-970c-7c29692050a3/edit?viewport_loc=-509%2C-448%2C2219%2C1052%2C0_0&invitationId=inv_dcb9d19e-812c-4a39-8ba7-250fa108104a)

![concept_dragram](https://user-images.githubusercontent.com/54210615/218357352-792bbd62-c685-41b8-a677-d63045383abb.PNG)


## Homework Stretch Assignments
### Destroy your root account credentials, Set MFA, IAM role
I used the root account only to enable billing alarms and setup my other user. I've enabled MFA as well

### Use EventBridge to hookup Health Dashboard to SNS and send notification when there is a service health issue
TBD

### Review all the questions of each pillars in the Well Architected Tool (No specialized lens)
TBD

### Create an architectural diagram (to the best of your ability) the CI/CD logical pipeline in Lucid Charts
#### My version of the Logical diagram:
[Logical Diagram Link](https://lucid.app/lucidchart/fe6f1a32-3b7e-477d-970c-7c29692050a3/edit?viewport_loc=-155%2C-247%2C2219%2C1052%2C99HwTMa.uPDE&invitationId=inv_dcb9d19e-812c-4a39-8ba7-250fa108104a)

![logical_diagram](https://user-images.githubusercontent.com/54210615/218357565-17ed6e03-e7d6-4331-a49b-92af7f9ee9f4.PNG)

### Research the technical and service limits of specific services and how they could impact the technical path for technical flexibility. 
TBD

### Open a support ticket and request a service limit
TBD

## Extra
### Domain name work
I expanded on the prereq to get a domain name. I wanted to put up an under construction page instead of having the registrar's parked page. So I followed these steps:
- Created a Hosted Zone for the domain on AWS Route53
- Updated my domain on NameCheap to use Route53 nameservers
- Created an S3 bucket to host an “under construction page”
- Named the bucket with my domain name
- Turned off Block Public Access
- Created a Policy to allow GetObject on the bucket from anyone
- Turned on Static website hosting on the bucket
- Placed my index.html file in the bucket
- Created an A record in Route53 to point my domain name to the S3 bucket
