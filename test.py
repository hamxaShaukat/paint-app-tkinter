from tkinter import *
import random
import time
from tkinter import colorchooser
from PIL import Image, ImageDraw
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk,Image
import PIL.ImageGrab as ImageGrab
import math
'''
Main Window
'''
root = Tk()
root.title("Paint Application")
root.geometry("1280x640")

fillMode=False

# Whole above frame for everything
Plate=Frame(root,height=110,width=1280)
Plate.grid(row=0,column=0,sticky=NW)

# Frame for Saving 
SavingFrame=Frame(Plate,height=110,width=180,relief=SUNKEN,borderwidth=3)
SavingFrame.grid(row=0,column=0)

# Frame for tools 
Tools=Frame(Plate,height=110,width=180,relief=SUNKEN,borderwidth=3)
Tools.grid(row=0,column=1)

# Shapes Frames
ShapesFrames=Frame(Plate,height=110,width=180,relief=SUNKEN,borderwidth=3)
ShapesFrames.grid(row=0,column=2)

# Stroke Size Frame
StrokeSize=Frame(Plate,height=110,width=180,relief=SUNKEN,borderwidth=3)
StrokeSize.grid(row=0,column=3)

# Polygons Size Frame
Polygons=Frame(Plate,height=110,width=180,relief=SUNKEN,borderwidth=3)
Polygons.grid(row=0,column=4)

# Multiple Color Frames
MultipleColorPlate=Frame(Plate,height=110,width=180)
MultipleColorPlate.grid(row=0,column=6)




def usePencil():
    global defaultColor
    print("I am a pencil")
    # defaultColor.set("black")
    PencilButton.config(bg="#58D68D") #Pencil Button
    EraserButton.config(bg="#BFC9CA") #Eraser Button
    Pentagon_Button.config(bg="#BFC9CA") #Pentagon Button
    Rhombus_Button.config(bg="#BFC9CA") #Rhombus Button
    Equal_Triangle_Button.config(bg="#BFC9CA") #Equal Triangle Button
    Iso_Triangle_Button.config(bg="#BFC9CA") #IsoTriangle Button
    Right_Triangle_Button.config(bg="#BFC9CA") #Right Triangle Button
    Five_Star_Button.config(bg="#BFC9CA") #Five Star Button
    Rectangle_Button.config(bg="#BFC9CA") # Rectangle Button
    Circle_Button.config(bg="#BFC9CA") # Circle Button
    Oval_Button.config(bg="#BFC9CA") # Oval Button
    Line_Button.config(bg="#BFC9CA") # Line Button
    Curve_Line_Button.config(bg="#BFC9CA") # Curve Line Button
    HexButton.config(bg="#BFC9CA") # Hex Button
    BucketButton.config(bg="#BFC9CA") # Bucket Button
    PickerButton.config(bg="#BFC9CA") # Pick Button
    SaveButton.config(bg="#BFC9CA") # Save Button
    ClearButton.config(bg="#BFC9CA") # Clear Button
    NewButton.config(bg="#BFC9CA") # New Button
    mainCanvas["cursor"]="fleur"
    mainCanvas.bind("<B1-Motion>", paint)
    mainCanvas.bind("<ButtonRelease-1>", paint)

def useEraser():
    global defaultColor
    print("I am a Eraser")
    defaultColor.set("white")
    PencilButton.config(bg="#BFC9CA") #Pencil Button
    EraserButton.config(bg="#58D68D") #Eraser Button
    Pentagon_Button.config(bg="#BFC9CA") #Pentagon Button
    Rhombus_Button.config(bg="#BFC9CA") #Rhombus Button
    Equal_Triangle_Button.config(bg="#BFC9CA") #Equal Triangle Button
    Iso_Triangle_Button.config(bg="#BFC9CA") #IsoTriangle Button
    Right_Triangle_Button.config(bg="#BFC9CA") #Right Triangle Button
    Five_Star_Button.config(bg="#BFC9CA") #Five Star Button
    Rectangle_Button.config(bg="#BFC9CA") # Rectangle Button
    Circle_Button.config(bg="#BFC9CA") # Circle Button
    Oval_Button.config(bg="#BFC9CA") # Oval Button
    Line_Button.config(bg="#BFC9CA") # Line Button
    Curve_Line_Button.config(bg="#BFC9CA") # Curve Line Button
    HexButton.config(bg="#BFC9CA") # Hex Button
    BucketButton.config(bg="#BFC9CA") # Bucket Button
    PickerButton.config(bg="#BFC9CA") # Pick Button
    SaveButton.config(bg="#BFC9CA") # Save Button
    ClearButton.config(bg="#BFC9CA") # Clear Button
    NewButton.config(bg="#BFC9CA") # New Button
    mainCanvas["cursor"]=DOTBOX
    mainCanvas.bind("<B1-Motion>", paint)
    mainCanvas.bind("<ButtonRelease-1>", paint)

def useMagnifier():
    global defaultColor
    print("I am a Eraser")
    defaultColor.set("white")
    PencilButton.config(bg="#BFC9CA") #Pencil Button
    EraserButton.config(bg="#BFC9CA") #Eraser Button
    Pentagon_Button.config(bg="#BFC9CA") #Pentagon Button
    Rhombus_Button.config(bg="#BFC9CA") #Rhombus Button
    Equal_Triangle_Button.config(bg="#BFC9CA") #Equal Triangle Button
    Iso_Triangle_Button.config(bg="#BFC9CA") #IsoTriangle Button
    Right_Triangle_Button.config(bg="#BFC9CA") #Right Triangle Button
    Five_Star_Button.config(bg="#BFC9CA") #Five Star Button
    Rectangle_Button.config(bg="#BFC9CA") # Rectangle Button
    Circle_Button.config(bg="#BFC9CA") # Circle Button
    Oval_Button.config(bg="#BFC9CA") # Oval Button
    Line_Button.config(bg="#BFC9CA") # Line Button
    Curve_Line_Button.config(bg="#BFC9CA") # Curve Line Button
    HexButton.config(bg="#BFC9CA") # Hex Button
    BucketButton.config(bg="#BFC9CA") # Bucket Button
    PickerButton.config(bg="#BFC9CA") # Pick Button
    SaveButton.config(bg="#BFC9CA") # Save Button
    MagnifierButton.config(bg="#58D68D") # Save Button
    ClearButton.config(bg="#BFC9CA") # Clear Button
    NewButton.config(bg="#BFC9CA") # New Button
    mainCanvas["cursor"]=DOTBOX
    root.bind("<MouseWheel>", magnify)



def useDefaultButton():
    stroke_size=0

def clearCanvas():
    if messagebox.askyesno("Paint App", "Do you want to clear everything....." ):
        mainCanvas.delete("all")
def newCanvas():
    if messagebox.askyesno("Paint App", "Do you want to save before you clear everything....." ):
        mainCanvas.delete("all")
    clearCanvas()


def pick_color(event):
    global default_color
    x = event.x
    y = event.y
    closest_items = mainCanvas.find_closest(x, y)
    print("Picked")

    if closest_items:
        color = mainCanvas.itemcget(closest_items[0], "fill")
        print(color)
        defaultColor.set(color)



def usePick():
    global defaultColor
    PencilButton.config(bg="#BFC9CA") #Pencil Button
    EraserButton.config(bg="#BFC9CA") #Eraser Button
    Pentagon_Button.config(bg="#BFC9CA") #Pentagon Button
    Rhombus_Button.config(bg="#BFC9CA") #Rhombus Button
    Equal_Triangle_Button.config(bg="#BFC9CA") #Equal Triangle Button
    Iso_Triangle_Button.config(bg="#BFC9CA") #IsoTriangle Button
    Right_Triangle_Button.config(bg="#BFC9CA") #Right Triangle Button
    Five_Star_Button.config(bg="#BFC9CA") #Five Star Button
    Rectangle_Button.config(bg="#BFC9CA") # Rectangle Button
    Circle_Button.config(bg="#BFC9CA") # Circle Button
    Oval_Button.config(bg="#BFC9CA") # Oval Button
    Line_Button.config(bg="#BFC9CA") # Line Button
    Curve_Line_Button.config(bg="#BFC9CA") # Curve Line Button
    HexButton.config(bg="#BFC9CA") # Hex Button
    BucketButton.config(bg="#BFC9CA") # Bucket Button
    PickerButton.config(bg="#58D68D") # Pick Button
    SaveButton.config(bg="#BFC9CA") # Save Button
    ClearButton.config(bg="#BFC9CA") # Clear Button
    NewButton.config(bg="#BFC9CA") # New Button
    mainCanvas["cursor"]=DOTBOX
    mainCanvas.bind("<Button-1>", pick_color)
    mainCanvas.bind("<ButtonRelease-1>", pick_color)


'''
Colors for Buttons

'''


def selectColor():
    chosenColor=colorchooser.askcolor(title="Select your Choice")
    defaultColor.set(chosenColor[1])



def saveImage():
    fileLoc=filedialog.asksaveasfilename(defaultextension="png")
    x=root.winfo_rootx()+55
    y=root.winfo_rooty()+160
    img=ImageGrab.grab(bbox=(x,y,x+1600,y+660))
    img.show()
    img.save(fileLoc)
    
def load_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.gif")])
    if file_path:
        image = Image.open(file_path)
        image = image.resize((1280,530 ), Image.BILINEAR)
        image = ImageTk.PhotoImage(image)
        mainCanvas.create_image(0, 0, image=image, anchor='nw')
        mainCanvas.image = image


def start_typing():
    mainCanvas.unbind('<Button-1>')
    mainCanvas.bind('<Button-1>', create_text)

def create_text(event):
    x = event.x
    y = event.y
    text_input =Text(mainCanvas, width=20, height=1)
    mainCanvas.create_window(x, y, window=text_input, anchor='nw')
    text_input.focus_set()
    text_input.bind('<Return>', hide_cursor)

def hide_cursor(event):
    text_input = event.widget
    text = text_input.get('1.0', 'end-1c')
    x = text_input.winfo_x()
    y = text_input.winfo_y()
    mainCanvas.create_text(x, y, text=text, anchor='nw')
    text_input.destroy()
    mainCanvas.unbind('<Button-1>')





'''
Hexagon

'''


def useHexagon():
    global defaultColor
    print("I am a Hexagon")
    PencilButton.config(bg="#BFC9CA") #Pencil Button
    EraserButton.config(bg="#BFC9CA") #Eraser Button
    Pentagon_Button.config(bg="#BFC9CA") #Pentagon Button
    Rhombus_Button.config(bg="#BFC9CA") #Rhombus Button
    Equal_Triangle_Button.config(bg="#BFC9CA") #Equal Triangle Button
    Iso_Triangle_Button.config(bg="#BFC9CA") #IsoTriangle Button
    Right_Triangle_Button.config(bg="#BFC9CA") #Right Triangle Button
    Five_Star_Button.config(bg="#BFC9CA") #Five Star Button
    Rectangle_Button.config(bg="#BFC9CA") # Rectangle Button
    Circle_Button.config(bg="#BFC9CA") # Circle Button
    Oval_Button.config(bg="#BFC9CA") # Oval Button
    Line_Button.config(bg="#BFC9CA") # Line Button
    Curve_Line_Button.config(bg="#BFC9CA") # Curve Line Button
    HexButton.config(bg="#58D68D") # Hex Button
    BucketButton.config(bg="#BFC9CA") # Bucket Button
    PickerButton.config(bg="#BFC9CA") # Pick Button
    SaveButton.config(bg="#BFC9CA") # Save Button
    ClearButton.config(bg="#BFC9CA") # Clear Button
    NewButton.config(bg="#BFC9CA") # New Button
    start_drawing()

