# sing-box_ADBlock-Rules

sing-box 广告拦截规则集（二进制 .srs），每日自动同步上游。

## 内容

| 文件 | 来源 | 说明 | 更新机制 |
|---|---|---|---|
| `1hosts-lite.srs` | [badmojr/1Hosts](https://github.com/badmojr/1Hosts) **Lite** 档（保守，零假阳性定位）| 国外 app 广告 + 追踪 | 每日 04:00 UTC 轮询上游，**内容变化时**自动编译并推送 |
| `anti-ad.srs` | [anti-ad.net](https://anti-ad.net/) 官方编译产物 | 中文广告域名（国内 SDK）| 每日镜像官方文件（存档副本，防源失效）|
| `geosite-category-ads-all.srs` | [SagerNet/sing-geosite](https://github.com/SagerNet/sing-geosite) 官方编译产物 | 广告分类域名（geosite 生态）| 每日镜像官方文件（存档副本，防源失效）|

> 三个文件**独立维护、不合并**。anti-ad 与 geosite 是官方产物的只读存档；`1hosts-lite.srs` 是本仓库的主动转换产物（上游只提供纯域名文本）。

## 在 sing-box 中使用

官方推荐：anti-ad 与 geosite-category-ads-all 直接引用**官方源**（保持最新且由官方维护）：

```jsonc
// anti-ad（官方）
{ "type": "remote", "tag": "anti-ad", "format": "binary",
  "url": "https://anti-ad.net/anti-ad-sing-box.srs", "update_interval": "24h" }

// geosite-category-ads-all（官方）
{ "type": "remote", "tag": "geosite-category-ads-all", "format": "binary",
  "url": "https://raw.githubusercontent.com/SagerNet/sing-geosite/rule-set/geosite-category-ads-all.srs", "update_interval": "24h" }

// 1hosts-lite（本仓库）
{ "type": "remote", "tag": "1hosts-lite", "format": "binary",
  "url": "https://raw.githubusercontent.com/YuanLi-Tech/sing-box_ADBlock-Rules/main/1hosts-lite.srs", "update_interval": "24h" }
```

如官方源不可用，可把 anti-ad / geosite 的 URL 切换为本仓库对应文件（内容一致，本仓库每日镜像）。

DNS / 路由规则引用 `"rule_set": "1hosts-lite"`（或 anti-ad / geosite-category-ads-all）即可。

## 更新流程

1. 每天 04:00 UTC 拉取三个上游源
2. `1hosts-lite`：转换为 sing-box rule-set JSON（`convert.py`）→ 用 sing-box v1.14.0 编译为 .srs
3. `anti-ad` / `geosite-category-ads-all`：直接下载官方 .srs 存档
4. 与仓库现有文件对比，**内容变化才提交推送**（无变化跳过）

上游更新后，本仓库次日同步；sing-box 客户端侧配置 `update_interval` 自行拉取新版。
