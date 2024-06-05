
password = []
max_chars_per_line = 28
line_height = 40  # Adjust this value to the desired line spacing

#------------------------ SCROLLABLE BOX --------------------------------
class ScrollableBox:
    def __init__(self, x, y, w, h, content_funcs, content_heights):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.content_funcs = content_funcs
        self.content_heights = content_heights
        self.scroll_offset = 0
        self.visible_height = h
        
    def display(self):
        fill(255, 165, 0)
        rect(self.x, self.y, self.w, self.h, 15)
        clip(self.x, self.y, self.w, self.h)  # Restrict drawing to the box area
        fill(0)
        textSize(16)
        textAlign(LEFT, TOP)
        
        current_y = self.y + 10 - self.scroll_offset
        
        for i in range(len(self.content_funcs)):
            if current_y + self.content_heights[i] > self.y and current_y < self.y + self.h:
                func = self.content_funcs[i]
                func(self.x + 10, current_y)
            current_y += self.content_heights[i]
        
        noClip()  # Reset clipping

    def scroll(self, direction):
        self.scroll_offset += direction * 30  # Adjust this value for scrolling speed
        total_content_height = sum(self.content_heights)
        self.scroll_offset = constrain(self.scroll_offset, 0, max(0, total_content_height - self.visible_height))

scrollable_box = None

# ------------------- RULES ------------------------
# Example content functions
def rule1(x, y):
    text_content = "The Password must contain more than 8 characters"
    rect_w = 850
    rect_h = 50
    fill(255)
    rect(x, y, rect_w, rect_h, 15)
    fill(0)
    text(text_content, x + 30, y + 20)
    return rect_h

def rule2(x, y):
    text_content = "The Password must contain more Paul"
    rect_w = 850
    rect_h = 50
    fill(255)
    rect(x, y, rect_w, rect_h, 15)
    fill(0)
    text(text_content, x + 30, y + 20)
    return rect_h

def rule3(x, y):
    text_content = "The Password must eat shit"
    rect_w = 850
    rect_h = 50
    fill(255)
    rect(x, y, rect_w, rect_h, 15)
    fill(0)
    text(text_content, x + 30, y + 20)
    return rect_h

def rule4(x, y):
    text_content = "IMMA KMS"
    rect_w = 850
    rect_h = 50
    fill(255)
    rect(x, y, rect_w, rect_h, 15)
    fill(0)
    text(text_content, x + 30, y + 20)
    return rect_h

def rule5(x, y):
    text_content = "IMMA KMS"
    rect_w = 850
    rect_h = 50
    fill(255)
    rect(x, y, rect_w, rect_h, 15)
    fill(0)
    text(text_content, x + 30, y + 20)
    return rect_h

def rule6(x, y):
    text_content = "IMMA KMS"
    rect_w = 850
    rect_h = 50
    fill(255)
    rect(x, y, rect_w, rect_h, 15)
    fill(0)
    text(text_content, x + 30, y + 20)
    return rect_h

def rule7(x, y):
    text_content = "IMMA KMS"
    rect_w = 850
    rect_h = 50
    fill(255)
    rect(x, y, rect_w, rect_h, 15)
    fill(0)
    text(text_content, x + 30, y + 20)
    return rect_h

def content_with_tree(x, y):
    global branch
    # Draw a rectangle for background
    rect_w = 620  # Fixed width for the tree drawing area
    rect_h = 360  # Fixed height for the tree drawing area
    fill(255)
    rect(x, y, rect_w, rect_h)
    
    # Set up for drawing the tree inside this rectangle
    pushMatrix()
    translate(x + rect_w / 2, y + rect_h)  # Translate to bottom center of the rectangle
    a = (mouseX / float(width)) * 90
    theta = radians(a)
    stroke(0)
    branch(120, theta)
    popMatrix()
    
    return rect_h

def branch(h, theta):
    # Each branch will be 2/3rds the size of the previous one
    h *= 0.66
    # All recursive functions must have an exit condition
    if h > 2:
        # Save the current state of transformation
        pushMatrix()
        rotate(theta)
        line(0, 0, 0, -h)
        translate(0, -h)
        branch(h, theta)
        popMatrix()
        pushMatrix()
        rotate(-theta)
        line(0, 0, 0, -h)
        translate(0, -h)
        branch(h, theta)
        popMatrix()


# -----------------------------------------------
# ------------------- CONDITIONS ---------------------

# NEED A FUNCTION TO MANAGE CONDITIONS AND RULE.

# I WOULD SUGGEST TO USE A FUNCTION THAT POPS OUT CONTENT FROM CONTENT_FUNCS

# CONTENT_FUNC.pop(CONTENT) if doesn't match REQUIREMENT.

# THIS SHOULD BE HARD CODED AS IT CAN'T CHANGE


#---------------------------- GAME PLAY LOOP ----------------------------------



def setup():
    global scrollable_box, content_funcs
    size(1200, 600)
    frameRate(30)
    
    # Load and set the font
    # global font
    # font = loadFont("Charter-Roman-48.vlw")
    # textFont(font, 28)
    
        # Sample content
    content_funcs = [rule1, rule2, rule3, rule4, rule5, rule6, rule7, content_with_tree]  # IF THIS INPUT IS WRONG. WHOLE FCKING CODE BREAKS. USE WITH CAUTION.
    # Calculate the heights of all content
    content_heights = [func(0, 0) for func in content_funcs]  # Call each function to get its height
    # Initialize ScrollableBox
    scrollable_box = ScrollableBox(100, 250, 900, 300, content_funcs, content_heights)
 
    
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
