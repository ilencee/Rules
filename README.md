# Rules

代理规则



\# QX填写

```bash

https://raw.githubusercontent.com/ilencee/Rules/main/Emby.list



\#Clash verge

<details>

<summary>点击查看 Clash 脚本备注</summary>

```bash

function main(config) {

&nbsp; // 1. 定义 rule-providers

&nbsp; const embyProvider = {

&nbsp;   type: "http",

&nbsp;   behavior: "classical",

&nbsp;   url: "https://raw.githubusercontent.com/ilencee/Rules/main/Emby-clash.list",

&nbsp;   path: "./ruleset/emby.yaml",

&nbsp;   interval: 86400

&nbsp; };



&nbsp; const steamProvider = {

&nbsp;   type: "http",

&nbsp;   behavior: "classical",

&nbsp;   url: "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/refs/heads/master/Clash/Ruleset/SteamRegionCheck.list",

&nbsp;   path: "./ruleset/SteamRegionCheck.yaml",

&nbsp;   interval: 86400

&nbsp; };



&nbsp; // 2. 注入到 config (这里要把两个都放进去)

&nbsp; config\["rule-providers"] = Object.assign({}, config\["rule-providers"], {

&nbsp;   "emby-rules": embyProvider,

&nbsp;   "steam-rules": steamProvider // 这里的 key 要和下面 newRules 对应

&nbsp; });



&nbsp; // 3. 注入规则到最前方

&nbsp; const newRules = \[

&nbsp;   "RULE-SET,emby-rules,🎯 全球直连",

&nbsp;   "RULE-SET,steam-rules,🎯 全球直连" // 确保这里是小写的 steam-rules

&nbsp; ];



&nbsp; config.rules = \[...newRules, ...config.rules];



&nbsp; return config;

}

}

