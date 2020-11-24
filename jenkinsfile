pipeline {
    agent any

    environment {
       API_KEY  = credentials('API_KEY')
    }
    stages {
        stage('Build') {
            steps {
                sh './init.py' 
            }
        }
    }
}
