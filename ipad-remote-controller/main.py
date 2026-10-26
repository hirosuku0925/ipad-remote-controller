import struct

def create_hid_mouse_report(button: int, dx: int, dy: int, wheel: int = 0) -> bytes:
    """
    Bluetooth HID マウスレポート（4バイト）を生成する関数
    - button: 0=なし, 1=左クリック, 2=右クリック
    - dx: X軸の移動量 (-127 〜 127)
    - dy: Y軸の移動量 (-127 〜 127)
    - wheel: スクロール量 (-127 〜 127)
    """
    dx = max(-127, min(127, dx))
    dy = max(-127, min(127, dy))
    wheel = max(-127, min(127, wheel))
    
    return struct.pack('bbbb', button, dx, dy, wheel)

if __name__ == "__main__":
    print("=== iPad Remote Controller (Codespaces Build) ===")
    
    # テストパケット生成
    report = create_hid_mouse_report(button=1, dx=15, dy=-5)
    print(f"生成されたHIDパケット (HEX): {report.hex()}")
