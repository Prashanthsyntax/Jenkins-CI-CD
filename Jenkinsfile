pipeline {
    agent any

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
                bat 'python -m venv venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                bat """
                venv\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                bat """
                venv\\Scripts\\activate
                pytest
                """
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
