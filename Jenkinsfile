pipeline {
	agent any
	// tools {
	// 	// jdk 'name of installation in jenkins'
	// }
	parameters{
		// booleanParam(name: 'executeTests',defaultValue: true, description:"")
		choice(
			name: 'REQUESTED_ACTION',
            choices: ['Proceed' , 'Stop'],
            description: '')
	}
	environment{
		FLASK_APP= 'appl.py'
		// SERVER_CREDENTIALS = credentials('credentialID')
		//credential binding plugin
	}
	stages {
		stage("build"){
			when{
				expression {params.REQUESTED_ACTION == 'Proceed'}
			}
			steps{
				// sh "jenkins  ALL= NOPASSWD: ALL"
				sh "sudo apt-get update -y"
				sh "sudo apt-get install python3 -y"
				sh	"sudo apt-get install python3-venv -y"
				sh	"python3 -m venv venv"
				sh	". venv/bin/activate"
				sh "pip3 install -r requirements.txt --user"
				// sh "sudo easy_install pip"
				sh "sudo apt-get install -y pylint"
				//  change
				// sh "export PATH=$HOME/.local/bin:$PATH"
				// sh "python3 --version"
				echo " BUILD stage completed Successfully"
		
			}
		}
		stage("test"){
			when{
				expression {params.REQUESTED_ACTION == 'Proceed'}
			}
			steps{
				sh "pylint --rcfile google.cfg --reports=n --disable=deprecated-module appl.py || return 0 "
				sh "python3 -m unittest tests/test_routes.py"				
				echo " Test stage completed Successfully"
				// sh " shell script"
			}
		}
		stage("deploy"){
			when{
				expression {params.REQUESTED_ACTION == 'Proceed'}
			}
			steps{
				// sh "startup_script.sh"
				// sh "gcloud compute scp "			
				echo " Test stage completed Successfully"
				// sh " shell script"
			}
		}




	}
	post{
		always{
			// always executed
			echo " always post"
			junit 'test-reports/*.xml'
			deleteDir()
		}
		success {
			echo "success post"
		}
		failure {
			echo "failure post"

		}

	}
}
