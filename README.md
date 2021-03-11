## 1. pip安装依赖(Virtualenv python环境 3.7.10)
pip install -r requirements/requirements.txt

## 2. for pyqt5
pyrcc5 -o libs/resources.py resources.qrc

## 3.运行
python labelImg.py

## 4. win打包
pyinstaller labelImg.spec -y

## 注意事项
- 项目代码放在英文路径下

## 依赖更新后用
pip freeze > requirements/requirements.txt