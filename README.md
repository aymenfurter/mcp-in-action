# 🤖 MCP in Action

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Azure](https://img.shields.io/badge/azure-AI%20Foundry-0078D4.svg)](https://azure.microsoft.com/products/ai-foundry)
[![MCP](https://img.shields.io/badge/MCP-protocol-green.svg)](https://spec.modelcontextprotocol.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> Build AI agents with the Model Context Protocol (MCP) — an open standard for connecting language models to external tools.

## 🚀 Quick Start

**Prerequisites:** Azure subscription with AI Foundry project • Python 3.10+ • Docker • Azure CLI

```bash
# Install dependencies
pip install -r requirements.txt

# Configure credentials
cp .env.example .env  # Edit with your endpoints
```

**Required `.env` variables:**
```bash
#PROJECT_ENDPOINT=https://your-aifoundry-resource.services.ai.azure.com/api/projects/your-project
ENDPOINT=https://your-aifoundry-resource.openai.azure.com/
API_KEY=your-api-key-here
PROJECT_ENDPOINT=https://your-project-foundry.services.ai.azure.com/api/projects/your-project
MODEL_DEPLOYMENT_NAME=your-model-deployment
MODEL_SHIELDS=your-model-with-shields
MODEL_NO_SHIELDS=your-model-without-shields
AZURE_PLAYWRIGHT_CONNECTION_ID=/subscriptions/your-subscription-id/resourceGroups/your-resource-group/providers/Microsoft.CognitiveServices/accounts/your-account/projects/your-project/connections/browser
AZURE_CLIENT_ID=your-client-id
```

## 📖 Notebooks

### [1️⃣ Tools Evolution](./1-tools.ipynb)
From string parsing to decoupled servers.

- **ReAct Pattern** - Prompt engineering with "Thought → Action → Observation"
- **Native Functions** - Structured function calls built into LLMs
- **Local Functions** - Imported tools (tight coupling)
- **MCP Protocol** - Remote tool servers (decoupled architecture)

**Key insight:** MCP separates tool lifecycle from agent logic for independent updates and reuse.

---

### [2️⃣ Custom MCP Servers](./2-custom-mcps.ipynb)
Build a Quality Management System with FastMCP.

- **FastMCP Framework** - Python decorator pattern for defining tools
- **Three Connection Types** - stdio (`MCPStdioTool`), HTTP/SSE (`MCPStreamableHTTPTool`), WebSocket (`MCPWebsocketTool`)
- **Azure Dev Tunnels** - Public endpoint for local development
- **Natural Language Interface** - Operators log defects via chat

**Example:** Factory workers describe defects in plain language instead of filling forms.

---

### [3️⃣ Beyond MCP](./3-browser-automation.ipynb)
Built-in Azure AI Foundry tools.

- 🌐 **Browser Automation** - Navigate websites with Playwright
- 📊 **Code Interpreter** - Execute Python in sandbox, generate matplotlib charts
- 📄 **File Search (RAG)** - Vector search over PDFs with citations

**When to use:** Azure tools for public data vs. custom MCP for internal systems.

---

### [4️⃣ Production Deployment](./4-secure-mcp.ipynb)
Secure MCP server with OAuth2 and network isolation.

```
User → Agent → APIM (OAuth2) → Container Apps (IP restricted) → MCP Server
```

**Security layers:**
- 🔐 **Microsoft Entra ID** - Token-based auth (no API keys)
- 🛡️ **Network Isolation** - IP allowlist restricts access to APIM

---

### [5️⃣ Prompt Shields](./5-prompt-shields.ipynb)
⚠️ **Educational only** - Demonstrates injection attacks and defenses.

| Test | Defense Layers | Result |
|------|----------------|--------|
| No shields | Model only | ❌ Vulnerable to injection |
| With shields | Model + Content Safety + Metaprompt | ✅ Attack detected |
| + Human approval | + Application logic (user confirmation) | ✅ Defense-in-depth |

**Critical:** Never pass PII or credentials to untrusted MCP servers. Use separate agents for public vs. private contexts.

---

## 🛡️ Responsible AI & Safety

### Defense-in-Depth Strategy

![Mitigation Layers](https://learn.microsoft.com/en-us/azure/ai-foundry/responsible-ai/openai/media/mitigation-layers.png)

1. **Model** - Responsible AI-aligned (GPT-4 with RLHF)
2. **Safety System** - Azure AI Content Safety (prompt shields, content filtering)
3. **Application** - Metaprompting + human approval workflows
4. **Positioning** - User education about capabilities/limitations

### Prompt Shields

Detect injection attacks by analyzing:
- **User prompts** - Attempts to change system rules, role-play personas, encoding tricks
- **Documents** - Malicious instructions hidden in PDFs, images, or grounding data

Categories: Manipulated content • Unauthorized access • Information gathering • Availability disruption • Fraud • Malware

### Content Filtering

Classifies inputs/outputs into categories: **Hate** • **Sexual** • **Violence** • **Self-harm**

Severity levels: `Safe` → `Low` → `Medium` → `High`

Supports: English, German, Japanese, Spanish, French, Italian, Portuguese, Chinese

---

## 📁 Project Structure

```
mcp-in-action/
├── 📓 1-tools.ipynb              # ReAct → Native → MCP evolution
├── 📓 2-custom-mcps.ipynb        # Build FastMCP servers
├── 📓 3-browser-automation.ipynb # Browser, code, RAG tools
├── 📓 4-secure-mcp.ipynb         # OAuth2 + APIM + Logic Apps
├── 📓 5-prompt-shields.ipynb     # Injection attacks & defenses
├── 📂 lib/
│   └── search_functions.py       # Helper functions (notebook 1)
├── 📝 system_prompt.prompt.yml   # ReAct prompt template
├── 📋 requirements.txt           # Python dependencies
└── 📖 README.md                  # This file
```

## 🔗 Resources

**MCP & Agent Framework**
- [Model Context Protocol on Microsoft Learn](https://learn.microsoft.com/agent-framework/user-guide/model-context-protocol/) - Overview & third-party considerations
- [Using MCP Tools with Agents](https://learn.microsoft.com/agent-framework/user-guide/model-context-protocol/using-mcp-tools) - Step-by-step guide
- [Using MCP with Foundry Agents](https://learn.microsoft.com/agent-framework/user-guide/model-context-protocol/using-mcp-with-foundry-agents) - Hosted tools & approvals

**Azure AI Foundry**
- [Tools in Agent Service](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/overview) - Built-in tools, invocation patterns
- [Microsoft Learn MCP Server](https://learn.microsoft.com/training/support/mcp) - Public documentation API
- [Logic Apps as MCP Servers](https://learn.microsoft.com/azure/logic-apps/set-up-model-context-protocol-server-standard) - Workflows, auth, monitoring

**Safety & Security**
- [Prompt Shields](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/content-filter-prompt-shields) - Injection detection
- [Content Filtering](https://learn.microsoft.com/azure/ai-foundry/concepts/content-filtering) - Categories & severity levels
- [Microsoft 365 Copilot Security](https://learn.microsoft.com/copilot/microsoft-365/microsoft-365-copilot-ai-security) - Defense-in-depth practices

**Community**
- [MCP Specification](https://spec.modelcontextprotocol.io/) - Official protocol docs
- [FastMCP GitHub](https://github.com/jlowin/fastmcp) - Python framework

---

## 📝 License

MIT License - Educational purposes only. Review [Microsoft API Terms of Use](https://www.microsoft.com/legal/terms-of-use) and [Responsible AI Guidelines](https://learn.microsoft.com/azure/ai-foundry/responsible-ai/) before production deployment.

---

## 🎓 Next Steps

1. **Understand** → Run `1-tools.ipynb` to see function calling evolution
2. **Build** → Create custom server in `2-custom-mcps.ipynb`
3. **Explore** → Try built-in tools in `3-browser-automation.ipynb`
4. **Deploy** → Secure production setup in `4-secure-mcp.ipynb`
5. **Defend** → Learn safety systems in `5-prompt-shields.ipynb`

---
