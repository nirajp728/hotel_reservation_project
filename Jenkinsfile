pipeline{
    agent any
    
    environment {
        VENV_DIR = 'venv'
        GCP_PROJECT = "scientific-air-428214-f7"
        GCLOUD_PATH = "/venv/jenkins_home/google-cloud-sdk/bin"
    }
    stages{
        stage('Cloning github repo to jenkins'){
            steps{
                script{
                    echo 'Cloning github repo to jenkins.............'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/nirajp728/hotel_reservation_project.git']])
                }
            }
        }
        stage('Setting up or vortuall envirnoment and installing dependencies'){
            steps{
                script{
                    echo 'Setting up or vortuall envirnoment and installing dependencies.............'
                    //Triple quotes ares used to write mutliple commands
                    sh '''
                    python -m venv ${VENV_DIR}
                    ${VENV_DIR}/bin/pip install --upgrade pip
                    ${VENV_DIR}/bin/pip install -e .
                    '''
                }
            }
        }
        stage('Building and pushing docker image to GCR'){
            steps{
                withCredentials([file(credentialsId : 'gcp-key', variable : 'GOOGLE_APPLICATION_CREDENTIALS')]){
                    script{
                       echo 'Building and pushing docker image to GCR.............'
                       //Triple quotes ares used to write mutliple commands
                       //Ensure gcloud is available within the path or not
                       //Acces GCP
                       //Set project 
                       //configure docker with GCR, in quiet mode so unnessecary logs aren't shown
                       //Building docker image
                       //Pushing docker image to GCP
                       sh '''
                       export PATH=$PATH-${GCLOUD_PATH}
                       gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
                       gcloud config set project ${GCP_project}
                       gcloud auth configure-docker --quiet

                       docker build -t gcr.io/${GCP_PROJECT}/ml-project-hotel-reservation:latest .

                       docker push gcr.io/${GCP_PROJECT}/ml-project-hotel-reservation:latest 
                       '''
                }
              }
            }
        }
    }
        

}