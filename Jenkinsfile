pipeline {
  agent any

  stages {
    stage('Hello') {
      steps {
        echo "Hey Lakita — GitHub ↔ Jenkins is live! 🚀"
      }
    }
    stage('List repo files') {
      steps {
        sh 'pwd && ls -la'
      }
    }
  }
  post {
    always {
      echo "Build finished."
    }
  }
}
