import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((1600, 900)) #Surfaceを生成
    clock  = pg.time.Clock()
    bg_img = pg.image.load("C:\\Users\\c0a22\\OneDrive\\ドキュメント\\CS2年後期\\ProjExD2023\\ex01\\fig\\pg_bg.jpg") #画像の読み込み
    bg_img2 = pg.image.load("C:\\Users\\c0a22\\OneDrive\\ドキュメント\\CS2年後期\\ProjExD2023\\ex01\\fig\\pg_bg.jpg")#反転画像
    bg_img2 = pg.transform.flip(bg_img,True,False)
    kk_img=pg.image.load("C:\\Users\\c0a22\\OneDrive\\ドキュメント\\CS2年後期\\ProjExD2023\\ex01\\fig\\3.png")
    kk_img=pg.transform.flip(kk_img,True,False)#上書き代入
    kk_img2=pg.transform.rotozoom(kk_img,10,1.0)
    kk_imgs=[kk_img,kk_img2]#回転した奴としてないやつのリスト
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x=tmr%1600
            

        screen.blit(bg_img2, [-x, 0])#さいしょ
        screen.blit(bg_img, [1600-x, 0])#さいご(tmrが1600になったとき)
        screen.blit(kk_imgs[tmr%2], [300, 200]) #こうかとんの読み込み
    
        
        #screen.blit(kk_img, [300, 200]) #こうかとんの読み込み
        pg.display.update()
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
