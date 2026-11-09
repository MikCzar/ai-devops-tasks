pipeline {
    agent any
    
    environment {
        // Nazwa obrazu i dane rejestru (możesz dostosować lub przenieść do Jenkins Credentials)
        DOCKER_IMAGE = 'twoj-login-rejestru/my-node-app'
        CREDENTIALS_ID = 'docker-hub-credentials' // ID danych uwierzytelniających w Jenkinsie
    }

    stages {
        stage('Checkout') {
            steps {
                // Pobranie kodu źródłowego z repozytorium
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                // Instalacja zależności (zalecane użycie npm ci dla stabilności w CI/CD)
                sh 'npm ci'
            }
        }

        stage('Run Tests') {
            steps {
                // Uruchomienie testów jednostkowych
                sh 'npm test'
            }
        }

        stage('Build App') {
            steps {
                // Budowanie aplikacji (np. kompilacja TypeScript, bundler itp.)
                sh 'npm run build'
            }
        }

        stage('Build Docker Image') {
            steps {
                // Budowanie obrazu Docker z unikalnym tagiem opartym na numerze builda
                script {
                    app = docker.build("${env.DOCKER_IMAGE}:${env.BUILD_NUMBER}")
                }
            }
        }

        stage('Publish Docker Image') {
            steps {
                // Logowanie do rejestru Docker i wypchnięcie obrazu
                script {
                    docker.withRegistry('https://index.docker.io/v1/', "${env.CREDENTIALS_ID}") {
                        app.push("${env.BUILD_NUMBER}")
                        app.push("latest") // Opcjonalnie: tagowanie również jako latest
                    }
                }
            }
        }
    }

    post {
        always {
            // Czyszczenie środowiska po zakończeniu (opcjonalnie)
            cleanWs()
        }
        success {
            echo 'Pipeline zakończył się sukcesem!'
        }
        failure {
            echo 'Wystąpił błąd podczas wykonywania pipeline.'
        }
    }
}