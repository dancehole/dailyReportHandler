from setuptools import setup, find_packages

# 0.1.0 更新：完成安装包流程
# 0.1.1 更新：测试命令行调用
# 0.1.2 更新：可以正确解析命令行参数+过整体流程

setup(
    name='dailyReportHandler',  # 包名
    version='0.1.2',    # 版本号
    packages=find_packages(),  # 自动发现所有包
    install_requires=['requests'],  # 依赖列表
    author='Dancehole',  # 作者名
    author_email='1391755954@qq.com',  # 作者邮箱
    description='A file manager to generate daily report',  # 包描述
    long_description=open('readme.md').read(),  # 详细描述，可读取README文件
    long_description_content_type='text/markdown',  # README文件类型，如果是Markdown
    url='https://github.com/dancehole/dailyReportHandler',  # 项目URL
    classifiers=[  # 分类信息
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    # 程序入口点[命令行]
    entry_points={
        'console_scripts': [
            'daily=dailyReportHandler.cmd:main',
        ]
    }
)
