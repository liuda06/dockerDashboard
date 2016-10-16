#！ /bin/bash
# usage ==> ./docker.sh 'ip:port' 'command'

DOCKER_HOST="tcp://$1"
echo DOCKET_HOST=$DOCKER_HOST
echo "将执行以下命令："$2
$2