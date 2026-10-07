import Cocoa

// Native app code: MIT. Beagle artwork: CC BY 4.0; see the project LICENSE.
final class BeagleView: NSImageView {
    override func mouseDown(with event: NSEvent) {
        window?.performDrag(with: event)
    }

    override func rightMouseDown(with event: NSEvent) {
        guard let menu else { return }
        NSMenu.popUpContextMenu(menu, with: event, for: self)
    }
}

final class CompanionApp: NSObject, NSApplicationDelegate {
    private let size = NSSize(width: 160, height: 240)
    private var window: NSWindow!
    private var view: BeagleView!
    private var statusItem: NSStatusItem!
    private var pauseItem: NSMenuItem!
    private var motionItem: NSMenuItem!
    private var paused = false
    private var still: NSImage!
    private var animation: NSImage?

    func applicationDidFinishLaunching(_ notification: Notification) {
        guard let imageURL = Bundle.main.url(forResource: "beagle-pet", withExtension: "png"),
              let image = NSImage(contentsOf: imageURL) else {
            let alert = NSAlert()
            alert.messageText = "没有找到比格图片"
            alert.informativeText = "请保留完整的 PaperBank Beagle.app，或从项目重新运行 build.sh。"
            alert.runModal()
            NSApp.terminate(nil)
            return
        }
        still = image
        if let gifURL = Bundle.main.url(forResource: "beagle-wave", withExtension: "gif") {
            animation = NSImage(contentsOf: gifURL)
        }

        window = NSWindow(contentRect: NSRect(origin: .zero, size: size),
                          styleMask: .borderless, backing: .buffered, defer: false)
        window.title = "PaperBank 比格小馆长"
        window.isOpaque = false
        window.backgroundColor = .clear
        window.hasShadow = false
        window.level = .floating
        window.collectionBehavior = [.canJoinAllSpaces, .fullScreenAuxiliary]
        window.isReleasedWhenClosed = false

        view = BeagleView(frame: NSRect(origin: .zero, size: size))
        view.imageScaling = .scaleProportionallyUpOrDown
        view.imageAlignment = .alignCenter
        view.toolTip = "拖动小馆长；右键打开菜单。"
        view.setAccessibilityLabel("PaperBank 比格小馆长，拖动移动，右键打开菜单")
        window.contentView = view

        let menu = NSMenu()
        menu.autoenablesItems = false
        let title = NSMenuItem(title: "PaperBank · 比格小馆长", action: nil, keyEquivalent: "")
        title.isEnabled = false
        menu.addItem(title)
        menu.addItem(.separator())
        pauseItem = addItem("暂停挥手", action: #selector(togglePause), to: menu)
        motionItem = NSMenuItem(title: "", action: nil, keyEquivalent: "")
        motionItem.isEnabled = false
        menu.addItem(motionItem)
        addItem("回到右下角", action: #selector(resetPosition), to: menu)
        addItem("打开论文指南", action: #selector(openGuide), to: menu)
        menu.addItem(.separator())
        addItem("退出桌面伴侣", action: #selector(quit), to: menu, key: "q")
        view.menu = menu

        statusItem = NSStatusBar.system.statusItem(withLength: NSStatusItem.variableLength)
        statusItem.button?.title = "🐶"
        statusItem.button?.toolTip = "PaperBank 比格小馆长"
        statusItem.menu = menu

        NSWorkspace.shared.notificationCenter.addObserver(
            self, selector: #selector(refreshMotion),
            name: NSWorkspace.accessibilityDisplayOptionsDidChangeNotification, object: nil)
        refreshMotion()
        resetPosition()
        window.orderFrontRegardless()
    }

    @discardableResult
    private func addItem(_ title: String, action: Selector, to menu: NSMenu,
                         key: String = "") -> NSMenuItem {
        let item = NSMenuItem(title: title, action: action, keyEquivalent: key)
        item.target = self
        menu.addItem(item)
        return item
    }

    @objc private func refreshMotion() {
        let reduceMotion = NSWorkspace.shared.accessibilityDisplayShouldReduceMotion
        let animate = animation != nil && !paused && !reduceMotion
        view.animates = false
        view.image = animate ? animation : still
        view.animates = animate
        pauseItem.title = paused ? "继续挥手" : "暂停挥手"
        pauseItem.isEnabled = animation != nil && !reduceMotion
        motionItem.title = reduceMotion ? "系统已开启减少动态效果：使用静态图" : "动画仅在本机播放"
    }

    @objc private func togglePause() {
        paused.toggle()
        refreshMotion()
    }

    @objc private func resetPosition() {
        guard let screen = NSScreen.main ?? NSScreen.screens.first else { return }
        let area = screen.visibleFrame
        window.setFrameOrigin(NSPoint(x: area.maxX - size.width - 24, y: area.minY + 24))
    }

    @objc private func openGuide() {
        // The only external action occurs after the user chooses this menu item.
        if let url = URL(string: "https://da1yuqin.github.io/PaperBank/") {
            NSWorkspace.shared.open(url)
        }
    }

    @objc private func quit() {
        NSApp.terminate(nil)
    }
}

let app = NSApplication.shared
let delegate = CompanionApp()
app.setActivationPolicy(.accessory)
app.delegate = delegate
app.run()
