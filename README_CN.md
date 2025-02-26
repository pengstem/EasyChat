# 🚀 EasyChat

EasyChat 是一个基于 Python 的应用程序，可通过文本和语音界面与 Google 的 Gemini AI 模型进行交互。

## ✨ 功能特点

- 💬 与 Gemini AI 模型进行基于文本的交流
- 🎤 语音交流功能，适合英语口语练习
- 🤖 多种 Gemini 模型选择（gemini-2.0-flash、gemini-2.0-pro-exp、gemini-2.0-flash-thinking）
- 🌐 英语口语练习并获得发音反馈
- 📝 可自定义系统指令

## 📋 系统要求

- Python 3.10+
- Google API 密钥（可从 <https://aistudio.google.com/apikey> 获取）
- 互联网连接

## 🛠️ 安装方法

```bash
# 克隆代码库
git clone https://github.com/yourusername/EasyChat.git

# 进入项目目录
cd EasyChat

# 安装所需包
pip install google-generativeai websockets websockets-proxy rich elevenlabs pyaudio
```

## 🚀 使用方法

运行主脚本：

```bash
python gemini.py
```

### 文本交流模式

1. 在提示时输入您的 Google API 密钥
2. 选择选项 "2" 进行文本交流
3. 选择您偏好的 Gemini 模型
4. 可选择提供系统指令
5. 开始与 AI 交谈

### 语音交流模式

1. 在提示时输入您的 Google API 密钥
2. 选择选项 "1" 进行语音交流
3. 使用麦克风练习英语口语
4. 接收发音反馈和纠正

## 📱 模型选项

- **gemini-2.0-flash**：快速高效的模型，适合日常对话
- **gemini-2.0-pro-exp**：高级模型，具有扩展功能，适合复杂任务
- **gemini-2.0-flash-thinking**：专门具有"思考过程"功能的模型

## ❓ 常见问题解决

- **API 密钥问题**：确保您的 Google API 密钥有效并有权访问 Gemini 模型
- **音频问题**：检查麦克风设置和权限
- **连接问题**：验证您的互联网连接和代理设置（如果适用）
- **包错误**：确保所有依赖项都已正确安装并版本适当

## 🤝 贡献指南

欢迎贡献！如果您想改进 EasyChat：

1. Fork 代码库
2. 创建功能分支：`git checkout -b new-feature`
3. 提交您的更改：`git commit -am '添加新功能'`
4. 推送到分支：`git push origin new-feature`
5. 提交拉取请求

## 🎯 项目目的

EasyChat 专为那些希望使用免费 AI 模型的用户设计：

- 英语语言练习并获得发音反馈
- 通过文本对话获取 AI 通用协助
- 测试 Google Gemini 模型的不同能力

## 📝 许可证

本项目采用 MIT 许可证 - 详情请参阅 [LICENSE](LICENSE) 文件。
