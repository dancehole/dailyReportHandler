# DailyReport 说明文档

## 概述

**DailyReport** 旨在快速且方便地处理每天的工作日报/日志，同时方便归档和分类总结。

## 快速上手

### 包名

`DailyReport` 是 `daily report handler` 的缩写。

### 无标志参数

- `init`：初始化目录，目录格式如下：
  - `init weekly`：按周归档（默认）
  - `init monthly`：按月归档
  - `init yearly`：按年归档

```
工作日报文档 / 一般在docs目录下
|-- archivingFile归档文件
|-- Common常用功能
    |-- daily.py
    |-- 模板文件（日报模板/周报模板等）
    |-- 日报模板.md
    |-- 周报模板.md
|-- dailyReport日报 ---后续目录可以调整(自动归档)
    |-- archivingFile(归档文件，暂时考虑按照日期排列)
    |-- 04-24-week1
        |-- common
        |-- 04-24.md
        |-- 04-25.md
        |-- week1周报.md
    |-- 05-06-week2
    |-- 05-13-week3
|-- docsOutput文档输出
```

## 安装说明

可以使用以下命令安装：

```bash
pip install daily_report_handler
```

## 使用方法

### 日志目录初始化

```bash
python -m daily_report_handler init

【假设测试目录为：D:/tmpfile/dailyReport】
python cmd.py # 创建今天的日报&目录&初始化
daily init # 创建今天的日报&目录&初始化

```

### 日报文件初始化

自适应调休/加班情况，自动识别并处理。

模板传参数：

- `week`：当前周数
- `day`：工作天数
- `type`：日/周（日报还是周报）
- `ip`：服务的IP
- `curr_date`：当前日期 mm-dd
- `work_list`：todo list，一般是今天工作重点内容概要
- `work_detail`：todo list的详细内容
- `todo`：记录今天没干完的事情
- `work_brief`：工作简要
- `work_class`：所在项目或者分类
- `work_link`：日报链接

## 功能说明

### 日志目录初始化

- 在 `dailyReport` 目录下初始化日志文件夹。
- 建立目录格式为 `mm-dd-weekx` 的目录。
- 按周归档日志，年份固定为 2024。
- 判断是新的一周或未来的第x周，提前建立目录。

### 日报文件初始化

- 根据调休/加班情况自动识别。
- 模板参数包括当前周数、工作天数、日报类型、服务IP、当前日期等。

## 贡献指南

如果你想为此项目做出贡献，请按照以下步骤：

- [python包开发流程](./static/develop.md)
- [代码贡献流程](./static/contribute.md)

1. Fork 此仓库。
2. 创建你的功能分支 (`git checkout -b feature/AmazingFeature`)。
3. 提交你的更改 (`git commit -m 'Add some AmazingFeature'`)。
4. 推送到分支 (`git push origin feature/AmazingFeature`)。
5. 打开一个 Pull Request。

## 许可证

此项目使用 MIT 许可证。详情请参阅 LICENSE 文件。

## 联系我们

如果你有任何问题或建议，请通过以下方式联系我们：

- 作者：Dancehole
- 邮箱：1391755954@qq.com
- GitHub：[https://github.com/dancehole](https://github.com/dancehole)

---

## 代码示例


## 主要代码逻辑


这段文档解释了如何使用 `DailyReportHandler` 来初始化日志目录、生成日报和周报，并更新配置文件。


## 问题反馈：
1. config记录周数不正常
2. 渲染模板周数不正常