def start_drawing():
    mainCanvas.unbind("<B1-Motion>")  # Unbind the paint function from <B1-Motion> event
    mainCanvas.unbind("<ButtonRelease-1>")  # Unbind the paint function from <ButtonRelease-1> event
    mainCanvas.bind("<Button-1>", initiate_drawing)
    mainCanvas.bind("<B1-Motion>", create_hexagon)
    mainCanvas.bind("<ButtonRelease-1>", stop_drawing)

def initiate_drawing(event):
    global x_start, y_start
    x_start, y_start = event.x, event.y

def create_hexagon(event):
    mainCanvas.delete("Hexagon")
    x_center, y_center = (x_start + event.x) / 2, (y_start + event.y) / 2
    radius = abs(event.x - x_start)  # Use the distance between the center and any vertex as the radius
    vertices = []
    for i in range(6):
        angle = 2 * math.pi * (i / 6)  # Calculate the angle for each vertex
        x = x_center + radius * math.cos(angle)
        y = y_center + radius * math.sin(angle)
        vertices.extend([x, y])
    mainCanvas.create_polygon(vertices, fill="", outline="black", tags="Hexagon")
   



def stop_drawing(event):
    print("i am unbinding")
    mainCanvas.unbind("<Button-1>")
    mainCanvas.unbind("<B1-Motion>")
    mainCanvas.unbind("<ButtonRelease-1>")







'''
Heptagon

'''


def useHeptagon():
    global defaultColor
    print("I am a Hexagon")
    PencilButton.config(bg="#BFC9CA") #Pencil Button
    EraserButton.config(bg="#BFC9CA") #Eraser Button
    Pentagon_Button.config(bg="#BFC9CA") #Pentagon Button
    Rhombus_Button.config(bg="#BFC9CA") #Rhombus Button
    Equal_Triangle_Button.config(bg="#BFC9CA") #Equal Triangle Button
    Iso_Triangle_Button.config(bg="#BFC9CA") #IsoTriangle Button
    Right_Triangle_Button.config(bg="#BFC9CA") #Right Triangle Button
    Five_Star_Button.config(bg="#BFC9CA") #Five Star Button
    Rectangle_Button.config(bg="#BFC9CA") # Rectangle Button
    Circle_Button.config(bg="#BFC9CA") # Circle Button
    Oval_Button.config(bg="#BFC9CA") # Oval Button
    Line_Button.config(bg="#BFC9CA") # Line Button
    Curve_Line_Button.config(bg="#BFC9CA") # Curve Line Button
    HexButton.config(bg="#BFC9CA") # Hex Button
    BucketButton.config(bg="#BFC9CA") # Bucket Button
    PickerButton.config(bg="#BFC9CA") # Pick Button
    SaveButton.config(bg="#BFC9CA") # Save Button
    ClearButton.config(bg="#BFC9CA") # Clear Button
    NewButton.config(bg="#BFC9CA") # New Button
    mainCanvas["cursor"]=DOTBOX
    start_drawing_heptagon()

def start_drawing_heptagon():
   # print("I am in the function doing my")
    mainCanvas.unbind("<B1-Motion>")  # Unbind the paint function from <B1-Motion> event
    mainCanvas.unbind("<ButtonRelease-1>")  # Unbind the paint function from <ButtonRelease-1> event
    mainCanvas.bind("<Button-1>", initiate_drawing_heptagon)
    mainCanvas.bind("<B1-Motion>", create_heptagon)
    mainCanvas.bind("<ButtonRelease-1>", stop_drawing_heptagon)

def initiate_drawing_heptagon(event):
    global x_start, y_start
    x_start, y_start = event.x, event.y

def create_heptagon(event):
    mainCanvas.delete("Heptagon")
    x_center, y_center = (x_start + event.x) / 2, (y_start + event.y) / 2
    radius = abs(event.x - x_start)  # Use the distance between the center and any vertex as the radius
    vertices = []
    for i in range(7):
        angle = 2 * math.pi * (i / 7)  # Calculate the angle for each vertex
        x = x_center + radius * math.cos(angle)
        y = y_center + radius * math.sin(angle)
        vertices.extend([x, y])
    mainCanvas.create_polygon(vertices, fill="", outline="black", tags="Heptagon")
   



def stop_drawing_heptagon(event):
    print("i am unbinding")
    mainCanvas.unbind("<Button-1>")
    mainCanvas.unbind("<B1-Motion>")
    mainCanvas.unbind("<ButtonRelease-1>")







'''
Heart
'''
def useHeart():
    global defaultColor
    print("I am a Hexagon")
    PencilButton.config(bg="#BFC9CA") #Pencil Button
    EraserButton.config(bg="#BFC9CA") #Eraser Button
    Pentagon_Button.config(bg="#BFC9CA") #Pentagon Button
    Rhombus_Button.config(bg="#BFC9CA") #Rhombus Button
    Equal_Triangle_Button.config(bg="#BFC9CA") #Equal Triangle Button
    Iso_Triangle_Button.config(bg="#BFC9CA") #IsoTriangle Button
    Right_Triangle_Button.config(bg="#BFC9CA") #Right Triangle Button
    Five_Star_Button.config(bg="#BFC9CA") #Five Star Button
    Rectangle_Button.config(bg="#BFC9CA") # Rectangle Button
    Circle_Button.config(bg="#BFC9CA") # Circle Button
    Oval_Button.config(bg="#BFC9CA") # Oval Button
    Line_Button.config(bg="#BFC9CA") # Line Button
    Curve_Line_Button.config(bg="#BFC9CA") # Curve Line Button
    HexButton.config(bg="#BFC9CA") # Hex Button
    BucketButton.config(bg="#BFC9CA") # Bucket Button
    PickerButton.config(bg="#BFC9CA") # Pick Button
    SaveButton.config(bg="#BFC9CA") # Save Button
    ClearButton.config(bg="#BFC9CA") # Clear Button
    NewButton.config(bg="#BFC9CA") # New Button
    mainCanvas["cursor"]=DOTBOX
    start_drawing_heart()




def start_drawing_heart():
    mainCanvas.unbind("<B1-Motion>")  # Unbind the paint function from <B1-Motion> event
    mainCanvas.unbind("<ButtonRelease-1>")  # Unbind the paint function from <ButtonRelease-1> event
    mainCanvas.bind("<Button-1>", initiate_drawing_heart)
    mainCanvas.bind("<B1-Motion>", create_heart)
    mainCanvas.bind("<ButtonRelease-1>", stop_drawing_heart)

def initiate_drawing_heart(event):
    global x_start, y_start
    x_start, y_start = event.x, event.y

def create_heart(event):
    mainCanvas.delete("Heart")
    x_center, y_center = (x_start + event.x) / 2, (y_start + event.y) / 2
    radius = abs(event.x - x_start)  # Use the distance between the center and any vertex as the radius
    vertices = []
    for angle in range(0, 360):
        radian = math.radians(angle)
        x = x_center + radius * 16 * (math.sin(radian) ** 3)
        y = y_center - radius * (13 * math.cos(radian) - 5 * math.cos(2 * radian) - 2 * math.cos(3 * radian) - math.cos(4 * radian))
        vertices.append(x)
        vertices.append(y)
    mainCanvas.create_polygon(vertices, fill="", outline="black", tags="Heart")

def stop_drawing_heart(event):
    mainCanvas.unbind("<Button-1>")
    mainCanvas.unbind("<B1-Motion>")
    mainCanvas.unbind("<ButtonRelease-1>")


'''
Cloud
'''
def useCloud():
    global defaultColor
    print("I am a Hexagon")
    PencilButton.config(bg="#BFC9CA") #Pencil Button
    EraserButton.config(bg="#BFC9CA") #Eraser Button
    Pentagon_Button.config(bg="#BFC9CA") #Pentagon Button
    Rhombus_Button.config(bg="#BFC9CA") #Rhombus Button
    Equal_Triangle_Button.config(bg="#BFC9CA") #Equal Triangle Button
    Iso_Triangle_Button.config(bg="#BFC9CA") #IsoTriangle Button
    Right_Triangle_Button.config(bg="#BFC9CA") #Right Triangle Button
    Five_Star_Button.config(bg="#BFC9CA") #Five Star Button
    Rectangle_Button.config(bg="#BFC9CA") # Rectangle Button
    Circle_Button.config(bg="#BFC9CA") # Circle Button
    Oval_Button.config(bg="#BFC9CA") # Oval Button
    Line_Button.config(bg="#BFC9CA") # Line Button
    Curve_Line_Button.config(bg="#BFC9CA") # Curve Line Button
    HexButton.config(bg="#BFC9CA") # Hex Button
    BucketButton.config(bg="#BFC9CA") # Bucket Button
    PickerButton.config(bg="#BFC9CA") # Pick Button
    SaveButton.config(bg="#BFC9CA") # Save Button
    ClearButton.config(bg="#BFC9CA") # Clear Button
    NewButton.config(bg="#BFC9CA") # New Button
    mainCanvas["cursor"]=DOTBOX
    start_drawing_cloud()

def start_drawing_cloud():
    mainCanvas.unbind("<B1-Motion>")
    mainCanvas.unbind("<ButtonRelease-1>")
    mainCanvas.bind("<Button-1>", initiate_drawing_cloud)
    mainCanvas.bind("<B1-Motion>", create_cloud)
    mainCanvas.bind("<ButtonRelease-1>", stop_drawing_cloud)

def initiate_drawing_cloud(event):
    global x_start, y_start
    x_start, y_start = event.x, event.y

def create_cloud(event):
    mainCanvas.delete("Cloud")
    x_center, y_center = (x_start + event.x) / 2, (y_start + event.y) / 2
    radius = abs(event.x - x_start)  # Use the distance between the center and any vertex as the radius
    num_circles = random.randint(10, 15)
    for _ in range(num_circles):
        x = random.uniform(x_center - radius, x_center + radius)
        y = random.uniform(y_center - radius, y_center + radius)
        circle_radius = random.uniform(0.05, 0.2) * radius
        mainCanvas.create_oval(x - circle_radius, y - circle_radius, x + circle_radius, y + circle_radius, fill="", outline="black", tags="Cloud")

def stop_drawing_cloud(event):
    mainCanvas.unbind("<Button-1>")
    mainCanvas.unbind("<B1-Motion>")
    mainCanvas.unbind("<ButtonRelease-1>")



'''
FPS
'''

def useFPS():
    global defaultColor
    print("I am a Hexagon")
    PencilButton.config(bg="#BFC9CA") #Pencil Button
    EraserButton.config(bg="#BFC9CA") #Eraser Button
    Pentagon_Button.config(bg="#BFC9CA") #Pentagon Button
    Rhombus_Button.config(bg="#BFC9CA") #Rhombus Button
    Equal_Triangle_Button.config(bg="#BFC9CA") #Equal Triangle Button
    Iso_Triangle_Button.config(bg="#BFC9CA") #IsoTriangle Button
    Right_Triangle_Button.config(bg="#BFC9CA") #Right Triangle Button
    Five_Star_Button.config(bg="#BFC9CA") #Five Star Button
    Rectangle_Button.config(bg="#BFC9CA") # Rectangle Button
    Circle_Button.config(bg="#BFC9CA") # Circle Button
    Oval_Button.config(bg="#BFC9CA") # Oval Button
    Line_Button.config(bg="#BFC9CA") # Line Button
    Curve_Line_Button.config(bg="#BFC9CA") # Curve Line Button
    HexButton.config(bg="#BFC9CA") # Hex Button
    BucketButton.config(bg="#BFC9CA") # Bucket Button
    PickerButton.config(bg="#BFC9CA") # Pick Button
    SaveButton.config(bg="#BFC9CA") # Save Button
    ClearButton.config(bg="#BFC9CA") # Clear Button
    NewButton.config(bg="#BFC9CA") # New Button
    mainCanvas["cursor"]=DOTBOX
    start_drawing_star()

