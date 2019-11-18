### flask+docker

(参考：https://zhuanlan.zhihu.com/p/78432719)

#### requirements.txt (pip freeze > requirements.txt)

主要用于docker build时获取项目依赖第三方包（pipenv install方式存在问题，暂时不用）

####  单flask应用部署:（docker login登录dockerhub）

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

---
#### 多服务flask应用部署（docker-compose）

docker-compose文件把所有的东西关联起来。它描述了应用的构成（一个 web 服务和一个数据库）、使用的 Docker 镜像、镜像之间的连接、挂载到容器的卷，以及服务开放的端口。

**目前compose 中定义了两个服务 web 和 redis。**

文件内容解释：

>web 服务
>
>build: 使用当前目录的 Dockerfile build 的镜像
>
>ports: 映射宿主机 5000 端口到容器的 5000 端口
>
>container_name: 指定了容器的名字
>
>redis 服务
>
>image: 使用 Docker Hub 中的 redis 镜像

##### 在运行 docker-compose up 之前，在本地项目里把redis连接配置修改

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

修改为：

r = redis.Redis(host='redis', port=6379, decode_responses=True)

##### 开始部署：

1、服务器项目根目录下，自动完成包括构建镜像，（重新）创建服务，启动服务，并关联服务相关容器的一系列操作（链接的服务都将会被自动启动，除非已经处于运行状态）

docker-compose up

2、列出当前运行的服务状态和相关信息

docker-compose ps