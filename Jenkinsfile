pipeline{
    agent any

    stages{
        stage('Cloning github repo to jenkins'){
            steps{
                script{
                    echo 'Cloning github repo to jenkins.............'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/nirajp728/hotel_reservation_project.git']])
                }
            }
        }
    }

}