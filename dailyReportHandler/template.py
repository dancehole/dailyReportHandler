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
    <strong>简体中文</strong> | <a href="">English</a>
</p>
    <a href ="http://10.10.41.235:8000/"><img src="https://img.shields.io/badge/Blog-dancehole-orange?style=flat&logo=microdotblog&logoColor=white&labelColor=blue"></a>
    <a href ="https://gitee.com/dancehole"><img src="https://img.shields.io/badge/Gitee-dancehole-orange?style=flat&logo=gitee&logoColor=red&labelColor=white"></a>
    <a href ="https://github.com/dancehole"><img src="https://img.shields.io/badge/Github-dancehole-orange?style=flat&logo=github&logoColor=white&labelColor=grey"></a>
</div>
<div align="center">
    <a><img src="https://img.shields.io/badge/入职嘉为-第{{week}}周-yellow"></a>
    <a><img src="https://img.shields.io/badge/工作日报-第{{day}}天-blue"></a>
    <a><img src="https://img.shields.io/badge/{{curr_date_badage}}-工作{{type}}报-green">
</div>
<p align="center" style="border: 1px solid black; padding: 5px; margin: 10px 0;">
    <b>{{curr_date}}嘉为实习{{type}}报CanLab</b><br>邓仕昊sx_dancehole@Canway.net<br>欢迎访问日报源网址<a href="{{ip}}">{{ip}}</a>
    </p>
    """

    content = """
## 1. 今日工作概要

{{work_list}}

## 2. 工作内容记录

{{work_detail}}

## 3. 总结与思考

{{work_summary}}

    """
    
    content_weekly = """
## 1. 本周工作总结
{{weekly_summary}}
## 2. 问题总结与解决思路
{{weekly_content}}
## 3. 下周工作计划
{{weekly_plan}}
    """

    footer = """
## 附录

| 日期  | 工作主要内容 | 所在项目/分类 | 文章输出 |
| ----- | ---------- | --------- | -------- |
| 第{{week}}周 | 第{{day}}天   |      |          |
|  {{curr_date}}     |      {{work_brief}}   |    {{work_class}}|  {{work_link}}|

我的工作日报已经公开，支持每日日报的查看。**更详细的工作日报输出和文档流输出，请[访问这里]({{ip}})。**

"""

    weekly_footer = """
## 附录
## 工作日志摘要
|日期 | 工作主要内容 | 所在项目/分类 | 工作日报链接 |
|---|---|---|---|
{%for date,content,class,link in weekly_report_data%}
| {{date}} | {{content}} |{{class}} |{{link}} |
{%endfor%}
"""

    default_work_list = """
### 1.1 工作安排
1. (default)完成第一个工作
2. (default)完成第二个工作
3. (default)完成第三个工作

### 1.2 时间安排
1. 9:00-12:00---工作一
2. 14:00-16:00---工作二
3. 16:00-18:00---工作三

    """
    
    default_work_detail = """
> 遇到问题，解决问题并记录，方便积累与复用

### 2.1 工作一
**第一个方面遇到的问题**
**解决方案**
### 2.2 工作二
**第二个方面遇到的问题**
**解决方案**

    """
    
    
    default_work_summary = """
### 3.1 今日未完成工作【暨明日todo】
1. (default)第一个工作
2. (default)第二个工作
3. (default)第三个工作
    
### 3.2 今日总结
1. (default)总结1
2. (default)总结2
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
        str = Template.header+Template.content+Template.footer if fill_data["type"]=="日" else Template.header+Template.content_weekly+Template.weekly_footer
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
        "type": "日",
        "curr_date": now.strftime("%m-%d"),# 当前日期格式化
        "curr_date_badage": now.strftime("%m--%d"),
        "work_brief": 'default',
        "work_list": Template.default_work_list,
        "work_detail": Template.default_work_detail,
        "work_summary":Template.default_work_summary,
        "work_class": "default",
        "work_link": "http://10.10.41.235:8001/",   # 日报的链接地址，细化
        "ip": "http://10.10.41.235:8001/",  # 示例IP地址
    }
    test_weekly_data = {
        "week": 1,  # 示例：假设是下周
        "day":  1,    # 示例：假设是明天
        "type": "周",
        "curr_date": now.strftime("%m-%d"),# 当前日期格式化
        "curr_date_badage": now.strftime("%m--%d"),
        "work_list": Template.default_work_list,
        "work_detail": Template.default_work_detail,
        "work_summary":Template.default_work_summary,
        "ip": "http://10.10.41.235:8001/",  # 示例IP地址
        "weekly_plan":"default",
        "weekly_summary":"default",
        "weekly_content":"default",
        "weekly_report_data":[
            {
                "date":"2023-05-01",
                "content":"default",
                "class":"default",
                "link":"default"
            },
            {
                "date":"2023-05-02",
                "content":"default",
                "class":"default",
                "link":"default"
            }
        ]
    }

    # 使用临时文件进行测试，避免污染实际文件系统
    with NamedTemporaryFile(mode="w+", suffix=".md", delete=False) as temp_file:
        output_path = temp_file.name
        success = Template.render_template(test_data, output_path)
    if success:
        print(f"测试渲染日报成功，输出文件位于：{output_path}")
    else:
        print("测试渲染失败")
        
    # 使用临时文件进行测试，避免污染实际文件系统
    with NamedTemporaryFile(mode="w+", suffix=".md", delete=False) as temp_file:
        output_path = temp_file.name
        success = Template.render_template(test_weekly_data, output_path)
    if success:
        print(f"测试渲染周报成功，输出文件位于：{output_path}")
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
