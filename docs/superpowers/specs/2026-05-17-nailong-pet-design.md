# 奶龙桌宠 (nailong-pet) 设计文档

**日期**：2026-05-17  
**状态**：design locked, awaiting user review

## 1. 目标与背景

在 Windows 桌面上放一个像素奶龙桌宠，**单击切换** Claude Code Desktop 的 bypass 模式 ↔ accept 模式。

桌宠是 [`C:\Users\david\.claude\hooks\bypass.cmd`](../../../../.claude/hooks/bypass.cmd) 这个开关脚本的可视化前端，技术上完全复用现有的哨兵文件机制（`C:\Users\david\.claude\hooks\.bypass-on`）。Hook 脚本和 `settings.json` 一行都不改。

**为什么需要**：Claude Code Desktop 在 macOS 上有 bug，会忽略 `permissions.allow` 和 `defaultMode: bypassPermissions`（[Issue #29026](https://github.com/anthropics/claude-code/issues/29026)），用户已通过 PreToolUse hook 绕过。桌宠把"现在到底是裸奔还是审慎"这件事可视化，避免心智误判。

## 2. 角色与视觉设计

### 双态选型

| 状态 | 形象 | 隐喻 |
|---|---|---|
| `accept`（哨兵文件不存在） | **梵高星空奶龙** —— 蓝黄漩涡夜空、油画厚涂笔触、月亮星辰 | 看似宁静的思考，但漩涡藏着 Claude 在按部就班询问 permission |
| `bypass`（哨兵文件存在） | **构成主义奶龙** —— 红黑黄三色块、握传声筒呐喊、苏联式宣传海报、利西茨基风几何 | 革命就在此刻，Claude 在裸奔执行 |

视觉对比维度：油画 vs 几何海报 / 冷蓝黄 vs 火红黑黄 / 沉思 vs 行动。

### 风格参考（给 Codex）

- accept 参考：梵·高《星夜》(The Starry Night, 1889)
- bypass 参考：埃尔·利西茨基《红楔击败白军》(Lissitzky, 1919)、罗钦科宣传海报
- 主体始终是**奶龙**（圆胖、黄色、短四肢、大笑表情），不是真人不是恐龙

## 3. 尺寸与帧规格

- **画布尺寸**：128×128 像素，PNG（含 alpha 通道）
- **像素粒度**：可见像素颗粒感，但允许细节（不强制 1bit / Tamagotchi 风）
- **帧数清单**：

| 用途 | 文件 | 帧数 |
|---|---|---|
| accept 待机循环 | `assets/accept_idle_00.png` ~ `accept_idle_07.png` | 8 |
| bypass 待机循环 | `assets/bypass_idle_00.png` ~ `bypass_idle_07.png` | 8 |
| accept → bypass 过场 | `assets/trans_to_bypass_00.png` ~ `trans_to_bypass_05.png` | 6 |
| bypass → accept 过场 | `assets/trans_to_accept_00.png` ~ `trans_to_accept_05.png` | 6 |
| **总计** | | **28** |

### 动画时序

- **待机循环**：每帧 250 ms，单循环 2 s，无限循环
- **过场**：每帧 100 ms，单次播放 0.6 s
- **触发**：左键点击 → 切换哨兵文件 → 播放过场 → 切到对端待机循环

## 4. 桌面行为

| 行为 | 实现 |
|---|---|
| 启动位置 | 屏幕右下角，距屏幕右边 24px、距任务栏 12px |
| 总是置顶 | 是（`Qt.WindowStaysOnTopHint`） |
| 透明无边窗 | 是（`Qt.FramelessWindowHint` + `Qt.WA_TranslucentBackground`） |
| 任务栏图标 | 否（`Qt.Tool` flag） |
| 鼠标拖动 | 按住左键 > 6 px 阈值视为拖动；< 6 px 视为单击 |
| 位置记忆 | 退出时写 `%LOCALAPPDATA%\nailong-pet\state.json`，下次启动读 |
| 左键单击 | 切换 bypass / accept（触发过场） |
| 右键菜单 | 强制切到 accept / 强制切到 bypass / 重置位置 / 暂停动画 / 关于 / 退出 |
| 鼠标悬停 | Tooltip 显示当前模式（"BYPASS 模式 · 全自动放权" / "ACCEPT 模式 · 正常审批"） |
| 开机自启 | 否（用户自行拖到 `shell:startup`） |
| 系统托盘图标 | 否 |
| 全局快捷键 | 否 |

## 5. 状态同步

- **真相源**：`Path.home() / ".claude" / "hooks" / ".bypass-on"` 哨兵文件（不硬编码用户名）
- **写**：左键点击 / 右键菜单 → 创建或删除哨兵 → 触发文件 watcher → 播过场
- **读 + 监听**：用 `watchdog` 库（或 `QFileSystemWatcher`）监听该文件
  - 用户双击桌面 `Claude Bypass Toggle.lnk` 切换时，桌宠也会自动同步显示
  - 启动时先读一次，定向到对应待机循环

## 6. 技术架构

### 技术栈

- Python ≥ 3.10
- **PySide6** —— Qt for Python（透明窗口 + 动画播放）
- **watchdog** —— 文件监听
- Windows 10/11 ≥ 1903

### 模块切分

```
src/
├── __main__.py          # python -m nailong_pet 入口
├── app.py               # QApplication + 主窗口实例
├── pet_window.py        # 透明无边窗、拖动、置顶、托盘菜单
├── animator.py          # 帧序列加载 + 定时器播放 (待机循环 + 过场)
├── state.py             # 哨兵文件读写 + 文件 watcher
└── config.py            # 资源路径、坐标记忆、常量
```

### 数据流

```
左键点击  →  state.toggle()                 →  写哨兵文件
                                            ↓
watchdog 侦测到文件变化               →  animator.play_transition(direction)
                                            ↓
                                            过场 6 帧播完
                                            ↓
                                            animator.play_idle(new_state)
```

### 错误处理

- 哨兵文件读写失败 → 弹错误对话框，桌宠继续按当前状态显示
- 帧文件缺失 → 启动时 fail-fast，提示用户先让 Codex 出图
- watchdog 失败 → 降级为每秒轮询 `Path.exists()`

## 7. 仓库目录

```
nailong-pet/
├── README.md
├── pyproject.toml              # PySide6, watchdog
├── src/
│   ├── __main__.py
│   ├── app.py
│   ├── pet_window.py
│   ├── animator.py
│   ├── state.py
│   └── config.py
├── assets/                     # 28 张 PNG (Codex 出图后落盘)
│   ├── accept_idle_*.png
│   ├── bypass_idle_*.png
│   ├── trans_to_bypass_*.png
│   └── trans_to_accept_*.png
├── codex/
│   ├── brief.md                # 给 Codex 的总指令（角色一致性、风格参考、命名约定）
│   ├── prompts.md              # 28 张图逐帧 prompt 文本
│   └── style-reference/        # 风格参考图（梵高星空 / 利西茨基海报）
├── docs/
│   └── superpowers/specs/2026-05-17-nailong-pet-design.md  # 本文档
└── tests/
    └── test_state.py           # 哨兵文件读写 + watcher 触发
```

## 8. Codex 工作流

桌宠源码我（Claude）写，**图像资产**全部交给 Codex 调 image-2 出，因为：
1. 用户偏好"美工需求交给 Codex + image-2"（见 user 长期 feedback）
2. image-2 在二创/像素艺术上比我写代码画 SVG 强百倍

**工作流**：

1. 用户在 Codex 终端打开 `C:\Users\david\nailong-pet`
2. 跟 Codex 说：「按 `codex/brief.md` 和 `codex/prompts.md`，调 image-2 出全部 28 张图，落到 `assets/`，文件名严格按 prompts.md 的约定」
3. Codex 出图 → 落盘 → 用户运行 `python -m nailong_pet` 看效果
4. 不满意的图回 Codex 单独重做

`codex/brief.md` 必须含：
- 角色一致性参考（奶龙的圆胖/黄色/短四肢/大笑表情）
- 两种风格的核心视觉规则（星夜笔触感 / 构成主义几何）
- 文件命名硬规则（精确到下划线和 00-07 编号位）
- 帧间一致性要求（同一循环内角色姿态连贯）
- 透明背景要求（PNG with alpha，主体周围裁空）

## 9. 验收标准

| # | 项 | 检查 |
|---|---|---|
| 1 | 桌宠启动 | `python -m nailong_pet` 后右下角出现奶龙 |
| 2 | 状态正确 | 启动时若 `.bypass-on` 存在显示构成主义，反之星空 |
| 3 | 单击切换 | 左键单击 → 过场动画 → 切到对端待机 |
| 4 | 同步外部切换 | 双击桌面 `Claude Bypass Toggle.lnk` → 桌宠 1 秒内同步 |
| 5 | 拖动 | 按住 + 拖动 → 桌宠跟随；松开 + 退出 + 再启动 → 在原位置 |
| 6 | 右键菜单 | 6 个菜单项全部可用 |
| 7 | 悬停提示 | 鼠标停 1 秒后 Tooltip 显示当前模式 |
| 8 | 退出 | 右键菜单 / Alt+F4 / 任务管理器都能正常关 |

## 10. 风险与依赖

| 风险 | 缓解 |
|---|---|
| Codex 出图质量参差不齐 | brief.md 写硬规则；个别帧返工 |
| PySide6 透明窗口在某些 Windows 11 主题下出现黑色背景 | 测试时用 `Qt.WA_NoSystemBackground`，必要时改用 `tkinter` + `wm_attributes("-transparentcolor", ...)` 兜底 |
| 哨兵文件路径写死 `C:\Users\david\...` | 改用 `Path.home() / ".claude" / "hooks" / ".bypass-on"` |
| watchdog 在 Windows 上偶发延迟 | 兜底 1s 轮询 |
| 28 帧一次出完工作量大 | 分两批：先出 16 帧待机看效果，再出 12 帧过场 |

## 11. 显式不做的事（YAGNI）

- ❌ 多角色 / 多变体切换（只做星空 + 构成主义两个）
- ❌ 进度条 / HP / 喂食 / 桌宠互动玩法
- ❌ 配置面板 GUI
- ❌ 自动更新 / 远程获取新皮肤
- ❌ 多人 / 联网
- ❌ 表情包导出
- ❌ 桌宠移动到屏幕边缘自动隐藏
- ❌ Mac / Linux 支持（先 Windows-only）
