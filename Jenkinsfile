
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out DevOpsX 2.0 source code...'
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                echo 'Checking Python installation...'
                bat 'python --version'
                bat 'pip --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing project dependencies...'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running DevOpsX 2.0 tests...'
                bat 'python -m pytest -v'
            }
        }
    }

    post {
        success {
            echo 'DevOpsX 2.0 CI Pipeline completed successfully!'
        }
        failure {
            echo 'DevOpsX 2.0 CI Pipeline failed. Check the logs.'
        }
    }
}
