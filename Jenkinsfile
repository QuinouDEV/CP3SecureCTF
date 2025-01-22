pipeline {
    agent none
    stages {
        stages("Build & Analyse avec SonarQube") { 
            agent any
            steps { 
              script {
                sh 'mnv clean package sonar:sonar'
              }
            }
        }
    }
}
