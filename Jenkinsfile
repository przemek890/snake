pipeline {
    agent any

    environment {
        GIT_REPO = 'https://github.com/przemek890/snake.git'
        GIT_CRED_ID = 'dad47e07-a5f8-46fc-8c3d-ba0d5ff7ef2f'
        GIT_BRANCH = 'master'
    }

    triggers {
        pollSCM('* * * * *')
    }

    stages {
        stage('Clean') {
            steps {
                cleanWs()
                sh '''
                   # Usuń wszystkie kontenery Docker, jeśli istnieją
                   if docker ps -a -q | read; then
                     docker stop $(docker ps -a -q)
                     docker rm $(docker ps -a -q)
                   fi

                   # Usuń wszystkie obrazy Docker, jeśli istnieją
                   if docker images -q | read; then
                     docker rmi $(docker images -q)
                   fi

                   docker ps -a
                   docker images
                '''
            }
        }



        stage('Collect') {
             steps {
                git branch: "${GIT_BRANCH}", credentialsId: "${GIT_CRED_ID}", url: "${GIT_REPO}"
                script {
                    if (!fileExists('log')) {
                        sh 'mkdir log'
                    }
                }
             }


        stage('Build') {
            steps {
                echo "Building..."
                sh '''
                cd Snake_files/build
                docker build -t snake_builder:latest --build-arg GIT_TOKEN=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 -f ./Dockerfile .
                docker run -d --name snake_builder -v ./artifacts:/snake/dist snake_builder:latest
                docker logs snake_builder > log/log_builder.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo "Testing..."
                sh '''
                cd Snake_files/tests
                docker build -t snake_tester:latest -f ./Dockerfile .
                docker run -d --name snake_tester -v ./artifacts:/snake/dist snake_tester:latest
                docker logs snake_tester > log/log_tester.txt
                '''
            }
        }
        stage('Deploy') {
            steps {
                echo "Deploying..."
                sh '''
                cd Snake_files/deploy
                docker build -t snake_deployer:latest -f ./Dockerfile .
                docker run -d --name snake_deployer -v ./artifacts:/snake/dist -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=host.docker.internal:0 snake_deployer:latest
                docker logs snake_deployer > log/log_deployer.txt
                '''
            }
        }

        stage('Publish') {
            steps {
                echo "Publishing..."
                sh '''
                TIMESTAMP=$(date +%Y%m%d%H%M%S)
                cd Snake_files/
                ls -l
                tar -czf Artifact_$TIMESTAMP.tar.gz ./
                '''
                echo "Archiving the artifact..."
                archiveArtifacts artifacts: 'Artifact_*.tar.gz', fingerprint: true
            }
        }
    }
}
