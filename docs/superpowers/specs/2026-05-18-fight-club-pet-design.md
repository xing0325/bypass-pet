# bypass-pet 设计文档 (Fight Club pivot)

**日期**：2026-05-18  
**前身**：奶龙桌宠（同仓库，2026-05-17 立项），后改向 Fight Club  
**状态**：design locked, awaiting Codex assets

## 1. 目标与背景

在 Windows 桌面上放一个像素桌宠，**单击切换** Claude Code Desktop 的 bypass 模式 ↔ accept 模式。

桌宠是 [`C:\Users\david\.claude\hooks\bypass.cmd`](../../../../.claude/hooks/bypass.cmd) 这个开关脚本的可视化前端，技术上完全复用现有的哨兵文件机制（`~/.claude/hooks/.bypass-on`）。Hook 脚本和 `settings.json` 一行都不改。

**为什么需要**：Claude Code Desktop 在 macOS 上有 bug，会忽略 `permissions.allow` 和 `defaultMode: bypassPermissions`（[Issue #29026](https://github.com/anthropics/claude-code/issues/29026)），用户已通过 PreToolUse hook 绕过。桌宠把"现在到底是裸奔还是审慎"可视化，避免心智误判。

## 2. 角色与视觉设计

### 双态选型（pivot 后定稿）

| 状态 | 形象 | 隐喻 |
|---|---|---|
| `accept`（哨兵文件不存在） | **the Narrator / "Jack"** —— 失眠职员，皱白衬衫、松领带、黑眼圈、瘫肩 | 守规矩、问 permission、累垮的成年人 |
| `bypass`（哨兵文件存在） | **Tyler Durden** —— 红皮夹克、漂白头发、嘴角斜笑、叼烟 | 无政府主义人格脱缰、想干啥干啥 |

视觉对比维度：冷调灰绿办公室光 vs 暖调钨丝灯红黑；瘫陷 vs 直挺；衬衫西裤 vs 红皮夹克；困倦呵欠 vs 抽烟坏笑。

两角色是**同一个人**（Fight Club 的设定），视觉上完全相反，对应桌宠隐喻：同一个"我"两种状态。

### 风格参考（给 Codex）

- accept 参考：Edward Norton 在 Fight Club (1999) 的 Narrator 造型，**像越准越好**
- bypass 参考：Brad Pitt 在 Fight Club (1999) 的 Tyler Durden 造型，**像越准越好**
- 像素风：modern pixel illustration（参考 Octopath Traveler / Hyper Light Drifter 的胸像）at 256×320，不是 photoreal 也不是 8-bit chunky

### 演员肖像策略：要像

- 个人桌面用，无 IP 商用问题
- 描述特征 + 直接点名演员名字（"like Edward Norton"、"like Brad Pitt"）一起写进 prompt
- 像素抽象本身就提供了"二创"的法律灰度，不需要额外 hedge

## 3. 尺寸与帧规格

- **画布尺寸**：**256×320 像素（竖向）**，PNG（含 alpha 通道）。竖向是为了塞下镜子 + 底部水池 + 顶部烟雾外溢空间。
- **像素粒度**：现代像素插画风（Octopath / Hyper Light Drifter 胸像档），不是 8-bit chunky 也不是 photoreal
- **场景**：固定一个浴室镜子视角。镜子在画布中央偏上、薄金属边框、右上角一道发丝裂痕（伏笔暗示 Tyler 之前砸过）。镜下是水池边沿、水龙头、牙刷、香皂等小道具。所有 28 帧摄影机不动，只换"镜中是谁 + 灯光色温"。
- **4th wall 设备**：Tyler 的手可以伸出镜面、越出 canvas **右边缘**；烟雾可以飘出 canvas **顶边**。Jack 不破墙。
- **帧数清单**：

| 用途 | 文件 | 帧数 |
|---|---|---|
| accept 待机循环（Jack 在水池上方洗脸） | `assets/accept_idle_00.png` ~ `accept_idle_07.png` | 8 |
| bypass 待机循环（Tyler 在镜中抽烟 + 一帧手伸出镜面） | `assets/bypass_idle_00.png` ~ `bypass_idle_07.png` | 8 |
| accept → bypass 过场（镜中倒影变成 Tyler，Jack 惊愕） | `assets/trans_to_bypass_00.png` ~ `trans_to_bypass_05.png` | 6 |
| bypass → accept 过场（Tyler 消散，Jack 倒影归来） | `assets/trans_to_accept_00.png` ~ `trans_to_accept_05.png` | 6 |
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
| 位置记忆 | 退出时写 `%LOCALAPPDATA%\bypass-pet\state.json`，下次启动读 |
| 左键单击 | 切换 bypass / accept（触发过场） |
| 右键菜单 | 强制切到 accept / 强制切到 bypass / 重置位置 / 暂停动画 / 关于 / 退出 |
| 鼠标悬停 | Tooltip 显示当前模式（"BYPASS 模式 · Tyler · 全自动放权" / "ACCEPT 模式 · Jack · 正常审批"） |
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
- **PySide6** —— Qt for Python（透明窗口 + 动画播放 + 文件监听）
- Windows 10/11 ≥ 1903

### 模块切分

```
src/bypass_pet/
├── __init__.py
├── __main__.py          # python -m bypass_pet 入口
├── app.py               # QApplication + 主窗口实例 + QFileSystemWatcher
├── pet_window.py        # 透明无边窗、拖动、置顶、右键菜单
├── animator.py          # FrameSet + Animator（待机循环 + 过场）
├── state.py             # SentinelState 读写
└── config.py            # 资源路径、坐标记忆、常量
```

> **文件监听**：用 Qt 自带的 `QFileSystemWatcher` 监听哨兵所在目录，所有信号都在主线程，避免跨线程同步成本。`watchdog` 在 spec 早期版本里提过，最终未采用。

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
bypass-pet/
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
│   ├── accept_idle_*.png       # Jack
│   ├── bypass_idle_*.png       # Tyler
│   ├── trans_to_bypass_*.png   # Jack -> Tyler
│   └── trans_to_accept_*.png   # Tyler -> Jack
├── codex/
│   ├── brief.md                # 给 Codex 的总指令
│   ├── prompts.md              # 28 张图逐帧 prompt 文本
│   └── style-reference/        # 风格参考图（可选）
├── docs/
│   └── superpowers/specs/2026-05-18-fight-club-pet-design.md  # 本文档
└── tests/
    └── test_state.py
```

## 8. Codex 工作流

桌宠源码由 Claude 写，**图像资产**全部交给 Codex 调 image-2 出。

**工作流**：

1. 用户在 Codex 终端打开仓库（或把 repo URL 发给 Codex）
2. Codex 按 `codex/brief.md` + `codex/prompts.md` 生成全部 28 张图
3. 落到 `assets/`，按命名约定
4. 用户运行 `python -m bypass_pet` 看效果
5. 不满意的图回 Codex 单独重做

`codex/brief.md` 必须含：
- 角色一致性参考（Jack 的失眠白领 vs Tyler 的红夹克漂白发）
- 两种风格的核心视觉规则（冷调办公室光 vs 暖调红黑钨丝灯）
- 文件命名硬规则（精确到下划线和 00-07 编号位）
- 帧间一致性要求
- 透明背景要求
- 内容护栏（不真人脸 / 不血腥 / 不暴露）

## 9. 验收标准

| # | 项 | 检查 |
|---|---|---|
| 1 | 桌宠启动 | `python -m bypass_pet` 后右下角出现宠物 |
| 2 | 状态正确 | 启动时若 `.bypass-on` 存在显示 Tyler，反之 Jack |
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
| Image-2 拒绝真人化的演员脸 | brief 明确"render TRAITS not actor faces"；像素风天然抽象 |
| PySide6 透明窗口在某些 Windows 11 主题下出现黑色背景 | 测试时用 `Qt.WA_NoSystemBackground`，必要时改用 `tkinter` + `wm_attributes` 兜底 |
| 哨兵文件 watcher 与点击 toggle 同时触发，过场播两次 | 进入 begin_transition 前比对 (当前/目标) 状态，重复请求 no-op |
| 28 帧一次出完工作量大 | 分两批：先 16 待机帧看效果，再 12 过场帧 |
| 同人 / 改编 IP 风险 | 个人桌面工具、非商用、不公开传播改图；像素抽象后非演员脸 |

## 11. 显式不做的事（YAGNI）

- 多角色 / 多变体切换（只做 Jack + Tyler 两个）
- 进度条 / HP / 喂食 / 桌宠互动玩法
- 配置面板 GUI
- 自动更新 / 远程获取新皮肤
- 多人 / 联网
- 表情包导出
- 桌宠移动到屏幕边缘自动隐藏
- Mac / Linux 支持（先 Windows-only）
- 血腥 / 露点（内容护栏；但**演员肖像可以追求像，不 hedge**）

## 12. 未来扩展（不在本期 spec 范围）

- **皮肤切换**：B 方案"同一扇窗内外两态"作为可选 skin。实现路径：把 `assets/` 重构成 `assets/skin-mirror/` + `assets/skin-window/`，加配置项 / 右键菜单切换。本期不做。
- 其它候选 skin 思路（编号沿用之前对话）：A 互助小组 + Tyler 窗外抽烟（异步双场景）、D 同一办公桌两态。
