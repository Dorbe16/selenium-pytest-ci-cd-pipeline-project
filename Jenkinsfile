pipeline {
  agent any

  parameters {
    choice(name: 'BROWSER', choices: ['chrome','firefox'], description: 'Browser')
    booleanParam(name: 'RUN_ON_GRID', defaultValue: 'true', description: 'Start & use Selenium Grid (Docker)')
    string(name: 'GRID_URL', defaultValue: 'http://localhost:4444/wd/hub', description: 'Start & use Selenium Grid (Docker)')
    booleanParam(name: 'PARALLEL', defaultValue: 'true', description: 'Run tests in parallel (xdist)')
    string(name: 'WORKSPACE', defaultValue: "C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\qa-automation\\", description: '')
    booleanParam(name: 'CI', defaultValue: 'true', description: '')
  }

  environment {
    VENV = ".venv"
    REPORTS = "reports"
    JUNIT_XML = "reports\\junit\\results.xml"
    ALLURE_DIR = "reports\\allure"
  }

  options {
    timeout(time: 30, unit: 'MINUTES')
    buildDiscarder(logRotator(numToKeepStr: '20'))
  }

  stages {

    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Setup Environment') {
      steps {
        script {
          if (isUnix()) {
            sh '''
              # ex: python3 -m venv venv
              # . venv/bin/activate
              # pip install -r requirements.txt
            '''
          } else {
            bat
                """
              REM ex: python -m venv venv
              REM call venv\\Scripts\\activate
              REM pip install -r requirements.txt

              python -m venv C:\ProgramData\Jenkins\.jenkins\workspace\qa-automation\.venv
              call .venv/Scripts/activate
              python -m pip install --upgrade pip
              pip install -r requirements.txt



              mkdir reports
              mkdir reports\junit
              mkdir reports\allure
              """
          }
        }
      }
    }

    stage('Start Services') {
      steps {
        script {
          if (isUnix()) {
            sh '''
              # ex: docker compose -f docker-compose.yml up -d
            '''
          } else {
            bat """
              IF /I "%RUN_ON_GRID%"=="true" docker compose -f infra/docker-compose-grid.yml up -d
              echo Waiting for Selenium Grid to be ready...
              timeout /t 15 /nobreak
              """
          }
        }
      }
    }

    stage('Run Tests') {
      steps {
        script {
          if (isUnix()) {
            sh '''
              # ex: pytest --some-options
            '''
          } else {
            bat """
              pytest -q -n 2 --browser=%BROWSER% --grid=%GRID_URL% --junitxml=reports\junit\results.xml
              """
          }
        }
      }
    }

    stage('Stop Services') {
      steps {
        script {
          if (isUnix()) {
            sh '''
              # ex: docker compose -f docker-compose.yml down
            '''
          } else {
            bat """
              IF /I "%RUN_ON_GRID%"=="true" docker compose -f infra/docker-compose-grid.yml down
              """
          }
        }
      }
    }

  } // end stages

  post {
    always {
      archiveArtifacts artifacts: 'reports\**, allure-report\**, reports\junit\results.xml', allowEmptyArchive: true
    }
    success {
      echo 'Build success!'
      junit testResults: "${env.JUNIT_XML}"
      allure results: [[path: "${env.ALLURE_DIR}"]]
    }
    failure {
      echo 'Build failed!'
      junit testResults: "${env.JUNIT_XML}"
      allure results: [[path: "${env.ALLURE_DIR}"]]
    }
  }
}