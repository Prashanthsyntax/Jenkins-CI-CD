pipeline {
    agent any

    environment {
        VENV = "venv"
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo 'Cloning GitHub repository...'
                checkout scm
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                echo 'Creating virtual environment...'
                sh '''
                python -m venv venv
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                sh '''
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running pytest...'
                sh '''
                . venv/bin/activate
                pytest
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Build Successful – All tests passed'
        }
        failure {
            echo '❌ Build Failed – Fix errors before merging'
        }
    }
}
