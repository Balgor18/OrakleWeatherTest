# Exercice Orakle Weather


## Step 1 Containerization

Création du projet avec `compose.yaml` et `Dockerfile`. Pour automatiser l'installation des requirements j'ai installer en amont dans le docker le package python [pipreqs](https://pypi.org/project/pipreqs/) qui me permet de generer automatiquement le fichier requirements.txt. Un fois recup je le place dans config.

Ensuite, j'ai commencé a faire le swagger grace a ça [DocsFastApi](https://fastapi.tiangolo.com/how-to/configure-swagger-ui/).

## Step2 Prise en main AWS

[Getting started](https://aws.amazon.com/fr/getting-started/onboarding-to-aws/)
[CDK Getting started](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html)

Contre temps
Probleme sur mon compte AWS un ghost topic est apparu impossible de le supprimer. Il n'avais plus de nom plus d'id et menpeche de faire disparaitre mes Piles.
J'ai donc recree un compte.

### Debut du test avec CDK et ECS
[Video d'aide](https://www.youtube.com/watch?v=sqlM20ZZbSg)
Apres avoir essaye une premiere fois de mettre en place un first project avec ECS et CDK en python.
J'essaye mtn de le faire fonctionner avec l'image du project FastAPi.
[Docs Login docker](https://docs.aws.amazon.com/AmazonECR/latest/userguide/getting-started-cli.html#:~:text=To%20authenticate%20Docker%20to%20an,you%20want%20to%20authenticate%20to)

J'ai reussie a push mon Image docker. Plus de difficulte a me connecter avec docker login.
`NOT GOOD aws ecr get-login-password --region region | docker login --username AWS --password-stdin 1234-1234-1234.dkr.ecr.region.amazonaws.com`
`   GOOD  aws ecr get-login-password --region region | docker login --username AWS --password-stdin 123412341234.dkr.ecr.region.amazonaws.com`

Activer l'env virutel
`cd test_CDK && source .venv/bin/activate`
```bash
cdk synth
cdk bootstrap
cdk deploy [--all]
```


## Other useful Link
https://github.com/aws-samples/aws-cdk-examples/blob/main/python/docker-app-with-asg-alb/README.md
https://www.youtube.com/watch?v=T-H4nJQyMig
https://docs.aws.amazon.com/fr_fr/cdk/v2/guide/home.html
