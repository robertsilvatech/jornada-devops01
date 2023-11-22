# Criando um Cluster Kubernetes Local com Kind

- [Criando um Cluster Kubernetes Local com Kind](#criando-um-cluster-kubernetes-local-com-kind)
  - [Instalando o Kind](#instalando-o-kind)
    - [Instalando no Linux no Linux](#instalando-no-linux-no-linux)
    - [Removendo kind no Linux](#removendo-kind-no-linux)
  - [Configuração de um cluster básico](#configuração-de-um-cluster-básico)
    - [Criar o cluster](#criar-o-cluster)
    - [Verificando detalhes do cluster](#verificando-detalhes-do-cluster)
    - [Criando um pod para validação](#criando-um-pod-para-validação)

## Instalando o Kind

Link: https://kind.sigs.k8s.io/docs/user/quick-start/#installation

### Instalando no Linux no Linux

```bash
cd /tmp
# For AMD64 / x86_64
[ $(uname -m) = x86_64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.20.0/kind-linux-amd64
# For ARM64
[ $(uname -m) = aarch64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.20.0/kind-linux-arm64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind
# Verificando a versão do Kind
kind version
```

### Removendo kind no Linux

```bash
rm /usr/local/bin/kind
```

## Configuração de um cluster básico

Link: https://kind.sigs.k8s.io/docs/user/quick-start/#creating-a-cluster

- Existem algumas maneiras de criar o cluster como descrito na documentação;
- Eu particulamente gosto de usar o arquivo de configuração;
- O arquivo de configuração tem a extensão **.yaml**;
- Exemplo:
       
`kind-config.yaml`

```yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
- role: worker
- role: worker
```
    
### Criar o cluster
    
```bash
kind create cluster --name jornadadevops --config kind-config.yaml
```
    
### Verificando detalhes do cluster
   
```bash
kubectl cluster-info --context kind-dzp
```   

### Criando um pod para validação
    
```bash
kubectl run pod-kind --image nginx
# listando pods
kubectl get pods
```