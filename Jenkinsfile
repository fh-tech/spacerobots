pipeline {
    agent {
        dockerfile {
            dir "FlaskServer"
            args "--target test"
        }
    }
    stages {
         stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}