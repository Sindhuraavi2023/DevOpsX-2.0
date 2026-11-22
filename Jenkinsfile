
pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\sindh\\AppData\\Local\\Programs\\Python\\Python39\\python.exe'
    }

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
                bat '"%PYTHON%" --version'
                bat '"%PYTHON%" -m pip --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing project dependencies...'
                bat '"%PYTHON%" -m pip install -r requirements.txt'
            }
        }

        stage('Docker Connectivity Check') {
            steps {
                 echo 'Checking Docker access from Jenkins...'
                   bat 'docker version'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running DevOpsX 2.0 tests...'
                bat '"%PYTHON%" -m pytest -v'
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
