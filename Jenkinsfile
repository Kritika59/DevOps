pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Checkout the latest code from GitHub repository
                git 'https://github.com/kritika59/DevOps.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Install Python dependencies if you have a requirements.txt file
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                // Run your tests with pytest and generate a report
                sh 'pytest test.py --html=report.html --self-contained-html'
            }
        }
        stage('Archive Test Report') {
            steps {
                // Archive the test report as an artifact
                archiveArtifacts artifacts: '**/report.html', allowEmptyArchive: true
            }
        }
    }
}

