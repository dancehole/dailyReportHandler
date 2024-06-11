# 亮点：对周的处理
from datetime import datetime
import os
from tempfile import NamedTemporaryFile
from jinja2 import Environment, FileSystemLoader


class Template:
    config_json = {
        "global": {
            "create_at": "",
            "last_modify": "",
            "work_day": -1,
            "work_week": -1,
        },
        "detail": [
            {
                "name": "week1",
                "desc": "测试",
                "date": ["04-24"],
                "detail": [
                    {
                        "date": "04-24",
                        "work_day": 1,
                        "work_week": 1,
                        "work_brief": "标题/工作概要，一句话",
                        "work_list": "工作内容列表，可以是一段话,可以是昨天没干完的事情todo",
                        "work_todo": "今天没干完的事情",
                        "work_content": "工作内容",
                        "work_link": "日报链接,支持自定义",
                    }
                ]
            }
        ],
    }
    header = """
<h1 align="center"> CanWay工作日志 </h1>

<div align="center">
        <img src="https://static.cwoa.net/d7c920db68254e858dc40e9064a8d4b2.png" style="width:250px;" /><br>
    <p align="center">
    <strong>简体中文</strong> | <a href="readme_en.md">English</a>
</p>
    <a href ="http://10.10.41.235:8000/"><img src="https://img.shields.io/badge/Blog-dancehole-orange?style=flat&logo=microdotblog&logoColor=white&labelColor=blue"></a>
    <a href ="https://gitee.com/dancehole"><img src="https://img.shields.io/badge/Gitee-dancehole-orange?style=flat&logo=gitee&logoColor=red&labelColor=white"></a>
    <a href ="https://github.com/dancehole"><img src="https://img.shields.io/badge/Github-dancehole-orange?style=flat&logo=github&logoColor=white&labelColor=grey"></a>
</div>
<div align="center">
    <a><img src="https://img.shields.io/badge/入职嘉为-第{{week}}周-yellow"></a>
    <a><img src="https://img.shields.io/badge/工作日报-第{{day}}天-blue"></a>
    <a><img src="https://img.shields.io/badge/{{curr_date}}--工作{{type}}报-green">
</div>

<p align="center" style="border: 1px solid black; padding: 5px; margin: 10px 0;">
    <b>嘉为实习{{type}}报CanLab-{{date}}</b><br>邓仕昊@Canway<br><a href="{{ip}}">{{ip}}</a>
    </p>
    """
    content = """
## 今日工作概要
> 来自昨日todo
{{work_list}}
## 工作内容记录
> 类似于工作日志
{{work_detail}}
## 明日计划todo
> 给明天/未来做todo，没完成的自动继承，完成了自动删除
{{todo}}
## 结语

我的工作日报已经公开，支持每日日报的查看。**更详细的工作日报输出和文档流输出，请[访问这里]({{ip}})。**

- 出于安全性考虑，网站只在**内网的工作时间**部署，暂不支持导出
    """
    
    footer = """
    
## 附录

## ※工作日志摘要

> 方便填写erp

| 日期  | 工作主要内容 | 所在项目/分类 | 文章输出 |
| ----- | ------------ | ------------- | -------- |
| 第{{week}}周 | 第{{day}}天        |               |          |
|  {{curr_date}}     |      {{work_brief}}        |    {{work_class}}           |    {{work_link}}      |
"""

    """渲染模板
    @prop:fill_data:填充数据
    @prop:output_path:文件路径 接收一个或者两个参数
    返回值:true 成功/失败
    
    注意：默认模板文件在Common目录下(base_directory)
    """
    @staticmethod
    def render_template(fill_data, *args):
        output_path = args[0] if len(args) == 1 else os.path.join(args[0],args[1])
        # 加载模板文件
        str = Template.header+Template.content+Template.footer
        env = Environment()
        try:
            # 渲染模板
            rendered_markdown = env.from_string(str).render(fill_data)
            # 输出渲染后的Markdown
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(rendered_markdown)
            return True
        except Exception as e:
            # logging.error(e)
            return False

    
"""增加一个测试接口"""
def test_render_template():
    # 使用当前时间作为模拟数据的一部分，以确保每次测试都有不同的日期信息
    now = datetime.now()
    test_data = {
        "week": 1,  # 示例：假设是下周
        "day":  1,    # 示例：假设是明天
        "curr_date": now.strftime("%m-%d"),                  # 当前日期格式化
        "work_brief": "测试工作概要",
        "work_list": "测试工作列表内容",
        "work_detail": "测试工作内容细节",
        "todo": "测试明日待办事项",
        "work_class": "测试项目分类",
        "work_link": "http://example.com/test-report",
        "ip": "127.0.0.1",  # 示例IP地址
    }

    # 使用临时文件进行测试，避免污染实际文件系统
    with NamedTemporaryFile(mode="w+", suffix=".md", delete=False) as temp_file:
        output_path = temp_file.name
        success = Template.render_template(test_data, output_path)
    
    if success:
        print(f"测试渲染成功，输出文件位于：{output_path}")
    else:
        print("测试渲染失败")
        
    # 可选：返回或打印渲染状态，以及可能的错误信息
    return success
        
        
def main():
    # 测试接口
    test_render_template()
    
# 如果脚本直接运行，执行main函数
if __name__ == "__main__":
    main()
