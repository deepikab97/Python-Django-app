pipeline {
    agent 'Agent_linux_deepika'

    environment {
        // Define environment variables, e.g., for database connection
        
        DB_PORT = '5432'
        DB_NAME = 'postgres'
        DB_USER = 'postgres'
        DB_PASS = 'postgres'
    }


    stages {
        stage('Checkout') {
            steps {
                // Check out your source code from a version control system like Git.
                git branch: "master", "develop"
                url: 'https://github.com/deepikab97/Python-Django-app.git'
                
            }
        }
        
        stage('Install Dependencies') {
            steps {
                // Use a virtual environment to isolate Python dependencies.
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Database Setup') {
            steps {
                // Initialize the PostgreSQL database (create schema, run migrations, etc.)
                sh 'python3 manage.py makemigrations'
                sh 'python3 manage.py migrate'
                
            }
        stage('Run Tests') {
            steps {
                // Run your Python tests.  
    
                sh 'python3 manage.py test'
                
            }
        }
        
        stage('Build and Package') {
            steps {
                // Build your Python application (e.g., create a distribution package).
                sh 'python setup.py sdist bdist_wheel'
            }
        }

        stage('Publish Artifacts') {
            steps {
                // Publish your Python package (e.g., to a package repository).
                // Replace the following line with your actual publish command.
                sh 'twine upload dist/*'
            }
        }
        
        stage('Cleanup') {
            steps {
                // Clean up any temporary files or resources.
                sh 'deactivate' // Deactivate the virtual environment
            }
        }
    }

    post {
        success {
            // Actions to perform when the pipeline is successful (e.g., notifications).
        }
        failure {
            // Actions to perform when the pipeline fails (e.g., notifications or rollback).
        }
    }
}
}
