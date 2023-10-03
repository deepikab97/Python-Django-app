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
          sh 'python3 -m venv venv'
          sh '. venv/bin/activate'
          sh 'pip3 install -r requirements.txt'
      }
    }
      stage('Database Setup') {
        steps {
          // Initialize the PostgreSQL database (create schema, run migrations, etc.)
          sh 'python3 manage.py makemigrations'
          sh 'python3 manage.py migrate'
        }
      }
      stage('Unit Testing') {
        steps {
         // Run your Python tests.  
          sh 'python3 manage.py test'
        }
      }
     
     stage('Sonarqube') {
         steps {
             withSonarQubeEnv(credentialsId: 'deepikaSonarcloudToken', installationName: 'SonarCloud ') {
            // some block
                sh 'sonar-scanner'
            }
             timeout(time: 10, unit: 'MINUTES') {
                 waitForQualityGate abortPipeline: true
                 echo 'inside sonar environment'
                      }
                }
           }   

      
      
    }

   
}
