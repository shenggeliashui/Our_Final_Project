# 创建虚拟环境
python -m venv venv

# 临时更改执行策略
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# 在Windows上激活虚拟环境
venv\Scripts\activate

# 项目结构
WordAPP/
│
├── app/
│   ├── __init__.py
│   ├── common/
│   │       ├──  __init__.py
│   │       ├──  cors.py
│   │       ├──  result.py
│   │       └──  role_enum.py
│   ├── controllers/
│   │       ├──  __init__.py
│   │       ├──  file_controller.py
│   │       ├──  user_controller.py
│   │       ├──  web_controller.py
│   │       └──  uservocab_controller.py
│   ├── exceptions/
│   │       ├──  __init__.py
│   │       └──  custom_exceptions.py
│   ├── mappers/
│   │       ├──  __init__.py
│   │       ├──  admin_mapper.py
│   │       ├──  user_mapper.py
│   │       └──  uservocab_mapper.py
│   ├── models/
│   │       ├──  __init__.py
│   │       ├──  account.py
│   │       ├──  admin.py
│   │       ├──  user.py
│   │       └──  uservocab.py
│   ├── services/
│   │       ├──  __init__.py
│   │       ├──  admin_services.py
│   │       ├──  user_services.py
│   │       └──  uservocab_service.py
│   ├── static/
│   └── templates/
├── config.py
└── run.py