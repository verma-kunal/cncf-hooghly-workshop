# Demo - Simple CI/CD Pipeline With Jenkins

### Prerequisites

- An app (I'm using a [Django ToDo List](https://github.com/shreys7/django-todo))
- [Docker](https://docs.docker.com/engine/install/) installed
- [Jenkins](https://www.jenkins.io/doc/book/installing/) installed


#### 1. Local Setup

- Follow the instructions mentioned [here](https://github.com/shreys7/django-todo).

#### 2. Run Tests

```python

python manage.py test -v=3

```

#### 3. Run Docker Container (locally)

```bash

docker build -t django-todo:latest .

docker run -dp 8000:8000 django-todo:latest

```

#### 4. Setup a Jenkins Pipeline

- Detailed steps given [here](https://kverma.hashnode.dev/aws-cloud-deployment-automation-with-jenkins-ci#heading-step-8-setting-up-a-jenkins-pipeline)

#### 5. Jenkinsfile 

- Detailed breakdown of Jenkinsfile given [here](https://kverma.hashnode.dev/aws-cloud-deployment-automation-with-jenkins-ci#heading-step-9-analysis-of-jenkinsfile)

#### 6. Pipeline Execution using Jenkins

1. Make a code change and commit to git.
2. Trigger the Jenkins pipeline
3. Check docker container status
4. Check Docker Hub status
5. Access the app (with the new changes)

## Resources

Refer the [resources](https://docs.google.com/document/d/13382lghUZxsO8ZFNbgT1Iuv4ndUd7cxeEKtZsLENamc/edit?usp=sharing) to learn more!


