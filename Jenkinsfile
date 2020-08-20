pipeline {
    environment{
        registry = "leexha/redis-demo"
        registyCredential = 'dockerhub'
        dockerImage = ''
    }

    agent any
    
    parameters {
        string(defaultValue: "latest", description: 'IMAGE_TAG', name: 'IMAGE_TAG')
        string(defaultValue: "https://github.com/leeadh/redis-example.git", description: 'GITHUB_URL', name: 'GITHUB_URL')
    }    
    

    stages {

        stage('Git clone'){
            steps{
                git branch: 'test', url: "${params.GITHUB_URL}"
            }
            
        }




        stage ('Building image'){
            steps{
                script{
                    dockerImage = docker.build(registry + ":${params.IMAGE_TAG}"," .")

                }
            }

        }

        stage('Test application'){
            steps{
                script{
                    dockerImage.inside {
                        sh 'python server/tests/testapp.test'
                    }
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
        
        stage('Deploy new pods') {
            steps{
                sh "cat kubernetes/deployment_template.yaml | sed \"s/{{IMAGE_TAG}}/${params.IMAGE_TAG}/g\" | kubectl apply -f -"
            }
        }

        stage('Get new pods') {
            steps{
                sh "kubectl get pods"
            }
        }

    }
}


