pipeline {
	agent any

	parameters{
		// User Manually Chooses Wherether to Build , Build and Test , Or to Build, Test and Deploy
		choice(
			name: 'REQUESTED_ACTION',
            choices: ['Build' , 'Test', "Deploy"],
            description: '')
		}
	}
	stages {
		stage("build"){
			steps{
				// sh "jenkins  ALL= NOPASSWD: ALL"
				// Installing and configuring Virtualenv
				sh	"sudo yum install python-virtualenv -y"
				sh	"python3 -m venv venv"
				sh	"source venv/bin/activate"
				// Installing Requirements.txt file
				sh "python3 -m pip install -r requirements.txt --user"
				sh "python3 -m pip install pylint"
				echo " BUILD stage completed Successfully"
		
			}
		}
		stage("test"){
			// Expression for checking User-Input in the firs step , 2 vvalues
			when{
				expression {params.REQUESTED_ACTION == 'Test' ||params.REQUESTED_ACTION == 'Deploy'}
			}
			steps{
				// using custom Google COnfiguration file with Pulint
				sh "python3 -m pylint --rcfile google.cfg --reports=n --disable=deprecated-module appl.py --exit-zero"
				// Running Unittest on Networking Aspects
				sh "python -m unittest discover tests/"				
				echo " Test stage completed Successfully"
			}
		}
		stage("deploy"){
			// Expression to check if User asked for deployment
			when{
				expression {params.REQUESTED_ACTION == 'Deploy'}

			}
			// Using Publish Over ssh Plugin
			steps([$class: 'BapSshPromotionPublisherPlugin']) {

				sshPublisher(
					continueOnError: false, failOnError: true,
					publishers: [
						sshPublisherDesc(
							configName: "aishwarya-jenkins-deployment",
							verbose:  	true,
							transfers:[
								// Clearing Dir and making new
								sshTransfer (execCommand: "/bin/rm -rf jenkins-aws")
								sshTransfer (execCommand: "/bin/mkdir jenkins-aws")
								// Copying Data to EC2 Deploy instance t
								sshTransfer (sourceFiles:  "*",)
								sshTransfer (execCommand: "/bin/mkdir jenkins-aws/templates")
								// zcopying HTML Files
								sshTransfer (sourceFiles: "templates/*",)
								// Copying CSS files
								sshTransfer (execCommand: "/bin/mkdir jenkins-aws/static")
								sshTransfer (execCommand: "/bin/mkdir jenkins-aws/static/css")
								sshTransfer (sourceFiles: "static/css/*",)
								sshTransfer (execCommand: "/bin/mkdir jenkins-aws/static/js")
								sshTransfer (sourceFiles: "static/js/*",)
								sshTransfer (sourceFiles: "static/*",)
								// Copying Test Scripts
								sshTransfer (execCommand: "/bin/mkdir jenkins-aws/tests")
								sshTransfer (sourceFiles: "tests/*",)
								sshTransfer (execCommand: "/bin/python3 -m venv venv")
								sshTransfer (execCommand: ". venv/bin/activate")
								sshTransfer (execCommand: "/bin/pip3 install -r requirements.txt --user")
								sshTransfer (execCommand: "/bin/python3 appl.py &")
							]
							)
					]
					)
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
