pipeline{
    agent any
    
    environment {
        VENV_DIR = 'venv'
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
    }
        

}