pipeline {
  agent any
  environment {
    IMAGE     = "netpol-flask"   // local image name
    HOST_PORT = "8081"           // port on your laptop
    APP_PORT  = "8080"           // port inside the container (matches app.py)
  }
  stages {
    stage('Checkout') {
      steps { checkout scm }
    }
    stage('Build Docker image') {
      steps {
        sh 'docker build -t $IMAGE .'
      }
    }
    stage('Run container') {
      steps {
        sh '''
          docker rm -f netpol-app || true
          docker run -d --name netpol-app -p ${HOST_PORT}:${APP_PORT} $IMAGE
        '''
      }
    }
  }
}

