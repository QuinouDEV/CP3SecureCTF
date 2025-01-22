pipeline {
    agent none
    stages {
        stage("Build & Analyse avec SonarQube") { 
            tools {
                maven 'Maven' // Nom défini dans Global Tool Configuration
            }
            steps { 
                script {
                    sh 'mvn clean package sonar:sonar'
                }
            }
        }
    }
}
