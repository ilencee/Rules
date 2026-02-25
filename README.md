# Rules

代理规则



\# QX填写

```
https://raw.githubusercontent.com/ilencee/Rules/main/Emby.list
``` 

\#Clash verge

<details>

<summary>点击查看 Clash 脚本备注</summary>

```
function main(config) {
  // 1. 定义 rule-providers
  const embyProvider = {
    type: "http",
    behavior: "classical",
    url: "https://raw.githubusercontent.com/ilencee/Rules/main/Emby-clash.list",
    path: "./ruleset/emby.yaml",
    interval: 86400
  };

  // 2. 注入到 config (这里要把两个都放进去)
  config["rule-providers"] = Object.assign({}, config["rule-providers"], {
    "emby-rules": embyProvider,
  });

  // 3. 注入规则到最前方
  const newRules = [
    "RULE-SET,emby-rules,🎯 全球直连",

  ];

  config.rules = [...newRules, ...config.rules];

  return config;
}
``` 
