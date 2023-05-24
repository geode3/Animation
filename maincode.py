# Rotting apple
import simplegui

def draw_handler(canvas):
    global count
    
    if count == 30:
        colors[3][5] = "#80e5ff"
        colors[4][5] = "#80e5ff"
        colors[5][5] = "#80e5ff"

    if count == 60:
        colors[4][4] = "#80e5ff"

    if count == 90:
        colors[4][3] = "#5B452A"
        colors[3][4] = "#5B452A"
        colors[5][4] = "#5B452A"
        colors[2][4] = "#CDA474"
        colors[6][4] = "#CDA474"
    if count == 120:
        colors[4][1] = "#80e5ff"
        colors[3][1] = "#80e5ff"
        colors[5][1] = "#80e5ff"
    if count == 150:
        colors[4][2] = "#80e5ff"
    if count == 180:
        colors[3][2] = "#5B452A"
        colors[5][2] = "#5B452A"
        colors[2][2] = "#CDA474"
        colors[6][2] = "#CDA474"
    if count == 210:
        colors[3][3] = "#CDA474"
        colors[2][3] = "#CDA474"
        colors[5][3] = "#CDA474"
        colors[6][3] = "#CDA474"
    if count > 210:
        count = 29
    row = 0
    col = 0
    
    # Draws image row by row
    for r in range(1, 350, 50):
        # And column by column
        for c in range(1, 350, 50):
            canvas.draw_polygon([(c, r), (c + 50, r), (c + 50, r + 50), (c, r + 50)], 1, "black", colors[row][col])
            col = col + 1
        row = row + 1
        col = 0
    
    # Keeps track of which frame the image is on - essentially controlling when each box changes color
    count += 1

# Main Part of Program
frame = simplegui.create_frame("Pic", 350, 350)
frame.set_draw_handler(draw_handler)
frame.start()

# A variable that will keep track of the frame
count = 0

# Creates our 2D list which is our original image
colors = []
colors.append(["#80e5ff", "#80e5ff", "#80e5ff", "#725635", "#6CDA32", "#6CDA32", "#80e5ff"])     
colors.append(["#80e5ff", "#80e5ff", "#80e5ff", "#725635", "#80e5ff", "#80e5ff", "#80e5ff"])    
colors.append(["#80e5ff", "#80e5ff", "#F61835", "#F61835", "#F61835", "#80e5ff", "#80e5ff"])    
colors.append(["#80e5ff", "#F61835", "#F61835", "#F61835", "#F61835", "#F61835", "#80e5ff"])
colors.append(["#80e5ff", "#F61835", "#F61835", "#F61835", "#F61835", "#F61835", "#80e5ff"])    
colors.append(["#80e5ff", "#F61835", "#F61835", "#F61835", "#F61835", "#F61835", "#80e5ff"])    
colors.append(["#80e5ff", "#80e5ff", "#F61835", "#F61835", "#F61835", "#80e5ff", "#80e5ff"])
