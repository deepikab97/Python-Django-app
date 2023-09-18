pipeline {
    agent {
        label 'Agent_linux_deepika'
    }
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
        // Use a virtual environment to isolate Python dependencies
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
      
      
      
    }

   }
}
