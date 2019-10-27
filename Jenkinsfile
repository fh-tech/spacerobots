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
      }
    }
    stage('Deploy') {
      steps {
        echo 'Deploying....'
      }
    }
  }
  post {
    always {
      junit '/var/jenkins_home/workspace/spacerobots_2_master/*.xml'

    }

  }
}
