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
        sh 'python test.py -v'
      }
    }
    stage('Deploy') {
      steps {
        echo 'Deploying....'
      }
    }
  }
}