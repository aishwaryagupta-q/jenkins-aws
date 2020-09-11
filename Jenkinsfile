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
				sh	"sudo yum install python-virtualenv -y"
				sh	"python3 -m venv venv"
				sh	"source venv/bin/activate"
				sh "python3 -m pip install -r requirements.txt --user"
				// sh "sudo python -m pip install pylint"
				sh "sudo yum install xmlrunner junit -y"
				// sh "sudo yum install -y pylint"
				//  change
				// sh "export PATH=$HOME/.local/bin:$PATH"
				sh "python3 -m pip install pylint"
				echo " BUILD stage completed Successfully"
		
			}
		}
		stage("test"){
			when{
				expression {params.REQUESTED_ACTION == 'Proceed'}
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
