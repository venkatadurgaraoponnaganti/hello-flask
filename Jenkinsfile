pipeline{
agent any
stages{
	stage('checkout'){
		steps{
git branch:'main' url:'https://github.com/venkatadurgaraoponnaganti/hello-flask'
}}
stage('install dep'){
steps{
sh '''pip install -r requirements.txt
'''

}}

stage('deploy'){
steps{
sh '''
docker build -t hello-flask-1 .
docker run -d -p 5000:5000 hello-flask-1 '''
}
}
}
}
