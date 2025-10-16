通过以 管理员 模式打开 PowerShell 并输入以下命令列出连接到 Windows 的所有 USB 设备。 列出设备后，选择并复制要附加到 WSL 的设备总线 ID。

```PowerShell
usbipd list
```

在附加 USB 设备之前，必须使用该命令 usbipd bind 来共享设备，从而允许它附加到 WSL。 这需要管理员权限。 选择要在 WSL 中使用的设备的总线 ID，然后运行以下命令。 运行命令后，请再次使用命令 usbipd list 验证设备是否共享。

```PowerShell
usbipd bind --busid 4-4
```
若要附加 USB 设备，请运行以下命令。 （不再需要使用提升的管理员提示。确保 WSL 命令提示符处于打开状态，以使 WSL 2 轻型 VM 保持活动状态。 请注意，只要 USB 设备连接到 WSL，Windows 将无法使用它。 一旦连接到 WSL，任何在 WSL 2 上运行的发行版都可以使用该 USB 设备。 请确认设备是否已连接 usbipd list。 在 WSL 提示符下，运行 lsusb 以验证 USB 设备是否已列出，并且可以使用 Linux 工具与之交互。

```PowerShell
usbipd attach --wsl --busid <busid>
```

打开 Ubuntu（或首选 WSL 命令行），并使用以下命令列出附加的 USB 设备：

```Bash
lsusb
```