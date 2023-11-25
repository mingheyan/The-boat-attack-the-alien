class Settings(): 
    """存储《外星人入侵》的所有设置的类""" 
 
    def __init__(self): 
        """初始化游戏的设置""" 
        # 屏幕设置 
        self.screen_width = 1200 
        self.screen_height = 800 
        self.bg_color = (128, 128, 128)
        self.ship_speed_factor = 1.5
        
        self.bullet_width = 6 
        self.bullet_height = 15 
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 7  
        self.alien_speed_factor = 1 
        self.fleet_drop_speed = 10 
        # fleet_direction为1表示向右
        # 移，为-1表示向左移 
        self.fleet_direction = 1 
        self.bullet_speed_factor = 3 
        self.ship_limit = 3 
        self.score_scale = 1.5
          # 以什么样的速度加快游戏节奏 
        self.speedup_scale = 1.1 
        self.initialize_dynamic_settings() 
    def initialize_dynamic_settings(self): 
    
        self.ship_speed_factor = 1.5 
        self.bullet_speed_factor = 3 
        self.alien_speed_factor = 1 

        # fleet_direction为1表示向右；为-1表示向左 
        self.fleet_direction = 1
        self.alien_points = 50
    def increase_speed(self): 
    
        self.ship_speed_factor *= self.speedup_scale 
        self.bullet_speed_factor *= self.speedup_scale 
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)