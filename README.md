# Use S2I to build a new docker image using sources and a builder image.
# cloned to rb

- oc delete namespace rb-ns-p2
- oc create namespace rb-ns-p2
- \# oc adm policy add-scc-to-user privileged -z default -n rb-ns-p2
- oc project  rb-ns-p2
-
- oc new-app https://github.com/findnix/rb-ocp-phy-1
- oc expose svc/deploy-python-openshift-s2i-tutorial
