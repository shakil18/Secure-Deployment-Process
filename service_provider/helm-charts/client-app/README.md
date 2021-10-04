# Generic chart

Deploy a generic SCONE application to a Kubernetes cluster.

### Prerequisites

* A Kubernetes cluster.
* At least one node with the Intel SGX driver installed and available.

### Install the chart

#### Add the repo

If you haven't yet, please add this repo to Helm.

To deploy a Hello World app with the default parameters to your Kubernetes cluster:

```bash
helm install client-app client-app
```

To deploy your own app, specify [custom parameters](#parameters), such as `image`, `command`, `scone.cas`, `scone.las` and `scone.configID`.

#### SGX device

By default, this helm chart uses the [SGX Plugin](../sgxdevplugin). Hence, it sets the resource limits of the application as follows:

```yaml
resources:
  limits:
    sgx.k8s.io/sgx: 1
```

In case you do not want to use the SGX plugin, you can remove the resource limit and explicitly mount the local SGX device into your container by setting:

```yaml
extraVolumes:
  - name: dev-isgx
    hostPath:
      path: /dev/isgx

extraVolumeMounts:
  - name: dev-isgx
    path: /dev/isgx
```

Please note that mounting the local SGX device into your container requires privileged mode, which will grant your container access to ALL host devices. To enable privileged mode, set `securityContext`:

```yaml
securityContext:
  privileged: true
```

### Parameters

|Parameter|Description|Default|
|---|---|---|
`replicaCount`|How many replicas|`1`
`image`|Application image|`sconecuratedimages/kubernetes:hello-k8s-scone0.1`
`imagePullPolicy`|Application pull policy|`IfNotPresent`
`command`|Application command array|`nil`
`imagePullSecrets`|Application pull secrets, in case of private repositories|`[]`
`useSGXDevPlugin`|Use [SGX Device Plugin](../sgxdevplugin) to access SGX resources.|`"enabled"`
`scone.las`|LAS address|`172.17.0.1:18766`
`scone.cas`|CAS address|`scone-cas.cf`
`scone.configID|Application session|`hello-k8s-scone/application`
`securityContext`|Security context for container|`{}`
`service.type`|Application service type|`ClusterIP`
`service.port`|Application service port|`80`
`service.containerPort`|Container port exposed by the Service|`8080`
`extraEnvVars`|Extra environment variables|`[]`
`resources`|CPU/Memory resource requests/limits for node.|`{}`
`tolerations`|List of node taints to tolerate (this value is evaluated as a template)|`[]`
`affinity`|Define node affinity for application|`{}`
