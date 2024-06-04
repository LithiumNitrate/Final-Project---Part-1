password = []
max_chars_per_line = 28
line_height = 40  # Adjust this value to the desired line spacing

#SCROLLABLE BOX
class ScrollableBox:
    def __init__(self, x, y, w, h, content_funcs, line_height=30):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.content_funcs = content_funcs
        self.scroll_offset = 0
        self.line_height = line_height
        self.visible_lines = int(h / line_height)
        
    def display(self):
        fill(255, 165, 0)
        rect(self.x, self.y, self.w, self.h)
        clip(self.x, self.y, self.w, self.h)  # Restrict drawing to the box area
        fill(0)
        textSize(16)
        textAlign(LEFT, TOP)
        start_line = int(self.scroll_offset / self.line_height)
        end_line = start_line + self.visible_lines
        
        for i in range(start_line, min(end_line, len(self.content_funcs))):
            func = self.content_funcs[i]
            func(self.x + 10, self.y + 10 + (i - start_line) * self.line_height)
        noClip()  # Reset clipping

    def scroll(self, direction):
        self.scroll_offset += direction * self.line_height
        self.scroll_offset = constrain(self.scroll_offset, 0, max(0, len(self.content_funcs) * self.line_height - self.h))


scrollable_box = None

def content1(x, y):
    fill(0)
    text("This is content line 1.", x, y)

def content2(x, y):
    fill(0)
    text("This is content line 2.", x, y)

def content3(x, y):
    fill(0)
    text("This is content line 3.", x, y)

def content4(x, y):
    fill(0)
    text("This is content line 4.", x, y)




#---------------------------- GAME PLAY LOOP ----------------------------------



def setup():
    global scrollable_box
    size(1200, 600)
    frameRate(30)
    
    # Load and set the font
    global font
    font = loadFont("Charter-Roman-48.vlw")
    textFont(font, 28)
    
        # Sample content
    content_funcs = [content1, content2, content3, content4] * 10  # Repeat to have enough content to scroll
    
    # Initialize ScrollableBox
    scrollable_box = ScrollableBox(100, 350, 1000, 300, content_funcs)
    
    
def draw():
    global password
    background(0)
        #SCROLLING TEXT BOX
    
    #DISPLAY FOR THE BOX
    scrollable_box.display()
    
    textAlign(LEFT, CENTER)
    x = len(password)
    
    current_x = 200
    current_y = 200
    
    char_count = 0
    
    fill(255)
    textSize(28)
    for i in range(x):
        _char = password[i]
        
        if char_count >= max_chars_per_line:
            current_x = 200
            current_y += line_height
            char_count = 0
        
        text(_char, current_x, current_y)
        current_x += textWidth(_char) + 5
        char_count += 1
    
    
def keyPressed():
    global password
    if key != CODED:
        if key != BACKSPACE:
            u = str(key)
            password.append(u)
            
            print(password) #TEST
            
        elif key == BACKSPACE and len(password) > 0:
            password.pop()
        elif key == ESC:
            print("Collected password:", ''.join(password))
            exit()
            

def mouseWheel(event):
    scrollable_box.scroll(event.getCount())
