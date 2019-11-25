# 部署前提，需要docker-compose.yml文件存在！
cmd=$(docker-compose ps | grep web)
if [[ ! ${cmd} ]]; then
  docker-compose up -d
  echo "服务部署成功！"
else
  docker-compose stop
  echo "服务已停止！"
  sleep 3
  echo "服务开始重新部署..."
  docker-compose up --build
  echo "服务部署成功！"
fi
