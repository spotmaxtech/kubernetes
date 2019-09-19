# All on Kubernetes
> Kubernetes是未来的Linux操作系统。

技术从业者必备的基础知识，不会在容器化环境工作的人5年内被淘汰，无论研发、运维与测试。

# Kubernetes体系
## 原生Kubernetes
![k8s_arch](./assets/k8s_arch.png)

## Amazon EKS
![eks_overview](./assets/eks_overview.png)

## EKS关键点
![eks_](./assets/eks_node_comm.png)

# All dockers
## 我们的应用构成
![spotmax_all](./assets/spotmax_all.png)

## 全部都是docker
![spotmax_docker](./assets/spotmax_docker.png)

## 日常工作流
*coding*
> 1. IDE开发
> 2. 测试
> 3. docker build & run

*testing*
> 部署到集成测试环境

*docker build*
> 1. 完成镜像构建与推送
> 2. 每个应用指定ECR与版本

*kubernetes release*
> 1. 编写chart
> 2. 编写ingress(是否单独制作
> 3. helm install ONE CLICK!)

## jenkins

## elasticsearch

## kibana

## consul

## mongo

helm install --name mongodb --set service.type=LoadBalancer --set mongodbRootPassword=mongoHaveFun stable/mongodb