def start_drawing_star():
    mainCanvas.unbind("<B1-Motion>")
    mainCanvas.unbind("<ButtonRelease-1>")
    mainCanvas.bind("<Button-1>", initiate_drawing_star)
    mainCanvas.bind("<B1-Motion>", create_star)
    mainCanvas.bind("<ButtonRelease-1>", stop_drawing_star)

def initiate_drawing_star(event):
    global x_start, y_start
    x_start, y_start = event.x, event.y

def create_star(event):
    mainCanvas.delete("Star")
    x_center, y_center = (x_start + event.x) / 2, (y_start + event.y) / 2
    radius = abs(event.x - x_start)  # Use the distance between the center and any vertex as the radius
    outer_radius = radius / 2
    inner_radius = radius / 4
    vertices = []
    for i in range(8):
        angle = math.radians(45 + i * 45)  # Calculate the angle for each vertex
        if i % 2 == 0:
            x = x_center + outer_radius * math.cos(angle)
            y = y_center + outer_radius * math.sin(angle)
        else:
            x = x_center + inner_radius * math.cos(angle)
            y = y_center + inner_radius * math.sin(angle)
        vertices.extend([x, y])
    mainCanvas.create_polygon(vertices, fill="", outline="black", tags="Star")

def stop_drawing_star(event):
    mainCanvas.unbind("<Button-1>")
    mainCanvas.unbind("<B1-Motion>")
    mainCanvas.unbind("<ButtonRelease-1>")


'''
Octagon

'''


def useOctagon():
    global defaultColor
    print("I am a Hexagon")
    PencilButton.config(bg="#BFC9CA") #Pencil Button
    EraserButton.config(bg="#BFC9CA") #Eraser Button
    Pentagon_Button.config(bg="#BFC9CA") #Pentagon Button
    Rhombus_Button.config(bg="#BFC9CA") #Rhombus Button
    Equal_Triangle_Button.config(bg="#BFC9CA") #Equal Triangle Button
    Iso_Triangle_Button.config(bg="#BFC9CA") #IsoTriangle Button
    Right_Triangle_Button.config(bg="#BFC9CA") #Right Triangle Button
    Five_Star_Button.config(bg="#BFC9CA") #Five Star Button
    Rectangle_Button.config(bg="#BFC9CA") # Rectangle Button
    Circle_Button.config(bg="#BFC9CA") # Circle Button
    Oval_Button.config(bg="#BFC9CA") # Oval Button
    Line_Button.config(bg="#BFC9CA") # Line Button
    Curve_Line_Button.config(bg="#BFC9CA") # Curve Line Button
    HexButton.config(bg="#BFC9CA") # Hex Button
    BucketButton.config(bg="#BFC9CA") # Bucket Button
    PickerButton.config(bg="#BFC9CA") # Pick Button
    SaveButton.config(bg="#BFC9CA") # Save Button
    ClearButton.config(bg="#BFC9CA") # Clear Button
    NewButton.config(bg="#BFC9CA") # New Button
    mainCanvas["cursor"]=DOTBOX
    start_drawing_Octagon()

def start_drawing_Octagon():
    mainCanvas.unbind("<B1-Motion>") 
    mainCanvas.unbind("<ButtonRelease-1>") 
    mainCanvas.bind("<Button-1>", initiate_drawing_Octagon)
    mainCanvas.bind("<B1-Motion>", create_Octagon)
    mainCanvas.bind("<ButtonRelease-1>", stop_drawing_Octagon)

def initiate_drawing_Octagon(event):
    global x_start, y_start
    x_start, y_start = event.x, event.y

def create_Octagon(event):
    mainCanvas.delete("Octagon")
    x_center, y_center = (x_start + event.x) / 2, (y_start + event.y) / 2
    radius = abs(event.x - x_start)  # Use the distance between the center and any vertex as the radius
    vertices = []
    for i in range(8):
        angle = 2 * math.pi * (i / 8)  # Calculate the angle for each vertex
        x = x_center + radius * math.cos(angle)
        y = y_center + radius * math.sin(angle)
        vertices.extend([x, y])
    mainCanvas.create_polygon(vertices, fill="", outline="black", tags="Octagon")
   



def stop_drawing_Octagon(event):
    print("i am unbinding")
    mainCanvas.unbind("<Button-1>")
    mainCanvas.unbind("<B1-Motion>")
    mainCanvas.unbind("<ButtonRelease-1>")



'''
9 sided

'''


def use9Gon():
    global defaultColor
    print("I am a Hexagon")
    PencilButton.config(bg="#BFC9CA") #Pencil Button
    EraserButton.config(bg="#BFC9CA") #Eraser Button
    Pentagon_Button.config(bg="#BFC9CA") #Pentagon Button
    Rhombus_Button.config(bg="#BFC9CA") #Rhombus Button
    Equal_Triangle_Button.config(bg="#BFC9CA") #Equal Triangle Button
    Iso_Triangle_Button.config(bg="#BFC9CA") #IsoTriangle Button
    Right_Triangle_Button.config(bg="#BFC9CA") #Right Triangle Button
    Five_Star_Button.config(bg="#BFC9CA") #Five Star Button
    Rectangle_Button.config(bg="#BFC9CA") # Rectangle Button
    Circle_Button.config(bg="#BFC9CA") # Circle Button
    Oval_Button.config(bg="#BFC9CA") # Oval Button
    Line_Button.config(bg="#BFC9CA") # Line Button
    Curve_Line_Button.config(bg="#BFC9CA") # Curve Line Button
    HexButton.config(bg="#BFC9CA") # Hex Button
    BucketButton.config(bg="#BFC9CA") # Bucket Button
    PickerButton.config(bg="#BFC9CA") # Pick Button
    SaveButton.config(bg="#BFC9CA") # Save Button
    ClearButton.config(bg="#BFC9CA") # Clear Button
    NewButton.config(bg="#BFC9CA") # New Button
    mainCanvas["cursor"]=DOTBOX
    start_drawing_Nan()

def start_drawing_Nan():
    mainCanvas.unbind("<B1-Motion>") 
    mainCanvas.unbind("<ButtonRelease-1>") 
    mainCanvas.bind("<Button-1>", initiate_drawing_Nan)
    mainCanvas.bind("<B1-Motion>", create_Nan)
    mainCanvas.bind("<ButtonRelease-1>", stop_drawing_Nan)

def initiate_drawing_Nan(event):
    global x_start, y_start
    x_start, y_start = event.x, event.y

def create_Nan(event):
    mainCanvas.delete("9Gon")
    num_sides = 9  # Number of sides in the nanogon
    x_center, y_center = (x_start + event.x) / 2, (y_start + event.y) / 2
    radius = abs(event.x - x_start)  # Use the distance between the center and any vertex as the radius
    vertices = []
    for i in range(num_sides):
        angle = 2 * math.pi * (i / num_sides)  # Calculate the angle for each vertex
        x = x_center + radius * math.cos(angle)
        y = y_center + radius * math.sin(angle)
        vertices.extend([x, y])
    mainCanvas.create_polygon(vertices, fill="", outline="black", tags="9Gon")
   



def stop_drawing_Nan(event):
    print("i am unbinding")
    mainCanvas.unbind("<Button-1>")
    mainCanvas.unbind("<B1-Motion>")
    mainCanvas.unbind("<ButtonRelease-1>")





'''
10 sided

'''


def use10Gon():
    global defaultColor
    print("I am a Hexagon")
    PencilButton.config(bg="#BFC9CA") #Pencil Button
    EraserButton.config(bg="#BFC9CA") #Eraser Button
    Pentagon_Button.config(bg="#BFC9CA") #Pentagon Button
    Rhombus_Button.config(bg="#BFC9CA") #Rhombus Button
    Equal_Triangle_Button.config(bg="#BFC9CA") #Equal Triangle Button
    Iso_Triangle_Button.config(bg="#BFC9CA") #IsoTriangle Button
    Right_Triangle_Button.config(bg="#BFC9CA") #Right Triangle Button
    Five_Star_Button.config(bg="#BFC9CA") #Five Star Button
    Rectangle_Button.config(bg="#BFC9CA") # Rectangle Button
    Circle_Button.config(bg="#BFC9CA") # Circle Button
    Oval_Button.config(bg="#BFC9CA") # Oval Button
    Line_Button.config(bg="#BFC9CA") # Line Button
    Curve_Line_Button.config(bg="#BFC9CA") # Curve Line Button
    HexButton.config(bg="#BFC9CA") # Hex Button
    BucketButton.config(bg="#BFC9CA") # Bucket Button
    PickerButton.config(bg="#BFC9CA") # Pick Button
    SaveButton.config(bg="#BFC9CA") # Save Button
    ClearButton.config(bg="#BFC9CA") # Clear Button
    NewButton.config(bg="#BFC9CA") # New Button
    mainCanvas["cursor"]=DOTBOX
    start_drawing_decagon()

def start_drawing_decagon():
    mainCanvas.unbind("<B1-Motion>") 
    mainCanvas.unbind("<ButtonRelease-1>") 
    mainCanvas.bind("<Button-1>", initiate_drawing_decagon)
    mainCanvas.bind("<B1-Motion>", create_decagon)
    mainCanvas.bind("<ButtonRelease-1>", stop_drawing_decagon)

def initiate_drawing_decagon(event):
    global x_start, y_start
    x_start, y_start = event.x, event.y

def create_decagon(event):
    mainCanvas.delete("10Gon")
    x_center, y_center = (x_start + event.x) / 2, (y_start + event.y) / 2
    radius = abs(event.x - x_start)  # Use the distance between the center and any vertex as the radius
    vertices = []
    for i in range(10):
        angle = 2 * math.pi * (i / 10)  # Calculate the angle for each vertex
        x = x_center + radius * math.cos(angle)
        y = y_center + radius * math.sin(angle)
        vertices.extend([x, y])
    mainCanvas.create_polygon(vertices, fill="", outline="black", tags="10Gon")
   



def stop_drawing_decagon(event):
    print("i am unbinding")
    mainCanvas.unbind("<Button-1>")
    mainCanvas.unbind("<B1-Motion>")
    mainCanvas.unbind("<ButtonRelease-1>")





'''
11 sided

'''


def use11Gon():
    global defaultColor
    print("I am a Hexagon")
    PencilButton.config(bg="#BFC9CA") #Pencil Button
    EraserButton.config(bg="#BFC9CA") #Eraser Button
    Pentagon_Button.config(bg="#BFC9CA") #Pentagon Button
    Rhombus_Button.config(bg="#BFC9CA") #Rhombus Button
    Equal_Triangle_Button.config(bg="#BFC9CA") #Equal Triangle Button
    Iso_Triangle_Button.config(bg="#BFC9CA") #IsoTriangle Button
    Right_Triangle_Button.config(bg="#BFC9CA") #Right Triangle Button
    Five_Star_Button.config(bg="#BFC9CA") #Five Star Button
    Rectangle_Button.config(bg="#BFC9CA") # Rectangle Button
    Circle_Button.config(bg="#BFC9CA") # Circle Button
    Oval_Button.config(bg="#BFC9CA") # Oval Button
    Line_Button.config(bg="#BFC9CA") # Line Button
    Curve_Line_Button.config(bg="#BFC9CA") # Curve Line Button
    HexButton.config(bg="#BFC9CA") # Hex Button
    BucketButton.config(bg="#BFC9CA") # Bucket Button
    PickerButton.config(bg="#BFC9CA") # Pick Button
    SaveButton.config(bg="#BFC9CA") # Save Button
    ClearButton.config(bg="#BFC9CA") # Clear Button
    NewButton.config(bg="#BFC9CA") # New Button
    mainCanvas["cursor"]=DOTBOX
    start_drawing_11Gon()

