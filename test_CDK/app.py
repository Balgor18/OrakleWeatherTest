#!/usr/bin/env python3
import aws_cdk as cdk

from test_cdk.test_cdk_stack import TestCdkStack
from vpc.vpc_stack import TestVpcStack
from ecs.ecs_cluster import ECSCluster
from ecs.ecs_service import ECSService

app = cdk.App()
stack1 = TestCdkStack(app, "TestCdkStack")

vpc_stack = TestVpcStack(app, "VPC-Stack")
cluster_stack = ECSCluster(app, "ECS-Stack", vpc=vpc_stack.vpc)
service_stack = ECSService(
    app, "ECS-Service", vpc=vpc_stack.vpc, cluster=cluster_stack.cluster
)

app.synth()