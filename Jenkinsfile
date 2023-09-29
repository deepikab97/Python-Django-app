pipeline {
    agent {
        label 'Agent_linux_akshay'
    }
    environment {
    // Define environment variables, e.g., for database connection
      DB_PORT = '5432'
      DB_NAME = 'postgres'
      DB_USER = 'postgres'
      DB_PASS = 'postgres'
   }

    stages {

      stage('Install Dependencies') {
        steps {
          // Use a virtual environment to isolate Python dependencies
          //sh 'python -m venv venv'
          //sh '. venv/bin/activate'
          sh 'pip install -r requirements.txt'
      }
    }
      stage('Database Setup') {
        steps {
          // Initialize the PostgreSQL database (create schema, run migrations, etc.)
          sh 'python manage.py makemigrations'
          sh 'python manage.py migrate'
        }
      }
      stage('Run Tests') {
        steps {
         // Run your Python tests.  
          sh 'python manage.py test'
        }
      }

        
      
      
    }

   
}
