node {
    def app
    stage('Clone repository') {
        checkout scm
    }
    stage('Build image') {
       app = docker.build("MarkoMinovski/devops_hw4")
    }
    stage('Push image') {
        docker.withRegistry('https://registry.hub.docker.com', '639d499a-0b82-49b5-9dd1-b96f088ceab8') {
            app.push("${env.BRANCH_NAME}-${env.BUILD_NUMBER}")
            app.push("${env.BRANCH_NAME}-latest")
            // signal the orchestrator that there is a new version
        }
    }
}