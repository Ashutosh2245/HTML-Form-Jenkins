pipeline {
    agent any

    stages {

        stage('Checkout Source Code') {
            steps {
                echo 'Fetching source code from GitHub...'

                checkout scm

                echo 'Source code retrieved successfully.'
            }
        }

        stage('Verify HTML File') {
            steps {
                script {
                    if (fileExists('index.html')) {
                        echo 'SUCCESS: index.html exists.'
                    } else {
                        error 'FAILURE: index.html not found.'
                    }
                }
            }
        }

        stage('Verify Python') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'python3 --version'
                    } else {
                        bat 'py -3 --version'
                    }
                }
            }
        }

        stage('Automated HTML Tests') {
            steps {
                echo 'Running automated HTML form tests...'

                script {
                    if (isUnix()) {
                        sh 'python3 -m unittest -v test_form.py'
                    } else {
                        bat 'py -3 -m unittest -v test_form.py'
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: All pipeline stages completed.'
        }

        failure {
            echo 'FAILURE: Check the Console Output for errors.'
        }

        always {
            echo 'Jenkins Pipeline execution completed.'
        }
    }
}