def start_drawing_11Gon():
    mainCanvas.unbind("<B1-Motion>") 
    mainCanvas.unbind("<ButtonRelease-1>") 
    mainCanvas.bind("<Button-1>", initiate_drawing_11Gon)
    mainCanvas.bind("<B1-Motion>", create_11Gon)
    mainCanvas.bind("<ButtonRelease-1>", stop_drawing_11Gon)

def initiate_drawing_11Gon(event):
    global x_start, y_start
    x_start, y_start = event.x, event.y

def create_11Gon(event):
    mainCanvas.delete("11Gon")
    x_center, y_center = (x_start + event.x) / 2, (y_start + event.y) / 2
    radius = abs(event.x - x_start)  # Use the distance between the center and any vertex as the radius
    vertices = []
    for i in range(11):
        angle = 2 * math.pi * (i / 11)  # Calculate the angle for each vertex
        x = x_center + radius * math.cos(angle)
        y = y_center + radius * math.sin(angle)
        vertices.extend([x, y])
    mainCanvas.create_polygon(vertices, fill="", outline="black", tags="11Gon")



def stop_drawing_11Gon(event):
    print("i am unbinding")
    mainCanvas.unbind("<Button-1>")
    mainCanvas.unbind("<B1-Motion>")
    mainCanvas.unbind("<ButtonRelease-1>")



'''
N polygons
'''


def usePolygon():
    print("I am in a polygon with number of polygons")
    print(NoOfPolygons.get())
    if(NoOfPolygons.get()==7):
        useHeptagon()
    elif(NoOfPolygons.get()==4):
        useRhombus()
    elif(NoOfPolygons.get()==5):
        usePentagon()
    elif(NoOfPolygons.get()==6):
        useHexagon()
    elif(NoOfPolygons.get()==8):
        useOctagon()
    elif(NoOfPolygons.get()==9):
        use9Gon()
    elif(NoOfPolygons.get()==10):
        use10Gon()
    elif(NoOfPolygons.get()==11):
        use11Gon()



'''
Pentagon drawing

'''

def usePentagon():
    global defaultColor
    print("I am a Hexagon")
    PencilButton.config(bg="#BFC9CA") #Pencil Button
    EraserButton.config(bg="#BFC9CA") #Eraser Button
    Pentagon_Button.config(bg="#58D68D") #Pentagon Button
    Rhombus_Button.config(bg="#BFC9CA") #Rhombus Button
    Equal_Triangle_Button.config(bg="#BFC9CA") #Equal Triangle Button
    Iso_Triangle_Button.config(bg="#BFC9CA") #IsoTriangle Button
    Right_Triangle_Button.config(bg="#BFC9CA") #Right Triangle Button
    Five_Star_Button.config(bg="#BFC9CA") #Five Star Button
    Rectangle_Button.config(bg="#BFC9CA") # Rectangle Button
    Circle_Button.config(bg="#BFC9CA") # Circle Button
    Oval_Button.config(bg="#BFC9CA") # Oval Button
    Line_Button.config(bg="#BFC9CA") # Line Button
    Curve_Line_Button.config(bg="#BFC9CA") # Curve Line Button
    HexButton.config(bg="#BFC9CA") # Hex Button
    BucketButton.config(bg="#BFC9CA") # Bucket Button
    PickerButton.config(bg="#BFC9CA") # Pick Button
    SaveButton.config(bg="#BFC9CA") # Save Button
    ClearButton.config(bg="#BFC9CA") # Clear Button
    NewButton.config(bg="#BFC9CA") # New Button
    mainCanvas["cursor"]=DOTBOX
    start_drawing_pentagon()


def start_drawing_pentagon():
    mainCanvas.unbind("<B1-Motion>") 
    mainCanvas.unbind("<ButtonRelease-1>") 
    mainCanvas.bind("<Button-1>", initiate_drawing_pentagon)
    mainCanvas.bind("<B1-Motion>", create_pentagon)
    mainCanvas.bind("<ButtonRelease-1>", stop_drawing_pentagon)


pentagons = []  # List to store the coordinates of each pentagon

def initiate_drawing_pentagon(event):
    global x_start, y_start
    x_start, y_start = event.x, event.y

def create_pentagon(event):
    mainCanvas.delete("Pentagon")
    x_center, y_center = (x_start + event.x) / 2, (y_start + event.y) / 2
    radius = abs(event.x - x_start)  
    vertices = []
    for i in range(5):
        angle = 2 * math.pi * (i / 5)  
        x = x_center + radius * math.cos(angle)
        y = y_center + radius * math.sin(angle)
        vertices.extend([x, y])
    mainCanvas.create_polygon(vertices, fill="", outline="black", tags="Pentagon")

def stop_drawing_pentagon(event):
    print("I am unbinding")
    mainCanvas.unbind("<Button-1>")
    mainCanvas.unbind("<B1-Motion>")
    mainCanvas.unbind("<ButtonRelease-1>")


'''
Rhombus drawing
'''


def useRhombus():
    global defaultColor
    print("I am a Hexagon")
    PencilButton.config(bg="#BFC9CA") #Pencil Button
    EraserButton.config(bg="#BFC9CA") #Eraser Button
    Pentagon_Button.config(bg="#BFC9CA") #Pentagon Button
    Rhombus_Button.config(bg="#58D68D") #Rhombus Button
    Equal_Triangle_Button.config(bg="#BFC9CA") #Equal Triangle Button
    Iso_Triangle_Button.config(bg="#BFC9CA") #IsoTriangle Button
    Right_Triangle_Button.config(bg="#BFC9CA") #Right Triangle Button
    Five_Star_Button.config(bg="#BFC9CA") #Five Star Button
    Rectangle_Button.config(bg="#BFC9CA") # Rectangle Button
    Circle_Button.config(bg="#BFC9CA") # Circle Button
    Oval_Button.config(bg="#BFC9CA") # Oval Button
    Line_Button.config(bg="#BFC9CA") # Line Button
    Curve_Line_Button.config(bg="#BFC9CA") # Curve Line Button
    HexButton.config(bg="#BFC9CA") # Hex Button
    BucketButton.config(bg="#BFC9CA") # Bucket Button
    PickerButton.config(bg="#BFC9CA") # Pick Button
    SaveButton.config(bg="#BFC9CA") # Save Button
    ClearButton.config(bg="#BFC9CA") # Clear Button
    NewButton.config(bg="#BFC9CA") # New Button
    mainCanvas["cursor"]=DOTBOX
    start_drawing_rhombus()


def start_drawing_rhombus():
    mainCanvas.unbind("<B1-Motion>") 
    mainCanvas.unbind("<ButtonRelease-1>") 
    mainCanvas.bind("<Button-1>", initiate_drawing_rhombus)
    mainCanvas.bind("<B1-Motion>", create_rhombus)
    mainCanvas.bind("<ButtonRelease-1>", stop_drawing_rhombus)



def initiate_drawing_rhombus(event):
    global x_start, y_start
    x_start, y_start = event.x, event.y

def create_rhombus(event):
    mainCanvas.delete("rhombus")

    # x_start, y_start = event.x, event.y
    x_end, y_end = mainCanvas.winfo_pointerx(), mainCanvas.winfo_pointery()

    width = abs(x_end - x_start)
    height = abs(y_end - y_start)

    x1 = x_start - width / 2
    y1 = y_start
    x2 = x_start
    y2 = y_start - height / 2
    x3 = x_start + width / 2
    y3 = y_start
    x4 = x_start
    y4 = y_start + height / 2

    mainCanvas.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4, fill="", outline="black", tags="rhombus")

def stop_drawing_rhombus(event):
    print("I am unbinding")
    mainCanvas.unbind("<Button-1>")
    mainCanvas.unbind("<B1-Motion>")
    mainCanvas.unbind("<ButtonRelease-1>")


'''
Equilateral Triangle
'''
def useEqualTriangle():
    global defaultColor
    print("I am a Hexagon")
    PencilButton.config(bg="#BFC9CA") #Pencil Button
    EraserButton.config(bg="#BFC9CA") #Eraser Button
    Pentagon_Button.config(bg="#BFC9CA") #Pentagon Button
    Rhombus_Button.config(bg="#BFC9CA") #Rhombus Button
    Equal_Triangle_Button.config(bg="#58D68D") #Equal Triangle Button
    Iso_Triangle_Button.config(bg="#BFC9CA") #IsoTriangle Button
    Right_Triangle_Button.config(bg="#BFC9CA") #Right Triangle Button
    Five_Star_Button.config(bg="#BFC9CA") #Five Star Button
    Rectangle_Button.config(bg="#BFC9CA") # Rectangle Button
    Circle_Button.config(bg="#BFC9CA") # Circle Button
    Oval_Button.config(bg="#BFC9CA") # Oval Button
    Line_Button.config(bg="#BFC9CA") # Line Button
    Curve_Line_Button.config(bg="#BFC9CA") # Curve Line Button
    HexButton.config(bg="#BFC9CA") # Hex Button
    BucketButton.config(bg="#BFC9CA") # Bucket Button
    PickerButton.config(bg="#BFC9CA") # Pick Button
    SaveButton.config(bg="#BFC9CA") # Save Button
    ClearButton.config(bg="#BFC9CA") # Clear Button
    NewButton.config(bg="#BFC9CA") # New Button
    mainCanvas["cursor"]=DOTBOX
    start_drawing_equal_triangle()


def start_drawing_equal_triangle():
    mainCanvas.unbind("<B1-Motion>") 
    mainCanvas.unbind("<ButtonRelease-1>") 
    mainCanvas.bind("<Button-1>", initiate_drawing_equal_triangle)
    mainCanvas.bind("<B1-Motion>", create_equilateral_triangle)
    mainCanvas.bind("<ButtonRelease-1>", stop_drawing_equal_triangle)

def initiate_drawing_equal_triangle(event):
    global x_start, y_start
    x_start, y_start = event.x, event.y

def create_equilateral_triangle(event):
    mainCanvas.delete("equal_triangle")
    x_end, y_end = mainCanvas.winfo_pointerx(), mainCanvas.winfo_pointery()
    width = abs(x_end - x_start)
    height = abs(y_end - y_start)
    size = min(width, height)  # Use the smaller dimension as the size for the equilateral triangl
    # Calculate the coordinates of the equilateral triangle vertices
    x1 = x_start
    y1 = y_start - (size / math.sqrt(3))
    x2 = x_start + (size / 2)
    y2 = y_start + (size / (2 * math.sqrt(3)))
    x3 = x_start - (size / 2)
    y3 = y_start + (size / (2 * math.sqrt(3)))

    mainCanvas.create_polygon(x1, y1, x2, y2, x3, y3, fill="", outline="black", tags="equal_triangle")

def stop_drawing_equal_triangle(event):
    print("I am unbinding")
    mainCanvas.unbind("<Button-1>")
    mainCanvas.unbind("<B1-Motion>")
    mainCanvas.unbind("<ButtonRelease-1>")


