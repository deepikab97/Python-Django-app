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
     // scannerHome = tool 'sonarscanner'
        
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

     stage('Code Coverage') {
        steps {
            script {
            def currentDirectory = pwd()
            echo "Current working directory is: ${currentDirectory}"
            }
         // Generate code coverage.  
          sh 'python3 -m venv venv'
          sh '. venv/bin/activate' 
          sh 'pip3 install -r requirements.txt' 
          sh 'python3 manage.py makemigrations'
          sh 'python3 manage.py migrate'  

            
          sh 'pip3 install coverage'
          sh 'coverage run manage.py test'       // Run tests with coverage 
          sh 'coverage xml -i -o ${currentDirectory}/coverage.xml'   // Generate the coverage report  

        }
      }
        
     stage('Sonarqube Analysis') {
         // def scannerHome = tool name: 'sonarscanner';
         steps {
             withSonarQubeEnv(installationName:'Sonarqube',credentialsId:'Sq-Deepika') {
            // some block 
                 echo 'Inside Soanrqube'
                sh '/home/akshay/sonar-scanner-4.4.0.2170-linux/bin/sonar-scanner'
            }
             timeout(time: 10, unit: 'MINUTES') {
                 waitForQualityGate abortPipeline: true
                 echo 'inside sonar environment'
                      }
                }
           }   

      
      
    }

   
}
