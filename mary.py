#include <stdio.h>
#include <conio.h>
#include <windows.h>

#define WIDTH 30
#define HEIGHT 20

int main() {
    int x = WIDTH / 2;
    int y = HEIGHT - 1;
    char map[HEIGHT][WIDTH] = {
        "##############################",
        "#                            #",
        "#                            #",
        "#                            #",
        "#                            #",
        "#                            #",
        "#                            #",
        "#                            #",
        "#                            #",
        "#                            #",
        "#                            #",
        "#                            #",
        "#                            #",
        "#                            #",
        "#                            #",
        "#                            #",
        "#                            #",
        "#                            #",
        "#                            #",
        "##############################"
    };

    while (1) {
        system("cls");

        // 绘制地图
        for (int i = 0; i < HEIGHT; i++) {
            printf("%s\n", map[i]);
        }

        // 读取键盘输入
        if (_kbhit()) {
            char input = _getch();

            // 根据输入移动玛丽
            switch (input) {
                case 'a':
                    if (map[y][x - 1] == ' ') {
                        map[y][x] = ' ';
                        x -= 1;
                        map[y][x] = 'M';
                    }
                    break;
                case 'd':
                    if (map[y][x + 1] == ' ') {
                        map[y][x] = ' ';
                        x += 1;
                        map[y][x] = 'M';
                    }
                    break;
                case 'q':
                    return 0;
                    break;
            }
        }

        // 移动完成后的操作（例如碰撞检测、游戏结束等）
    }

    return 0;
}
