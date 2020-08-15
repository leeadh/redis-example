pipeline {
    environment{
        registry = "leexha/redis-demo"
        registyCredential = 'dockerhub'
        dockerImage = ''
    }

    agent any
    
    parameters {
        string(defaultValue: "latest", description: 'IMAGE_TAG', name: 'IMAGE_TAG')
    }    
    

    stages {

        stage('Git clone'){
            steps{
                git branch: 'test', url: 'https://github.com/leeadh/redis-example.git'
            }
            
        }
        
        stage ('Building image'){
            steps{
                script{
                    dockerImage = docker.build(registry + ":${params.IMAGE_TAG}"," .")

                }
            }

        }


        stage ('Pushing to Docker Hub'){
            steps{
                script{
                    println dockerImage.id
                    docker.withRegistry('',registyCredential){
                        
                        dockerImage.push()
                    }
                }
            }

        }
        
        stage('List pods') {
            steps{
                sh 'kubectl get pods'
            }
        }

    }
}


