import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((1600, 900)) #Surfaceを生成
    clock  = pg.time.Clock()
    bg_img = pg.image.load("C:\\Users\\c0a22\\OneDrive\\ドキュメント\\CS2年後期\\ProjExD2023\\ex01\\fig\\pg_bg.jpg") #画像の読み込み
    kk_img=pg.image.load("C:\\Users\\c0a22\\OneDrive\\ドキュメント\\CS2年後期\\ProjExD2023\\ex01\\fig\\3.png")
    kk_img=pg.transform.flip(kk_img,True,False)#上書き代入
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [300, 200]) #追加行
        pg.display.update()
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
