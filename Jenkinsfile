pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/venkatadurgaraoponnaganti/hello-flask.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                
                pip install --no-cache-dir -r requirements.txt
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t hello-flask-1 .
                '''
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                docker run -d -p 5000:5000 --name hello-flask-container hello-flask-1
                '''
            }
        }
    }
}

