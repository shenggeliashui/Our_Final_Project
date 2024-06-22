# 创建虚拟环境
python -m venv venv

# 临时更改执行策略
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# 在Windows上激活虚拟环境
venv\Scripts\activate