'''
Isosceles Triangle
'''
def useIsoTriangle():
    global defaultColor
    print("I am a Hexagon")
    PencilButton.config(bg="#BFC9CA") #Pencil Button
    EraserButton.config(bg="#BFC9CA") #Eraser Button
    Pentagon_Button.config(bg="#BFC9CA") #Pentagon Button
    Rhombus_Button.config(bg="#BFC9CA") #Rhombus Button
    Equal_Triangle_Button.config(bg="#BFC9CA") #Equal Triangle Button
    Iso_Triangle_Button.config(bg="#58D68D") #IsoTriangle Button
    Right_Triangle_Button.config(bg="#BFC9CA") #Right Triangle Button
    Five_Star_Button.config(bg="#BFC9CA") #Five Star Button
    Rectangle_Button.config(bg="#BFC9CA") # Rectangle Button
    Circle_Button.config(bg="#BFC9CA") # Circle Button
    Oval_Button.config(bg="#BFC9CA") # Oval Button
    Line_Button.config(bg="#BFC9CA") # Line Button
    Curve_Line_Button.config(bg="#BFC9CA") # Curve Line Button
    HexButton.config(bg="#BFC9CA") # Hex Button
    BucketButton.config(bg="#BFC9CA") # Bucket Button
    PickerButton.config(bg="#BFC9CA") # Pick Button
    SaveButton.config(bg="#BFC9CA") # Save Button
    ClearButton.config(bg="#BFC9CA") # Clear Button
    NewButton.config(bg="#BFC9CA") # New Button
    mainCanvas["cursor"]=DOTBOX
    start_drawing_Iso()


def start_drawing_Iso():
    mainCanvas.unbind("<B1-Motion>") 
    mainCanvas.unbind("<ButtonRelease-1>") 
    mainCanvas.bind("<Button-1>", initiate_drawing_Iso)
    mainCanvas.bind("<B1-Motion>", create_isosceles_triangle)
    mainCanvas.bind("<ButtonRelease-1>", stop_drawing_Iso)

def initiate_drawing_Iso(event):
    global x_start, y_start
    x_start, y_start = event.x, event.y

def create_isosceles_triangle(event):
    mainCanvas.delete("Iso_triangle")

    # x_start, y_start = event.x, event.y
    x_end, y_end = mainCanvas.winfo_pointerx(), mainCanvas.winfo_pointery()

    width = abs(x_end - x_start)
    height = abs(y_end - y_start)

    # Calculate the coordinates of the isosceles triangle vertices
    x1 = x_start
    y1 = y_start - height
    x2 = x_start + (width / 2)
    y2 = y_start
    x3 = x_start - (width / 2)
    y3 = y_start

    mainCanvas.create_polygon(x1, y1, x2, y2, x3, y3, fill="", outline="black", tags="Iso_triangle")

def stop_drawing_Iso(event):
    print("I am unbinding")
    mainCanvas.unbind("<Button-1>")
    mainCanvas.unbind("<B1-Motion>")
    mainCanvas.unbind("<ButtonRelease-1>")


'''
Right angled triangle
'''
def useRightTriangle():
    global defaultColor
    print("I am a Hexagon")
    PencilButton.config(bg="#BFC9CA") #Pencil Button
    EraserButton.config(bg="#BFC9CA") #Eraser Button
    Pentagon_Button.config(bg="#BFC9CA") #Pentagon Button
    Rhombus_Button.config(bg="#BFC9CA") #Rhombus Button
    Equal_Triangle_Button.config(bg="#BFC9CA") #Equal Triangle Button
    Iso_Triangle_Button.config(bg="#BFC9CA") #IsoTriangle Button
    Right_Triangle_Button.config(bg="#58D68D") #Right Triangle Button
    Five_Star_Button.config(bg="#BFC9CA") #Five Star Button
    Rectangle_Button.config(bg="#BFC9CA") # Rectangle Button
    Circle_Button.config(bg="#BFC9CA") # Circle Button
    Oval_Button.config(bg="#BFC9CA") # Oval Button
    Line_Button.config(bg="#BFC9CA") # Line Button
    Curve_Line_Button.config(bg="#BFC9CA") # Curve Line Button
    HexButton.config(bg="#BFC9CA") # Hex Button
    BucketButton.config(bg="#BFC9CA") # Bucket Button
    PickerButton.config(bg="#BFC9CA") # Pick Button
    SaveButton.config(bg="#BFC9CA") # Save Button
    ClearButton.config(bg="#BFC9CA") # Clear Button
    NewButton.config(bg="#BFC9CA") # New Button
    mainCanvas["cursor"]=DOTBOX
    start_drawing_Right()


def start_drawing_Right():
    mainCanvas.unbind("<B1-Motion>") 
    mainCanvas.unbind("<ButtonRelease-1>") 
    mainCanvas.bind("<Button-1>", initiate_drawing_right)
    mainCanvas.bind("<B1-Motion>", create_right_triangle)
    mainCanvas.bind("<ButtonRelease-1>", stop_drawing_right)

def initiate_drawing_right(event):
    global x_start, y_start
    x_start, y_start = event.x, event.y

def create_right_triangle(event):
    mainCanvas.delete("Right_triangle")

    # x_start, y_start = event.x, event.y
    x_end, y_end = mainCanvas.winfo_pointerx(), mainCanvas.winfo_pointery()

    width = abs(x_end - x_start)
    height = abs(y_end - y_start)

    # Calculate the coordinates of the right-angled triangle vertices
    x1 = x_start
    y1 = y_start
    x2 = x_start + width
    y2 = y_start
    x3 = x_start
    y3 = y_start + height

    mainCanvas.create_polygon(x1, y1, x2, y2, x3, y3, fill="", outline="black", tags="Right_triangle")

def stop_drawing_right(event):
    print("I am unbinding")
    mainCanvas.unbind("<Button-1>")
    mainCanvas.unbind("<B1-Motion>")
    mainCanvas.unbind("<ButtonRelease-1>")


'''
Five sided star 
'''

def use5Star():
    global defaultColor
    print("I am a Hexagon")
    PencilButton.config(bg="#BFC9CA") #Pencil Button
    EraserButton.config(bg="#BFC9CA") #Eraser Button
    Pentagon_Button.config(bg="#BFC9CA") #Pentagon Button
    Rhombus_Button.config(bg="#BFC9CA") #Rhombus Button
    Equal_Triangle_Button.config(bg="#BFC9CA") #Equal Triangle Button
    Iso_Triangle_Button.config(bg="#BFC9CA") #IsoTriangle Button
    Right_Triangle_Button.config(bg="#BFC9CA") #Right Triangle Button
    Five_Star_Button.config(bg="#58D68D") #Five Star Button
    Rectangle_Button.config(bg="#BFC9CA") # Rectangle Button
    Circle_Button.config(bg="#BFC9CA") # Circle Button
    Oval_Button.config(bg="#BFC9CA") # Oval Button
    Line_Button.config(bg="#BFC9CA") # Line Button
    Curve_Line_Button.config(bg="#BFC9CA") # Curve Line Button
    HexButton.config(bg="#BFC9CA") # Hex Button
    BucketButton.config(bg="#BFC9CA") # Bucket Button
    PickerButton.config(bg="#BFC9CA") # Pick Button
    SaveButton.config(bg="#BFC9CA") # Save Button
    ClearButton.config(bg="#BFC9CA") # Clear Button
    NewButton.config(bg="#BFC9CA") # New Button
    mainCanvas["cursor"]=DOTBOX
    start_drawing_5Star()


def start_drawing_5Star():
    mainCanvas.unbind("<B1-Motion>") 
    mainCanvas.unbind("<ButtonRelease-1>") 
    mainCanvas.bind("<Button-1>", initiate_drawing_5Star)
    mainCanvas.bind("<B1-Motion>", create_five_sided_5star)
    mainCanvas.bind("<ButtonRelease-1>", stop_drawing_5Star)



def initiate_drawing_5Star(event):
    global x_start, y_start
    x_start, y_start = event.x, event.y

def create_five_sided_5star(event):
    mainCanvas.delete("star")

    # x_start, y_start = event.x, event.y
    x_end, y_end = mainCanvas.winfo_pointerx(), mainCanvas.winfo_pointery()

    width = abs(x_end - x_start)
    height = abs(y_end - y_start)
    size = min(width, height)  # Use the smaller dimension as the size for the star

    radius_outer = size / 2
    radius_inner = radius_outer / 2

    points = []
    angle = -math.pi / 2  # Start from the top vertex
    angle_increment = 2 * math.pi / 5  # Angle increment between each point

    for _ in range(5):
        x_outer = x_start + radius_outer * math.cos(angle)
        y_outer = y_start + radius_outer * math.sin(angle)
        points.extend([x_outer, y_outer])
        angle += angle_increment

        x_inner = x_start + radius_inner * math.cos(angle)
        y_inner = y_start + radius_inner * math.sin(angle)
        points.extend([x_inner, y_inner])
        angle += angle_increment

    mainCanvas.create_polygon(points, fill="", outline="black", tags="star")


def stop_drawing_5Star(event):
    print("I am unbinding")
    mainCanvas.unbind("<Button-1>")
    mainCanvas.unbind("<B1-Motion>")
    mainCanvas.unbind("<ButtonRelease-1>")


'''
4 sided star

'''

def useRectangle():
    global defaultColor
    print("I am a Hexagon")
    PencilButton.config(bg="#BFC9CA") #Pencil Button
    EraserButton.config(bg="#BFC9CA") #Eraser Button
    Pentagon_Button.config(bg="#BFC9CA") #Pentagon Button
    Rhombus_Button.config(bg="#BFC9CA") #Rhombus Button
    Equal_Triangle_Button.config(bg="#BFC9CA") #Equal Triangle Button
    Iso_Triangle_Button.config(bg="#BFC9CA") #IsoTriangle Button
    Right_Triangle_Button.config(bg="#BFC9CA") #Right Triangle Button
    Five_Star_Button.config(bg="#BFC9CA") #Five Star Button
    Rectangle_Button.config(bg="#58D68D") # Rectangle Button
    Circle_Button.config(bg="#BFC9CA") # Circle Button
    Oval_Button.config(bg="#BFC9CA") # Oval Button
    Line_Button.config(bg="#BFC9CA") # Line Button
    Curve_Line_Button.config(bg="#BFC9CA") # Curve Line Button
    HexButton.config(bg="#BFC9CA") # Hex Button
    BucketButton.config(bg="#BFC9CA") # Bucket Button
    PickerButton.config(bg="#BFC9CA") # Pick Button
    SaveButton.config(bg="#BFC9CA") # Save Button
    ClearButton.config(bg="#BFC9CA") # Clear Button
    NewButton.config(bg="#BFC9CA") # New Button
    mainCanvas["cursor"]=DOTBOX
    start_drawing_Rectangle()


def start_drawing_Rectangle():
    mainCanvas.unbind("<B1-Motion>") 
    mainCanvas.unbind("<ButtonRelease-1>") 
    mainCanvas.bind("<Button-1>", initiate_drawing_Rectangle)
    mainCanvas.bind("<B1-Motion>", create_Rectangle)
    mainCanvas.bind("<ButtonRelease-1>", stop_drawing_Rectangle)




def initiate_drawing_Rectangle(event):
    global x_start, y_start
    x_start, y_start = event.x, event.y

