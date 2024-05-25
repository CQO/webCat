import ctypes
import json
import pygetwindow as gw


def main():
    window_titles = gw.getAllTitles()
    print(window_titles)
    user32 = ctypes.windll.user32
    screen_width = user32.GetSystemMetrics(0)
    screen_height = user32.GetSystemMetrics(1) - 70

    print(f"屏幕宽度: {screen_width}")
    print(f"屏幕高度: {screen_height}")
    # 读取 JSON 文件
    with open('config.json', 'r') as json_file:
        data = json.load(json_file)
        print(data["point"])
        window = gw.getWindowsWithTitle('bet365 - 在线体育投注 - Google Chrome')
        ind = 0
        for item in window:
            if (len(data["point"]) > ind):
                item.moveTo(data["point"][0], data["point"][1])
                item.resizeTo(data["point"][2], data["point"][3])
            ind += 1

    input("Press Enter to exit...")
# def main():
#     window_titles = gw.getAllTitles()
#     print(window_titles)
#     user32 = ctypes.windll.user32
#     screen_width = user32.GetSystemMetrics(0)
#     screen_height = user32.GetSystemMetrics(1) - 70

#     print(f"屏幕宽度: {screen_width}")
#     print(f"屏幕高度: {screen_height}")
#     while True:
#         print("请选择一个操作：")
#         print("1. 一屏一个窗口")
#         print("2. 一屏两个窗口")
#         print("3. 一屏三个窗口")
#         print("4. 退出")

#         choice = input("输入你的选择：")

#         if choice == '4':
#             print("退出程序")
#             break
#         if choice == '1':
#             # 设置新的窗口大小
#             window = gw.getWindowsWithTitle('bet365 - 在线体育投注 - Google Chrome')
#             for item in window:
#                 item.moveTo(0, 0)
#                 item.resizeTo(screen_width, screen_height)
#         if choice == '2':
#             # 设置新的窗口大小
#             screen_height_copy = screen_height + 135
#             window = gw.getWindowsWithTitle('bet365 - 在线体育投注 - Google Chrome')
#             ind = 0
#             for item in window:
#                 ind += 1
#                 if (ind == 1):
#                     item.moveTo(0, 0)
#                     item.resizeTo(screen_width, int(screen_height_copy / 2))
#                 if (ind == 2):
#                     item.moveTo(0, int(screen_height_copy / 2) - 135)
#                     item.resizeTo(screen_width, int(screen_height_copy / 2))
#         if choice == '3':
#             # 设置新的窗口大小
#             window = gw.getWindowsWithTitle('bet365 - 在线体育投注 - Google Chrome')
#             ind = 0
#             screen_height_copy = screen_height + 270
#             for item in window:
#                 ind += 1
#                 if (ind == 1):
#                     item.moveTo(0, 0)
#                     item.resizeTo(screen_width, int(screen_height_copy / 3))
#                 if (ind == 2):
#                     item.moveTo(0, int(screen_height_copy / 3) - 135)
#                     item.resizeTo(screen_width, int(screen_height_copy / 3))
#                 if (ind == 3):
#                     item.moveTo(0, int(screen_height_copy / 3 * 2) - 270)
#                     item.resizeTo(screen_width, int(screen_height_copy / 3))
if __name__ == "__main__":
    main()