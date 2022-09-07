# Use S2I to build a new docker image using sources and a builder image.
# cloned to rb

* oc delete namespace rb-ns-p1
* oc create namespace rb-ns-p1
* oc adm policy add-scc-to-user privileged -z default -n rb-ns-p1
* oc project  rb-ns-p1

* oc new-app https://github.com/IBM/deploy-python-openshift-s2i-tutorial
* oc expose svc/deploy-python-openshift-s2i-tutorial
