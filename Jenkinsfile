pipeline {
    agent any

    environment {
        GIT_REPO = 'https://github.com/przemek890/snake.git'
        GIT_CRED_ID = 'dad47e07-a5f8-46fc-8c3d-ba0d5ff7ef2f'
        GIT_BRANCH = 'master'
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-token')
        HOST_IP = '192.168.100.83:0' // may change
    }

    triggers {
        pollSCM('* * * * *')
    }

    stages {
        stage('Collect') {
            steps {
                cleanWs()
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
                docker run --name snake_builder -v ./artifacts:/snake/dist snake_builder:latest
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
                docker run --name snake_tester -v ./artifacts:/snake/dist snake_tester:latest
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
                docker run --name snake_deployer -v ./artifacts:/snake/dist -e DISPLAY="${HOST_IP}" snake_deployer:latest
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
                //////////////////////////////////////////////////////////////////
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                sh 'docker tag snake_deployer:latest przemek899/snake_deployer:latest'
                sh 'docker push przemek899/snake_deployer:latest'
                sh 'docker logout'
                //////////////////////////////////////////////////////////////////
                emailext (
                    from: 'kikpl899@gmail.com',
                    body: "Please find the attached log files for Job '${env.JOB_NAME}' (${env.BUILD_NUMBER}).\nHOST_IP = '${HOST_IP}'",
                    subject: "Job '${env.JOB_NAME}' (${env.BUILD_NUMBER}) - Log Files",
                    to: 'przemek.899@wp.pl',
                    attachmentsPattern: '**/Snake_files/log/*.txt'
                )
            }
        }
    }
}
