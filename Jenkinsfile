pipeline {
	agent any

	parameters{
		// booleanParam(name: 'executeTests',defaultValue: true, description:"")
		choice(
			name: 'REQUESTED_ACTION',
            choices: ['Build' , 'Test', "Deploy"],
            description: '')
	}
	environment{
		FLASK_APP= 'appl.py'
		// SERVER_CREDENTIALS = credentials('credentialID')
		//credential binding plugin
	}
	stages {
		stage("build"){
			steps{
				// sh "jenkins  ALL= NOPASSWD: ALL"
				sh	"sudo yum install python-virtualenv -y"
				sh	"python3 -m venv venv"
				sh	"source venv/bin/activate"
				sh "python3 -m pip install -r requirements.txt --user"
				sh "python3 -m pip install pylint"
				echo " BUILD stage completed Successfully"
		
			}
		}
		stage("test"){
			when{
				expression {params.REQUESTED_ACTION == 'Test' ||params.REQUESTED_ACTION == 'Deploy'}
			}
			steps{
				sh "python3 -m pylint --rcfile google.cfg --reports=n --disable=deprecated-module appl.py --exit-zero"
				// sh "python3 -m pylint appl.py"
				sh "python -m unittest discover tests/"				
				echo " Test stage completed Successfully"
				// sh " shell script"
			}
		}
		stage("deploy"){
			when{
				expression {params.REQUESTED_ACTION == 'Deploy'}
			}
			steps([$class: 'BapSshPromotionPublisherPlugin']) {
				sh "sudo yum update"
				sh "pip install flask"
				sh "pip install pylint"
				// sshPublisher(
				// 	continueOnError: false, failOnError: true,
				// 	publishers: [
				// 		sshPublisherDesc(
				// 			configName: "aishwarya-jenkins-deployment",
				// 			verbose:  	true,
				// 			transfers:[
				// 				sshTransfer (execCommand: "/bin/rm -rf jenkins-aws")
				// 				sshTransfer (execCommand: "/bin/mkdir jenkins-aws")
				// 				sshTransfer (sourceFiles:  "*",)
				// 				sshTransfer (execCommand: "/bin/mkdir jenkins-aws/templates")
				// 				sshTransfer (sourceFiles: "templates/*",)
				// 				sshTransfer (execCommand: "/bin/mkdir jenkins-aws/static")
				// 				sshTransfer (sourceFiles: "static/*",)
				// 				sshTransfer (execCommand: "/bin/mkdir jenkins-aws/tests")
				// 				sshTransfer (sourceFiles: "tests/*",)
				// 				sshTransfer (execCommand: "/bin/python3 -m venv venv")
				// 				sshTransfer (execCommand: ". venv/bin/activate")
				// 				sshTransfer (execCommand: "/bin/pip3 install -r requirements.txt --user")
				// 				sshTransfer (execCommand: "/bin/python3 appl.py &")
				// 			]
				// 			)
				// 	]
				// 	)
			}
		}




	}
	post{
		always{
			// always executed
			// cleanup
			deleteDir()
			cleanWs()
			echo "All Executed"

		}
		success {
			echo " Successfully"
		}
		failure {
			echo " with failures in the pipeline"

		}

	}
}
