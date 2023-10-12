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
      def slackResponse = slackSend(channel: "jenkins", message: "Build Started: ${env.JOB_NAME} ${env.BUILD_NUMBER}")  
         
   }

    stages {
         stage('Checkout'){
             steps{
                checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/deepikab97/Python-Django-app.git']])
		     
             }
		 
         }
      
      	stage('Install Dependencies') {
        	steps {
        	  // Use a virtual environment to isolate Python dependencies
        	  sh '''python3 -m venv venv
          	  . venv/bin/activate
        	    python --version
          	  pip3 install -r requirements.txt
          	  '''  
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
          sh '''python3 -m venv venv
              . venv/bin/activate
              python --version 
              pip3 install -r requirements.txt 
              python3 manage.py makemigrations
              python3 manage.py migrate
              python3 manage.py test
              pip3 install coverage
              coverage run manage.py test       
              coverage xml -o coverage.xml  ''' // Generate the coverage report  

        }
      }
        
     stage('Sonarqube Analysis') {
         // def scannerHome = tool name: 'sonarscanner';
         steps {
             withSonarQubeEnv(installationName:'Sonarqube',credentialsId:'Sonarqube-Token-Deepika') {
            // some block 
                 echo 'Inside Soanrqube'
                sh '/home/akshay/sonar-scanner-4.4.0.2170-linux/bin/sonar-scanner'
            }
	   slackSend(channel: slackResponse , message: "Sonar Analysis done : ${env.JOB_NAME} ${env.BUILD_NUMBER}") 
             timeout(time: 10, unit: 'MINUTES') {
                 waitForQualityGate abortPipeline: true
                 echo 'inside sonar environment'
                      }
                }
           }   

        

        stage('Artifact push to Jfrog'){
            steps{
                sh 'docker image build -t 172.27.59.80:8082/alm-jenkins-python-cicd-pipeline-deepika/python-djangoapp:${BUILD_NUMBER} .'
                sh  'docker login -u $JFROG_USER -p $JFROG_PASSWORD http://172.27.59.80:8082/'
                sh  'docker push  172.27.59.80:8082/alm-jenkins-python-cicd-pipeline-deepika/python-djangoapp:${BUILD_NUMBER}'  
            }
        }

        stage('Deploy application') {
          steps {
         // Build the application with docker .  
          sh 'docker rm -f db djangoapp'
          sh 'docker-compose up -d'  
          slackSend(channel:"jenkins" , message: "Docker containers are running successfully : ${env.JOB_NAME} ${env.BUILD_NUMBER}")  
             }
         }

        stage ('Trivy scan') {
		    steps{
                sh 'curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/html.tpl > html.tpl'
                sh  'trivy image --format template --template "@./html.tpl" -o report.html 172.27.59.80:8082/alm-jenkins-python-cicd-pipeline-deepika/python-djangoapp:${BUILD_NUMBER}'

            } 
   	}
            
      	stage('Reports'){
	   steps{
		publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, keepAll: false, reportDir: '.', reportFiles: 'report.html', reportName: 'Trivy Scan', reportTitles: '', useWrapperFileDirectly: true])   
	   }
	   }
      
    }

   
}
