pipeline {
  agent any
  stages {
    stage('Test') {
      agent {
        dockerfile {
        filename 'Dockerfile'
        dir 'FlaskServer'
        }
      }
      steps {
        echo 'Testing..'
        sh 'pwd'
        sh 'cd /srv/flask-app && ls -ahl'
        sh 'cd /srv/flask-app && python test.py -v'
        sh 'ls /var/jenkins_home/workspace/spacerobots_2_master'
      }
    }
    stage('Deploy') {
      agent any
      steps {
        echo 'Deploying....'
        sh "ssh docker@kudernatsch.at 'bash -s' < deploy.sh"
      }
    }
  }
  
}
