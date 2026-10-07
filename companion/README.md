# 比格小馆长 · macOS 桌面伴侣

让 PaperBank 的比格在桌面挥挥手。透明浮窗，拖动移动；右键或点菜单栏的 🐶，可以暂停、回到右下角、打开指南或退出。系统开启“减少动态效果”时使用静态图。

支持 macOS 12 及以上，Apple Silicon 与 Intel。没有外部依赖，不装开机启动项；不读屏幕、不收集数据。只有点击“打开论文指南”才会打开浏览器。

下载版：解压 `beagle-desktop.zip`，双击 `PaperBank Beagle.app`。应用未经 Apple 公证；可先查看源码并自行构建。若系统拦截，按系统提示自行决定是否打开，无需关闭 Gatekeeper。

源码版需要 Apple Command Line Tools 自带的 Swift 编译器。在完整 PaperBank 项目中运行：

```sh
sh companion/build.sh
open "companion/outputs/PaperBank Beagle.app"
```

编译结果写入 `companion/outputs/`。脚本从自身位置找到 `../assets/` 内的比格 logo、静态图与 GIF，不依赖启动目录。应用退出后没有后台进程。

原生程序源码采用 MIT 许可；比格图像与动画采用 CC BY 4.0。转载素材请带上 [Da1yuqin / PaperBank 的出处](https://da1yuqin.github.io/PaperBank/)、许可和修改说明；许可全文见项目根目录 `LICENSE`。
