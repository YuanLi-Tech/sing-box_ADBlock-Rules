# sing-box_ADBlock-Rules

sing-box 广告拦截规则集（二进制 .srs），每日自动同步上游。

## 内容

| 文件 | 来源 | 更新机制 |
|---|---|---|
| `1hosts-lite.srs` | [badmojr/1Hosts](https://github.com/badmojr/1Hosts) **Lite** 档（保守，零假阳性定位）| GitHub Actions 每天 04:00 UTC 轮询上游，内容变化时自动编译并推送 |

## 在 sing-box 中使用

```jsonc
{
  "type": "remote",
  "tag": "1hosts-lite",
  "format": "binary",
  "url": "https://raw.githubusercontent.com/YuanLi-Tech/sing-box_ADBlock-Rules/main/1hosts-lite.srs",
  "update_interval": "24h"
}
```

DNS 规则 / 路由规则引用 `"rule_set": "1hosts-lite"` 即可。

## 更新流程

1. 每天 04:00 UTC 拉取上游 `Lite/domains.txt`
2. 转换为 sing-box rule-set JSON（`convert.py`）
3. 用 sing-box v1.14.0 编译为 .srs
4. 与仓库现有文件对比，内容变化才提交推送（无变化跳过）

上游更新后，本仓库次日同步；sing-box 客户端侧配置 `update_interval` 自行拉取新版。
