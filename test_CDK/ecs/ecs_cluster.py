from constructs import Construct
from aws_cdk import (
    aws_autoscaling as autoscaling,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    Stack,
    CfnOutput,
)


class ECSCluster(Stack):
    def __init__(self, scope: Construct, id: str, vpc, **kwargs) -> None:
        super().__init__(scope, id, *kwargs)

        self.cluster = ecs.Cluster(self, "EcsCluster", vpc=vpc)

        CfnOutput(self, "Cluster", value=self.cluster.cluster_name)