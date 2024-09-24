# Exercice Orakle Weather


## Step 1 Containerization

Soirée du 23 Septembre :

Création du projet avec `compose.yaml` et `Dockerfile`. Pour automatiser l'installation des requirements j'ai installer en amont dans le docker le package python [pipreqs](https://pypi.org/project/pipreqs/) qui me permet de generer automatiquement le fichier requirements.txt. Un fois recup je le place dans config.

Ensuite, j'ai commencé a faire le swagger grace a ça [DocsFastApi](https://fastapi.tiangolo.com/how-to/configure-swagger-ui/).

## Step2 Prise en main AWS

[Getting started](https://aws.amazon.com/fr/getting-started/onboarding-to-aws/)
[CDK Getting started](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html)
https://github.com/aws-samples/aws-cdk-examples/blob/main/python/docker-app-with-asg-alb/README.md
https://www.youtube.com/watch?v=T-H4nJQyMig
https://docs.aws.amazon.com/fr_fr/cdk/v2/guide/home.html



Contre temps
Probleme sur mon compte AWS un ghost topic est apparu impossible de le supprimer. Il n'avais plus de nom plus d'id et menpeche de faire disparaitre mes Piles.
J'ai donc recree un compte.

### Debut du test avec CDK et ECS
[Video d'aide](https://www.youtube.com/watch?v=sqlM20ZZbSg)







<!-- Note pour lancer
cdk synth
cdk bootstrap
cdk deploy [--all]
 -->