import pygame.ftfont

class Button():
    def __init__(self,ai_settings,screen,msg):
        self.screen=screen
        self.screen_rect=screen.get_rect()
        #按钮的属性
        self.width,self.height=200,50
        self.button_color=(255,255,0)
        self.text_color=(255,255,255)
        self.font=pygame.font.SysFont(None,48)# None为默认字体，48为字号

        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center

        self.prep_msg(msg)

    def prep_msg(self,msg):
        """将msg渲染成图像，并于按钮上居中"""
        self.msg_image=self.font.render(msg,True,self.text_color,self.button_color) #将msg储存的文本转为图像
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)