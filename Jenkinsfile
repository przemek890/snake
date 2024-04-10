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

        stage('Collect') {
            steps {
                git branch: "${GIT_BRANCH}", credentialsId: "${GIT_CRED_ID}", url: "${GIT_REPO}"
                sh '''
                    chmod +x clear.sh
                    ./clear.sh
                '''
            }
        }


        stage('Build') {
            steps {
                echo "Building..."
                sh '''
                cd Snake_files
                docker build -t snake_builder:latest --build-arg GIT_TOKEN=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 -f ./build/Dockerfile .
                docker run -d --name snake_builder -v ./artifacts:/snake/dist snake_builder:latest
                echo docker logs snake_builder
                docker logs snake_builder > ./log/log_builder.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo "Testing..."
                sh '''
                cd Snake_files
                docker build -t snake_tester:latest -f ./tests/Dockerfile .
                docker run -d --name snake_tester -v ./artifacts:/snake/dist snake_tester:latest
                docker logs snake_tester > ./log/log_tester.txt
                '''
            }
        }
        stage('Deploy') {
            steps {
                echo "Deploying..."
                sh '''
                cd Snake_files
                docker build -t snake_deployer:latest -f ./deploy/Dockerfile .
                docker run -d --name snake_deployer -v ./artifacts:/snake/dist -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=host.docker.internal:0 snake_deployer:latest
                docker logs snake_deployer > ./log/log_deployer.txt
                '''
            }
        }

        stage('Publish') {
            steps {
                echo "Publishing..."
                sh '''
                TIMESTAMP=$(date +%Y%m%d%H%M%S)
                tar -czf Artifact_$TIMESTAMP.tar.gz ./Snake_files/artifacts ./Snake_files/tests ./Snake_files/build ./Snake_files/deploy ./Snake_files/log
                '''
                echo "Archiving the artifact..."
                archiveArtifacts artifacts: 'Artifact_*.tar.gz', fingerprint: true
            }
        }
    }
}
