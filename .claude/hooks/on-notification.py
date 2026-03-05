#!/usr/bin/env python3
# Notification hook — sends an OS notification when Claude needs user attention

import sys
import json
import platform
import subprocess

data = json.load(sys.stdin)
message = data.get("message", "Claude needs your attention")

title = "Claude Code - Action Required"

system = platform.system()

if system == "Darwin":
    subprocess.run([
        "osascript", "-e",
        f'display notification "{message}" with title "{title}" sound name "Ping"'
    ])
elif system == "Linux":
    subprocess.run(["notify-send", "-u", "critical", title, message])
elif system == "Windows":
    ps_script = (
        f"[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType=WindowsRuntime] | Out-Null;"
        f"$template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText02);"
        f"$template.SelectSingleNode('//text[@id=1]').InnerText = '{title}';"
        f"$template.SelectSingleNode('//text[@id=2]').InnerText = '{message}';"
        f"$toast = [Windows.UI.Notifications.ToastNotification]::new($template);"
        f"[Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier('Claude Code').Show($toast);"
    )
    subprocess.run(["powershell", "-Command", ps_script])
