pipeline {
  agent any
  stages {
    stage('Pull Repository') {
      steps {
        sh 'ls'
      }
    }

    stage('Test') {
      steps {
        echo 'Se inician las pruebas'
        sh '''#!/bin/bash
        export WORKSPACE=`pwd`
        # Create/Activate virtualenv
        python3 -m venv devenv
        source devenv/bin/activate
        # Install Requirements
        pip3 install -r Practica4/PaginaWeb/requirements.txt
        coverage run --source=\'Practica4/\' Practica4/PaginaWeb/manage.py test pagina
        coverage report -m
        coverage xml
        ls
        deactivate

        '''
        echo 'Se termino las pruebas'
      }
    }

    stage('ImageBuild-Producción') {
          when {
            branch 'main'
          }
          steps {
            echo 'Se ejecutara el deploy en producción.'
            sh 'docker build --no-cache --rm -t wygd/pagina-ansible:latest -f ./Dockerfile .'
            sh 'docker images'
          }
        }

      stage('Push-producción') {
        /*when {
          branch 'main'
        }*/
        environment {
          DOCKERHUB_CREDENTIALS = credentials('wygd-dockerhub')
        }
      steps {
        sh 'docker login -u $DOCKERHUB_CREDENTIALS_USR -p $DOCKERHUB_CREDENTIALS_PSW'
        sh 'docker push wygd/pagina-ansible:latest'
        sh 'docker logout'
      }
    }


    /*stage('Deploy-Production') {
      when {
        branch 'main'
      }
      steps {
        sh 'ls -a'
        sh 'ansible-playbook -i Ansible/inventory.produccion Ansible/docker_deploy_produccion.yaml'
      }
    }*/

  }
}