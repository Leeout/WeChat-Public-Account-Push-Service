flask+docker部署项目-参考资料：https://zhuanlan.zhihu.com/p/78432719

requirements.txt 主要用于docker build时获取项目依赖第三方包（pipenv install方式存在问题，暂时不用）

部署至服务器流程：（docker login登录docker）

1、本地写好Dockerfile(即获取、启动项目依赖，可理解为启动命令)

2、本地sudo docker build -t "想用的镜像名称" .

3、本地改下镜像名称 docker tag "镜像的CONTAINER ID" docker登录用户名/镜像名称:tag号

4、本地docker push docker登录用户名/镜像名称:tag号

5、服务器登录docker，进行docker pull docker登录用户名/镜像名称:tag号

6、docker images确认镜像拉下来了，然后sudo docker run -d -p 80:80 --name "你想取的进程名" docker登录用户名/镜像名称:tag号

7、docker ps 确认进程是否已经启动

8、外网访问：外网ip/"路由地址"

至此 接口项目部署完成！
