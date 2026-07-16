# xiaohang_helper

基于 Streamlit 的校园信息查询练手小程序。

## 项目结构

```text
xiaohang_helper/
├── src/
│   └── __init__.py
├── app.py
├── prompts.py
├── api.py
├── config.py
├── data/
│   ├── 01_新生入学.md
│   ├── 02_办事流程.md
│   ├── 03_电话黄页.md
│   └── 04_应急防骗.md
├── tests/
│   └── __init__.py
├── docs/
├── .gitignore
├── requirements.txt
└── README.md
```

## 安装依赖

```bash
pip install -r requirements.txt
```

## 运行方式

```bash
streamlit run app.py
```

## 环境变量

如需测试智能问答，请先设置：

- `SILICONFLOW_API_KEY`

如果没有配置 API Key，也可以先测试这些最小功能：
- 页面是否正常打开
- 身份切换是否正常
- 推荐问题按钮是否能自动填入输入框
- 电话黄页是否能正常展示
