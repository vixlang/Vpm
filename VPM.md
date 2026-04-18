# VPM说明

vpm包管理依托git仓库


## 包索引格式
```bash
vpm add fexcode.vnet                # 下载 github.com/fexcode/vnet 仓库  
vpm add fexcode.vnet@master         # 下载 github.com/fexcode/vnet 仓库 master 分支      
vpm add gitee.com:fexcode.vnet      # 下载 gitee.com/fexcode/vnet 仓库  
vpm add gitee:fexcode.vnet@master   # .com 可以省略  
```

> o,我还给自己留了个语法糖（因为我比较喜欢gitee嘛），  
> @fexcode.vpm  # 等价于 gitee:fexcode.vpm

## .vix目录结构示例
```bash
.vix
└── libs
    ├── gitee.com
    |    ├── fexcode
    |    │   ├── vpm
    |    │   └── vpm2
    |    └── fexcode2
    |        └── vpm3
    └── github.com
        ├── fexcode
        │   └── vpm
        ├── fexcode2
        │   └── vpm2
        └── fexcode3
            └── vpm3
```
