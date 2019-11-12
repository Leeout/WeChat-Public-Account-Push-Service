#### 一、flask+docker部署项目-参考资料：https://zhuanlan.zhihu.com/p/78432719

#### 二、requirements.txt-主要用于docker build时获取项目依赖第三方包（pipenv install方式存在问题，暂时不用）

#### 三、部署至服务器流程:（docker login登录dockerhub）

1、本地写好Dockerfile(即获取、启动项目依赖，可理解为启动命令)

touch Dockerfile

2、本地构建镜像

sudo docker build -t "想用的镜像名称" .

3、本地镜像添加到个人dockerhub

 docker tag "镜像的CONTAINER ID" docker登录用户名/镜像名称:tag号

4、推送至远程dockerhub

docker push docker登录用户名/镜像名称:tag号

5、Linux服务器获取镜像

docker pull docker登录用户名/镜像名称:tag号

6、部署docker

sudo docker run -d -p 80:80 --name "你想取的进程名" docker登录用户名/镜像名称:tag号

7、 确认进程是否已经启动

docker ps

8、外网访问：外网ip/"路由地址"

至此，flask项目部署完成！
