pipeline {
  agent {
    dockerfile {
      filename 'Dockerfile'
      dir 'FlaskServer'
    }

  }
  stages {
    stage('Build') {
      steps {
        echo 'Building..'
        sh 'mv FlaskServer/requirements.txt FlaskServer/app/'
        sh '''
cd FlaskServer/app/ && pip install -r requirements.txt --src /usr/local/src'''
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