def create_Rectangle(event):
    mainCanvas.delete("rectangle")

    # x_start, y_start = event.x, event.y
    x_end, y_end = mainCanvas.winfo_pointerx(), mainCanvas.winfo_pointery()

    width = abs(x_end - x_start)
    height = abs(y_end - y_start)

    x1 = min(x_start, x_end)
    y1 = min(y_start, y_end)
    x2 = x1 + width
    y2 = y1 + height

    mainCanvas.create_rectangle(x1, y1, x2, y2, fill="", outline="black", tags="rectangle")



def stop_drawing_Rectangle(event):
    print("I am unbinding")
    mainCanvas.unbind("<Button-1>")
    mainCanvas.unbind("<B1-Motion>")
    mainCanvas.unbind("<ButtonRelease-1>")

'''
Circle 
'''

def useCircle():
    global defaultColor
    print("I am a Hexagon")
    PencilButton.config(bg="#BFC9CA") #Pencil Button
    EraserButton.config(bg="#BFC9CA") #Eraser Button
    Pentagon_Button.config(bg="#BFC9CA") #Pentagon Button
    Rhombus_Button.config(bg="#BFC9CA") #Rhombus Button
    Equal_Triangle_Button.config(bg="#BFC9CA") #Equal Triangle Button
    Iso_Triangle_Button.config(bg="#BFC9CA") #IsoTriangle Button
    Right_Triangle_Button.config(bg="#BFC9CA") #Right Triangle Button
    Five_Star_Button.config(bg="#BFC9CA") #Five Star Button
    Rectangle_Button.config(bg="#BFC9CA") # Rectangle Button
    Circle_Button.config(bg="#58D68D") # Circle Button
    Oval_Button.config(bg="#BFC9CA") # Oval Button
    Line_Button.config(bg="#BFC9CA") # Line Button
    Curve_Line_Button.config(bg="#BFC9CA") # Curve Line Button
    HexButton.config(bg="#BFC9CA") # Hex Button
    BucketButton.config(bg="#BFC9CA") # Bucket Button
    PickerButton.config(bg="#BFC9CA") # Pick Button
    SaveButton.config(bg="#BFC9CA") # Save Button
    ClearButton.config(bg="#BFC9CA") # Clear Button
    NewButton.config(bg="#BFC9CA") # New Button
    mainCanvas["cursor"]=DOTBOX
    start_drawing_circle()


def start_drawing_circle():
    mainCanvas.unbind("<B1-Motion>") 
    mainCanvas.unbind("<ButtonRelease-1>") 
    mainCanvas.bind("<Button-1>", initiate_drawing_circle)
    mainCanvas.bind("<B1-Motion>", create_circle)
    mainCanvas.bind("<ButtonRelease-1>", stop_drawing_circle)




def initiate_drawing_circle(event):
    global x_start, y_start
    x_start, y_start = event.x, event.y

def create_circle(event):
    mainCanvas.delete("Circle")

    x_end, y_end = mainCanvas.winfo_pointerx(), mainCanvas.winfo_pointery()

    radius = math.sqrt((x_end - x_start) ** 2 + (y_end - y_start) ** 2)
    x1 = x_start - radius
    y1 = y_start - radius
    x2 = x_start + radius
    y2 = y_start + radius

    mainCanvas.create_oval(x1, y1, x2, y2, fill="", outline="black", tags="Circle")

def stop_drawing_circle(event):
    print("I am unbinding")
    mainCanvas.unbind("<Button-1>")
    mainCanvas.unbind("<B1-Motion>")
    mainCanvas.unbind("<ButtonRelease-1>")

'''
Oval
'''

def useOval():
    global defaultColor
    print("I am a Hexagon")
    PencilButton.config(bg="#BFC9CA") #Pencil Button
    EraserButton.config(bg="#BFC9CA") #Eraser Button
    Pentagon_Button.config(bg="#BFC9CA") #Pentagon Button
    Rhombus_Button.config(bg="#BFC9CA") #Rhombus Button
    Equal_Triangle_Button.config(bg="#BFC9CA") #Equal Triangle Button
    Iso_Triangle_Button.config(bg="#BFC9CA") #IsoTriangle Button
    Right_Triangle_Button.config(bg="#BFC9CA") #Right Triangle Button
    Five_Star_Button.config(bg="#BFC9CA") #Five Star Button
    Rectangle_Button.config(bg="#BFC9CA") # Rectangle Button
    Circle_Button.config(bg="#BFC9CA") # Circle Button
    Oval_Button.config(bg="#58D68D") # Oval Button
    Line_Button.config(bg="#BFC9CA") # Line Button
    Curve_Line_Button.config(bg="#BFC9CA") # Curve Line Button
    HexButton.config(bg="#BFC9CA") # Hex Button
    BucketButton.config(bg="#BFC9CA") # Bucket Button
    PickerButton.config(bg="#BFC9CA") # Pick Button
    SaveButton.config(bg="#BFC9CA") # Save Button
    ClearButton.config(bg="#BFC9CA") # Clear Button
    NewButton.config(bg="#BFC9CA") # New Button
    mainCanvas["cursor"]=DOTBOX
    start_drawing_Oval()


def start_drawing_Oval():
    mainCanvas.unbind("<B1-Motion>") 
    mainCanvas.unbind("<ButtonRelease-1>") 
    mainCanvas.bind("<Button-1>", initiate_drawing_Oval)
    mainCanvas.bind("<B1-Motion>", create_Oval)
    mainCanvas.bind("<ButtonRelease-1>", stop_drawing_Oval)


def initiate_drawing_Oval(event):
    global x_start, y_start
    x_start, y_start = event.x, event.y

def create_Oval(event):
    mainCanvas.delete("oval")

    # x_start, y_start = event.x, event.y
    x_end, y_end = mainCanvas.winfo_pointerx(), mainCanvas.winfo_pointery()

    x1 = min(x_start, x_end)
    y1 = min(y_start, y_end)
    x2 = max(x_start, x_end)
    y2 = max(y_start, y_end)

    mainCanvas.create_oval(x1, y1, x2, y2, fill="", outline="black", tags="oval")


def stop_drawing_Oval(event):
    print("I am unbinding")
    mainCanvas.unbind("<Button-1>")
    mainCanvas.unbind("<B1-Motion>")
    mainCanvas.unbind("<ButtonRelease-1>")




'''
Line
'''



def useLine():
    global defaultColor
    print("I am a Hexagon")
    PencilButton.config(bg="#BFC9CA") #Pencil Button
    EraserButton.config(bg="#BFC9CA") #Eraser Button
    Pentagon_Button.config(bg="#BFC9CA") #Pentagon Button
    Rhombus_Button.config(bg="#BFC9CA") #Rhombus Button
    Equal_Triangle_Button.config(bg="#BFC9CA") #Equal Triangle Button
    Iso_Triangle_Button.config(bg="#BFC9CA") #IsoTriangle Button
    Right_Triangle_Button.config(bg="#BFC9CA") #Right Triangle Button
    Five_Star_Button.config(bg="#BFC9CA") #Five Star Button
    Rectangle_Button.config(bg="#BFC9CA") # Rectangle Button
    Circle_Button.config(bg="#BFC9CA") # Circle Button
    Oval_Button.config(bg="#BFC9CA") # Oval Button
    Line_Button.config(bg="#58D68D") # Line Button
    Curve_Line_Button.config(bg="#BFC9CA") # Curve Line Button
    HexButton.config(bg="#BFC9CA") # Hex Button
    BucketButton.config(bg="#BFC9CA") # Bucket Button
    PickerButton.config(bg="#BFC9CA") # Pick Button
    SaveButton.config(bg="#BFC9CA") # Save Button
    ClearButton.config(bg="#BFC9CA") # Clear Button
    NewButton.config(bg="#BFC9CA") # New Button
    mainCanvas["cursor"]=DOTBOX
    start_drawing_line()


def start_drawing_line():
    mainCanvas.unbind("<B1-Motion>") 
    mainCanvas.unbind("<ButtonRelease-1>") 
    mainCanvas.bind("<Button-1>", initiate_drawing_line)
    mainCanvas.bind("<B1-Motion>", create_line)
    mainCanvas.bind("<ButtonRelease-1>", stop_drawing_line)


def initiate_drawing_line(event):
    global x_start, y_start
    x_start, y_start = event.x, event.y

def create_line(event):
    mainCanvas.delete("Line")

    # x_start, y_start = event.x, event.y
    x_end, y_end = mainCanvas.winfo_pointerx(), mainCanvas.winfo_pointery()

    mainCanvas.create_line(x_start, y_start, x_end, y_end, fill="black", tags="Line")



def stop_drawing_line(event):
    print("I am unbinding")
    mainCanvas.unbind("<Button-1>")
    mainCanvas.unbind("<B1-Motion>")
    mainCanvas.unbind("<ButtonRelease-1>")

'''
Curve line
'''


def useCurveLine():
    global defaultColor
    print("I am a Hexagon")
    PencilButton.config(bg="#BFC9CA") #Pencil Button
    EraserButton.config(bg="#BFC9CA") #Eraser Button
    Pentagon_Button.config(bg="#BFC9CA") #Pentagon Button
    Rhombus_Button.config(bg="#BFC9CA") #Rhombus Button
    Equal_Triangle_Button.config(bg="#BFC9CA") #Equal Triangle Button
    Iso_Triangle_Button.config(bg="#BFC9CA") #IsoTriangle Button
    Right_Triangle_Button.config(bg="#BFC9CA") #Right Triangle Button
    Five_Star_Button.config(bg="#BFC9CA") #Five Star Button
    Rectangle_Button.config(bg="#BFC9CA") # Rectangle Button
    Circle_Button.config(bg="#BFC9CA") # Circle Button
    Oval_Button.config(bg="#BFC9CA") # Oval Button
    Line_Button.config(bg="#BFC9CA") # Line Button
    Curve_Line_Button.config(bg="#58D68D") # Curve Line Button
    HexButton.config(bg="#BFC9CA") # Hex Button
    BucketButton.config(bg="#BFC9CA") # Bucket Button
    PickerButton.config(bg="#BFC9CA") # Pick Button
    SaveButton.config(bg="#BFC9CA") # Save Button
    ClearButton.config(bg="#BFC9CA") # Clear Button
    NewButton.config(bg="#BFC9CA") # New Button
    mainCanvas["cursor"]=DOTBOX
    start_drawing_Curve_line()


def start_drawing_Curve_line():
    mainCanvas.unbind("<B1-Motion>") 
    mainCanvas.unbind("<ButtonRelease-1>") 
    mainCanvas.bind("<Button-1>", initiate_drawing_Curve_line)
    mainCanvas.bind("<B1-Motion>", create_Curve_line)
    mainCanvas.bind("<ButtonRelease-1>", stop_drawing_Curve_line)


def initiate_drawing_Curve_line(event):
    global x_start, y_start
    x_start, y_start = event.x, event.y

def create_Curve_line(event):
    mainCanvas.delete("Curve")

    # x_start, y_start = event.x, event.y
    x_end, y_end = mainCanvas.winfo_pointerx(), mainCanvas.winfo_pointery()

    control_x = (x_start + x_end) / 2
    control_y = y_start - 50

    mainCanvas.create_line(x_start, y_start, control_x, control_y, x_end, y_end, smooth=True, fill="black", tags="Curve")




def stop_drawing_Curve_line(event):
    print("I am unbinding")
    mainCanvas.unbind("<Button-1>")
    mainCanvas.unbind("<B1-Motion>")
    mainCanvas.unbind("<ButtonRelease-1>")




