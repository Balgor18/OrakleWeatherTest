from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecr as ecr,
)
from constructs import Construct

class TestEcsStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        vpc = ec2.Vpc(self, "VpcTest")

        cluster = ecs.Cluster(self, "ClusterTest", vpc=vpc)

        repository = ecr.Repository.from_repository_name(self, "RepoApi", "pythonapi")

        task_definition = ecs.FargateTaskDefinition(self, "LaunchApi")

        container = task_definition.add_container(
            "apiContainer",
            image=ecs.ContainerImage.from_ecr_repository(repository),
            memory_limit_mib=512,
        )

        ecs.FargateService(self, "MyFargateService",
                           cluster=cluster,
                           task_definition=task_definition
                          )
