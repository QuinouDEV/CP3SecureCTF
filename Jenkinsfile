pipeline {
    agent none
    stages {
        stage("Build & Analyse avec SonarQube") { 
            agent {
                label 'maven-agent' // Label défini pour cet agent
            }
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
