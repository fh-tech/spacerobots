pipeline {
  agent {
    docker {
      image 'python:3.7'
    }

  }
  stages {
    stage('Build') {
      steps {
        echo 'Building..'
        sh 'pip install -r requirements.txt --src /usr/local/src'
      }
    }
    stage('Test') {
      steps {
        echo 'Testing..'
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