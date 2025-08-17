pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t my-sample-app .'
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    sh 'docker stop my-sample-app || true'
                    sh 'docker rm my-sample-app || true'
                    sh 'docker run -d -p 8888:8888 --name my-sample-app my-sample-app'
                }
            }
        }
    }
}