'''
Shapes below
'''
Hexagon_Img=Image.open("Shapes/Hexagon.png")
Hexagon_Img=Hexagon_Img.resize((30,30))
Hexagon = ImageTk.PhotoImage(Hexagon_Img)
HexButton=Button(ShapesFrames,image=Hexagon ,height=30,width=30,bg="#BFC9CA",command=useHexagon)
HexButton.grid(row=0,column=0)

Pentagon_Img=Image.open("Shapes/Pentagon.png")
Pentagon_Img=Pentagon_Img.resize((30,30))
Pentagon = ImageTk.PhotoImage(Pentagon_Img)
Pentagon_Button=Button(ShapesFrames,image=Pentagon ,height=30,width=30,bg="#BFC9CA",command=usePentagon)
Pentagon_Button.grid(row=1,column=0)

Rhombus_Img=Image.open("Shapes/Rhombus.png")
Rhombus_Img=Rhombus_Img.resize((30,30))
Rhombus = ImageTk.PhotoImage(Rhombus_Img)
Rhombus_Button=Button(ShapesFrames,image=Rhombus ,height=30,width=30,bg="#BFC9CA",command=useRhombus)
Rhombus_Button.grid(row=0,column=1)

Equal_Tri_Img=Image.open("Shapes/Equal_Tri.png")
Equal_Tri_Img=Equal_Tri_Img.resize((30,30))
Equal_Tri = ImageTk.PhotoImage(Equal_Tri_Img)
Equal_Triangle_Button=Button(ShapesFrames,image=Equal_Tri ,height=30,width=30,bg="#BFC9CA",command=useEqualTriangle)
Equal_Triangle_Button.grid(row=1,column=1)

Iso_Tri_Img=Image.open("Shapes/Iso_Tri.png")
Iso_Tri_Img=Iso_Tri_Img.resize((30,30))
Iso_Tri = ImageTk.PhotoImage(Iso_Tri_Img)
Iso_Triangle_Button=Button(ShapesFrames,image=Iso_Tri ,height=30,width=30,bg="#BFC9CA",command=useIsoTriangle)
Iso_Triangle_Button.grid(row=0,column=2)

Right_Img=Image.open("Shapes/Right.png")
Right_Img=Right_Img.resize((30,30))
Right = ImageTk.PhotoImage(Right_Img)
Right_Triangle_Button=Button(ShapesFrames,image=Right ,height=30,width=30,bg="#BFC9CA",command=useRightTriangle)
Right_Triangle_Button.grid(row=1,column=2)

Star_Img=Image.open("Shapes/Star.png")
Star_Img=Star_Img.resize((30,30))
Star = ImageTk.PhotoImage(Star_Img)
Five_Star_Button=Button(ShapesFrames,image=Star ,height=30,width=30,bg="#BFC9CA",command=use5Star)
Five_Star_Button.grid(row=0,column=3)

Rectangle_Img=Image.open("Shapes/Rectangle.png")
Rectangle_Img=Rectangle_Img.resize((30,30))
Rectangle = ImageTk.PhotoImage(Rectangle_Img)
Rectangle_Button=Button(ShapesFrames,image=Rectangle ,height=30,width=30,bg="#BFC9CA",command=useRectangle)
Rectangle_Button.grid(row=1,column=3)

Circle_Img=Image.open("Shapes/Circle.png")
Circle_Img=Circle_Img.resize((30,30))
Circle = ImageTk.PhotoImage(Circle_Img)
Circle_Button=Button(ShapesFrames,image=Circle ,height=30,width=30,bg="#BFC9CA",command=useCircle)
Circle_Button.grid(row=0,column=4)

Oval_Img=Image.open("Shapes/Oval.png")
Oval_Img=Oval_Img.resize((30,30))
Oval = ImageTk.PhotoImage(Oval_Img)
Oval_Button=Button(ShapesFrames,image=Oval ,height=30,width=30,bg="#BFC9CA",command=useOval)
Oval_Button.grid(row=1,column=4)

Line_Img=Image.open("Shapes/Line.png")
Line_Img=Line_Img.resize((30,30))
Line = ImageTk.PhotoImage(Line_Img)
Line_Button=Button(ShapesFrames,image=Line ,height=30,width=30,bg="#BFC9CA",command=useLine)
Line_Button.grid(row=0,column=5)

Curve_Line_Img=Image.open("Shapes/Curve_Line.png")
Curve_Line_Img=Curve_Line_Img.resize((30,30))
Curve_Line = ImageTk.PhotoImage(Curve_Line_Img)
Curve_Line_Button=Button(ShapesFrames,image=Curve_Line ,height=30,width=30,bg="#BFC9CA",command=useCurveLine)
Curve_Line_Button.grid(row=1,column=5)

Heart_Img=Image.open("Shapes/heart.png")
Heart_Img=Heart_Img.resize((30,30))
Heart = ImageTk.PhotoImage(Heart_Img)
Heart_Button=Button(ShapesFrames,image=Heart ,height=30,width=30,bg="#BFC9CA",command=useHeart)
Heart_Button.grid(row=0,column=6)

Light_Img=Image.open("Shapes/cloud.png")
Light_Img=Light_Img.resize((30,30))
Light = ImageTk.PhotoImage(Light_Img)
Light_Button=Button(ShapesFrames,image=Light ,height=30,width=30,bg="#BFC9CA",command=useCloud)
Light_Button.grid(row=1,column=6)

FP_star_Img=Image.open("Shapes/fps.png")
FP_star_Img=FP_star_Img.resize((30,30))
FP_star = ImageTk.PhotoImage(FP_star_Img)
FP_star_Button=Button(ShapesFrames,image=FP_star ,height=30,width=30,bg="#BFC9CA",command=useFPS)
FP_star_Button.grid(row=0,column=7)

Alpha_Img=Image.open("Shapes/Al;pha.png")
Alpha_Img=Alpha_Img.resize((30,30))
Alpha = ImageTk.PhotoImage(Alpha_Img)
Alpha_Button=Button(ShapesFrames,image=Alpha ,height=30,width=30,bg="#BFC9CA",command=start_typing)
Alpha_Button.grid(row=1,column=7)

# shapeLabel=Label(ShapesFrames,text="SHapes")
# shapeLabel.grid(row=2,column=5)

'''
Colors below
'''
# Color Frames
ColorPlate=Frame(Plate,height=110,width=110,relief=SUNKEN,borderwidth=3)
ColorPlate.grid(row=0,column=5)


# Colors Selection button
MultipleColor=Image.open("Colors/Multiple_Clr.png")
MultipleColor=MultipleColor.resize((50,50))
MultipleClr = ImageTk.PhotoImage(MultipleColor)
ColorBox=Button(MultipleColorPlate,image=MultipleClr,height=50,width=50,bg="#BFC9CA",command=selectColor)
ColorBox.grid(row=0)

# Blue Color
def useBlue():
    defaultColor.set("#004AAD")
BlueColor=Image.open("Colors/Blue_Clr.png")
BlueColor=BlueColor.resize((25,25))
BlueClr = ImageTk.PhotoImage(BlueColor)
ColorBox=Button(ColorPlate,image=BlueClr,height=25,width=25,bg="#BFC9CA",command=useBlue)
ColorBox.grid(row=0,column=0)

# Red Color
def useRed():
    defaultColor.set("#FF3131")
RedColor=Image.open("Colors/Red_Clr.png")
RedColor=RedColor.resize((25,25))
RedClr = ImageTk.PhotoImage(RedColor)
ColorBox=Button(ColorPlate,image=RedClr,height=25,width=25,bg="#BFC9CA",command=useRed)
ColorBox.grid(row=1,column=0)

# Yellow Color
def useYellow():
    defaultColor.set("#FFDE59")
YellowColor=Image.open("Colors/Yellow_Clr.png")
YellowColor=YellowColor.resize((25,25))
YellowClr = ImageTk.PhotoImage(YellowColor)
ColorBox=Button(ColorPlate,image=YellowClr,height=25,width=25,bg="#BFC9CA",command=useYellow)
ColorBox.grid(row=0,column=1)

# Green Color
def useGreen():
    defaultColor.set("#00BF63")
GreenColor=Image.open("Colors/Green_Clr.png")
GreenColor=GreenColor.resize((25,25))
GreenClr = ImageTk.PhotoImage(GreenColor)
ColorBox=Button(ColorPlate,image=GreenClr,height=25,width=25,bg="#BFC9CA",command=useGreen)
ColorBox.grid(row=1,column=1)

# Purple Color
def usePurple():
    defaultColor.set("#CB6CE6")
PurpleColor=Image.open("Colors/Purple_Clr.png")
PurpleColor=PurpleColor.resize((25,25))
PurpleClr = ImageTk.PhotoImage(PurpleColor)
ColorBox=Button(ColorPlate,image=PurpleClr,height=25,width=25,bg="#BFC9CA",command=usePurple)
ColorBox.grid(row=1,column=2)

# Parrot Color
def useParrot():
    defaultColor.set("#007B01")
ParrotColor=Image.open("Colors/Parrot_Clr.png")
ParrotColor=ParrotColor.resize((25,25))
ParrotClr = ImageTk.PhotoImage(ParrotColor)
ColorBox=Button(ColorPlate,image=ParrotClr,height=25,width=25,bg="#BFC9CA",command=useParrot)
ColorBox.grid(row=0,column=2)

# Lime Color
def useLime():
    defaultColor.set("#ADFF00")
LimeColor=Image.open("Colors/Lime_Clr.png")
LimeColor=LimeColor.resize((25,25))
LimeClr = ImageTk.PhotoImage(LimeColor)
ColorBox=Button(ColorPlate,image=LimeClr,height=25,width=25,bg="#BFC9CA",command=useLime)
ColorBox.grid(row=0,column=3)

# Orange Color
def useOrange():
    defaultColor.set("#F16B17")
OrangeColor=Image.open("Colors/Orange_Clr.png")
OrangeColor=OrangeColor.resize((25,25))
OrangeClr = ImageTk.PhotoImage(OrangeColor)
ColorBox=Button(ColorPlate,image=OrangeClr,height=25,width=25,bg="#BFC9CA",command=useOrange)
ColorBox.grid(row=1,column=3)

# Aqua Color
def useAqua():
    defaultColor.set("#00E8FF")
AquaColor=Image.open("Colors/Aqua_Clr.png")
AquaColor=AquaColor.resize((25,25))
AquaClr = ImageTk.PhotoImage(AquaColor)
ColorBox=Button(ColorPlate,image=AquaClr,height=25,width=25,bg="#BFC9CA",command=useAqua)
ColorBox.grid(row=0,column=4)

# Pink Color
def usePink():
    defaultColor.set("#FF0082")
PinkColor=Image.open("Colors/Pink_Clr.png")
PinkColor=PinkColor.resize((25,25))
PinkClr = ImageTk.PhotoImage(PinkColor)
ColorBox=Button(ColorPlate,image=PinkClr,height=25,width=25,bg="#BFC9CA",command=usePink)
ColorBox.grid(row=1,column=4)

# Black Color
def useBlack():
    defaultColor.set("#000000")
BlackColor=Image.open("Colors/Black_Clr.png")
BlackColor=BlackColor.resize((25,25))
BlackClr = ImageTk.PhotoImage(BlackColor)
ColorBox=Button(ColorPlate,image=BlackClr,height=25,width=25,bg="#BFC9CA",command=useBlack)
ColorBox.grid(row=1,column=5)

# Grey Color
def useGrey():
    defaultColor.set("#727272")
