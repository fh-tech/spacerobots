pipeline {
  agent {
    dockerfile {
      filename 'Dockerfile'
      dir 'FlaskServer'
    }

  }
  stages {
    stage('Test') {
      steps {
        echo 'Testing..'
        sh 'pwd'
        sh 'cd /srv/flask-app && ls -ahl'
        sh 'cd /srv/flask-app && python test.py -v'
        sh 'ls /var/jenkins_home/workspace/spacerobots_2_master'
      }
      post {
        always {
          junit '/var/jenkins_home/workspace/spacerobots_2_master/*.xml'
      }
   }
    }
    stage('Deploy') {
      steps {
        echo 'Deploying....'
      }
    }
  }
  
}