GreyColor=Image.open("Colors/Grey_Clr.png")
GreyColor=GreyColor.resize((25,25))
GreyClr = ImageTk.PhotoImage(GreyColor)
ColorBox=Button(ColorPlate,image=GreyClr,height=25,width=25,bg="#BFC9CA",command=useGrey)
ColorBox.grid(row=0,column=5)



# Default colors
defaultColor=StringVar()
defaultColor.set("black")

def useSelection():
    mainCanvas.bind("<ButtonPress-1>", start_selection)
    mainCanvas.bind("<B1-Motion>", update_selection)
    mainCanvas.bind("<ButtonRelease-1>", end_selection)

def start_selection(event):
    global start_x, start_y
    start_x = event.x
    start_y = event.y

def update_selection(event):
    mainCanvas.delete("selection")  # Remove previous selection rectangle if exists
    print("Updating selection")
    current_x = event.x
    current_y = event.y
    mainCanvas.create_rectangle(start_x, start_y, current_x, current_y, outline="red", tags="selection")

def end_selection(event):
    mainCanvas.delete("selection")  # Remove selection rectangle

    # Get the selected region coordinates
    x1 = min(start_x, event.x)
    y1 = min(start_y, event.y)
    x2 = max(start_x, event.x)
    y2 = max(start_y, event.y)

    # Create a movable selection rectangle
    selection_rect = mainCanvas.create_rectangle(x1, y1, x2, y2, outline="red", tags="selection")

    # Bind mouse events for moving the selection
    mainCanvas.bind("<ButtonPress-1>", lambda event: start_move(event, selection_rect))
    mainCanvas.bind("<B1-Motion>", lambda event: move_selection(event, selection_rect))

def start_move(event, selection_rect):
    global prev_x, prev_y
    prev_x = event.x
    prev_y = event.y

def move_selection(event, selection_rect):
    global prev_x, prev_y
    dx = event.x - prev_x
    dy = event.y - prev_y

    # Move the selection rectangle
    mainCanvas.move(selection_rect, dx, dy)
    prev_x = event.x
    prev_y = event.y

    # Move the drawn objects within the selected region
    selected_objects = mainCanvas.find_enclosed(start_x, start_y, start_x + dx, start_y + dy)
    for obj in selected_objects:
        mainCanvas.move(obj, dx, dy)

    # Update the start_x and start_y for the next move
    start_x += dx
    start_y += dy









def magnify(event):
    magnification_factor = 1.1 
    x = mainCanvas.canvasx(event.x)
    y = mainCanvas.canvasy(event.y)

    if event.delta > 0:
        # Zoom in
        mainCanvas.scale("all", x, y, magnification_factor, magnification_factor)
    else:
        # Zoom out
        mainCanvas.scale("all", x, y, 1/magnification_factor, 1/magnification_factor)





def handle_fill_color(event):
    global fillMode
    print(fillMode)
    if fillMode:
        x, y = event.x, event.y
        closest_item = mainCanvas.find_closest(x, y)
        print(closest_item)
        if closest_item:
            print("hi")
            target_color = mainCanvas.itemconfig(closest_item, "fill")[4]
            fill_color = defaultColor.get()
            if target_color != fill_color:
                pixel_stack = [(x, y)]
                while pixel_stack:
                    new_x, new_y = pixel_stack.pop()
                    current_item = mainCanvas.find_closest(new_x, new_y)
                    current_color = mainCanvas.itemconfig(current_item, "fill")[4]
                    if current_color == target_color:
                        mainCanvas.itemconfig(current_item, fill=fill_color, outline=defaultColor.get())
                        if new_x > 0:
                            pixel_stack.append((new_x - 1, new_y))
                        if new_x < mainCanvas.winfo_width() - 1:
                            pixel_stack.append((new_x + 1, new_y))
                        if new_y > 0:
                            pixel_stack.append((new_x, new_y - 1))
                        if new_y < mainCanvas.winfo_height() - 1:
                            pixel_stack.append((new_x, new_y + 1))


    
'''
Tools Below
'''

def useBucket():
    PencilButton.config(bg="#BFC9CA") #Pencil Button
    EraserButton.config(bg="#BFC9CA") #Eraser Button
    Pentagon_Button.config(bg="#BFC9CA") #Pentagon Button
    Rhombus_Button.config(bg="#BFC9CA") #Rhombus Button
    Equal_Triangle_Button.config(bg="#BFC9CA") #Equal Triangle Button
    Iso_Triangle_Button.config(bg="#BFC9CA") #IsoTriangle Button
    Right_Triangle_Button.config(bg="#BFC9CA") #Right Triangle Button
    Five_Star_Button.config(bg="#BFC9CA") #Five Star Button
    Rectangle_Button.config(bg="#BFC9CA") # Rectangle Button
    Circle_Button.config(bg="#BFC9CA") # Circle Button
    Oval_Button.config(bg="#BFC9CA") # Oval Button
    Line_Button.config(bg="#BFC9CA") # Line Button
    Curve_Line_Button.config(bg="#BFC9CA") # Curve Line Button
    HexButton.config(bg="#BFC9CA") # Hex Button
    BucketButton.config(bg="#58D68D") # Bucket Button
    PickerButton.config(bg="#BFC9CA") # Pick Button
    SaveButton.config(bg="#BFC9CA") # Save Button
    ClearButton.config(bg="#BFC9CA") # Clear Button
    NewButton.config(bg="#BFC9CA") # New Button
    global fillMode
    fillMode=True
    mainCanvas.bind("<Button-1>", handle_fill_color)
   #root.bind("<Button-1>", handle_fill_color)

# Bucket button
Bucket_img=Image.open("Tools/Bucket.png")
Bucket_img=Bucket_img.resize((30,30))
Bucket_photo = ImageTk.PhotoImage(Bucket_img)
BucketButton=Button(Tools,image=Bucket_photo,height=30,width=30,bg="#BFC9CA",command=useBucket)
BucketButton.grid(row=0,column=1)


# Pencil Button
pencil_img=Image.open("Tools/pencil.png")
pencil_img=pencil_img.resize((30,30))
pencil_photo = ImageTk.PhotoImage(pencil_img)
PencilButton=Button(Tools,image=pencil_photo,height=30,width=30,bg="#BFC9CA",command=usePencil )
PencilButton.grid(row=0,column=0)

# Eraser button
eraser_img=Image.open("Tools/eraser.png")
eraser_img=eraser_img.resize((30,30))
eraser_photo = ImageTk.PhotoImage(eraser_img)
EraserButton=Button(Tools,image=eraser_photo,height=30,width=30,bg="#BFC9CA",command=useEraser)
EraserButton.grid(row=1,column=0)

# Picker button
Picker_img=Image.open("Tools/Picker.png")
Picker_img=Picker_img.resize((30,30))
Picker_photo = ImageTk.PhotoImage(Picker_img)
PickerButton=Button(Tools,image=Picker_photo,height=30,width=30,bg="#BFC9CA",command=usePick)
PickerButton.grid(row=1,column=1)

# Magnifier button
Magnifier_img=Image.open("Tools/Mag.png")
Magnifier_img=Magnifier_img.resize((30,30))
Magnifier_photo = ImageTk.PhotoImage(Magnifier_img)
MagnifierButton=Button(Tools,image=Magnifier_photo,height=30,width=30,bg="#BFC9CA",command=useMagnifier)
MagnifierButton.grid(row=0,column=2)

# Select Button
Select=Image.open("Tools/Select.png")
Select=Select.resize((30,30))
SelectImg = ImageTk.PhotoImage(Select)
SelectButton=Button(Tools,image=SelectImg,height=30,width=30,bg="#BFC9CA",command=useSelection)
SelectButton.grid(row=1,column=2)


'''
Save etc
'''

# Save Button
Save=Image.open("Tools/Save.png")
Save=Save.resize((50,50))
saveImg = ImageTk.PhotoImage(Save)
SaveButton=Button(SavingFrame,image=saveImg,height=50,width=50,bg="#BFC9CA",command=saveImage)
SaveButton.grid(row=0,column=0)
# Clear Button
Clear=Image.open("Tools/Clear.png")
Clear=Clear.resize((50,50))
ClearImg = ImageTk.PhotoImage(Clear)
ClearButton=Button(SavingFrame,image=ClearImg,height=50,width=50,bg="#BFC9CA",command=clearCanvas)
ClearButton.grid(row=0,column=1)
# Clear Button
New=Image.open("Tools/New.png")
New=New.resize((50,50))
NewImg = ImageTk.PhotoImage(New)
NewButton=Button(SavingFrame,image=NewImg,height=50,width=50,bg="#BFC9CA",command=newCanvas)
NewButton.grid(row=0,column=2)

Load=Image.open("Tools/Load.png")
Load=Load.resize((50,50))
LoadImg = ImageTk.PhotoImage(Load)
LoadButton=Button(SavingFrame,image=LoadImg,height=50,width=50,bg="#BFC9CA",command=load_image)
LoadButton.grid(row=0,column=3)



'''
Strokes below
'''

# Label for stroke
Pen=Image.open("Tools/Stroke.png")
Pen=Pen.resize((50,50))
PenImg = ImageTk.PhotoImage(Pen)
PenLabel=Label(StrokeSize,image=PenImg,height=50,width=50)
PenLabel.grid(row=0,column=0)

# Label for stroke
StrokeLabel=Label(StrokeSize,text="Size",width=10 )
StrokeLabel.grid(row=2,column=0)

# Strokes parameters
stroke_size=IntVar()
listItems=[1,2,3,4,5,6,7,8,9,10]
StrokeList=OptionMenu(StrokeSize,stroke_size,*listItems)
StrokeList.grid(row=1,column=0)





# Label for stroke
Polygonal=Image.open("Tools/Polygon.png")
Polygonal=Polygonal.resize((50,50))
PolygonalImg = ImageTk.PhotoImage(Polygonal)
PolygonalLabel=Label(Polygons,image=PolygonalImg,height=50,width=50)
PolygonalLabel.grid(row=0,column=0)

# Label for stroke
# StrokeLabel=Label(Polygons,text="Size",width=10 )
# StrokeLabel.grid(row=2,column=0)



# Strokes parameters
NoOfPolygons=IntVar()
Nums=[4,5,6,7,8,9,10,11]
PollList=OptionMenu(Polygons,NoOfPolygons,*Nums)
PollList.grid(row=1,column=0)

Poll=Button(Polygons,text="Draw",width=10,command=usePolygon)
Poll.grid(row=2,column=0)








'''
Canvas Configuration 
| |             | |
| |             | |
| |             | |
 V               V
'''

canvas=Frame(root,height=640-110,width=1280,bg="yellow")
canvas.grid(row=1,column=0)

mainCanvas=Canvas(canvas,height=640-110,width=1280,bg="white",cursor="heart")
mainCanvas.grid(row=0,column=0)


'''
Drawings Configuration

'''
prevPoint=[0,0]
currentPoint=[0,0]



def paint(e):
    global prevPoint,currentPoint
    print("I am in paint")
    #prevPoint=[currentPoint[0],currentPoint[1]]
    currentPoint=[e.x,e.y]
    x=e.x
    y=e.y
   # mainCanvas.create_line(x,y,x+5,y+5,fill="black")
    if(prevPoint!=[0,0]):
        mainCanvas.create_polygon(prevPoint[0],prevPoint[1],currentPoint[0],currentPoint[1],fill=defaultColor.get(),outline=defaultColor.get(),width=stroke_size.get())
    prevPoint=currentPoint
    if(e.type=="5"):
        prevPoint=[0,0]






root.resizable(False,False)

# Start the main event loop
root.mainloop()
