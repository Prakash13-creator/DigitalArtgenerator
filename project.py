import turtle
import random
from PIL import Image

# Global color options
colors = ["red", "yellow", "blue", "green", "orange", "purple", "white"]

# Pattern functions
def draw_spiral(t, color, pen_width):
    for i in range(360):
        t.pencolor(color if color != "random" else random.choice(colors))
        t.width(pen_width)
        t.forward(i)
        t.left(59)

def draw_star(t, size, color, pen_width):
    t.pencolor(color if color != "random" else random.choice(colors))
    t.width(pen_width)
    for _ in range(5):
        t.forward(size)
        t.right(144)

def draw_polygon(t, sides, size, color, pen_width):
    angle = 360 / sides
    t.pencolor(color if color != "random" else random.choice(colors))
    t.width(pen_width)
    for _ in range(sides):
        t.forward(size)
        t.right(angle)

# Style input
def get_user_style():
    color = input("Enter a color (red, blue, green, etc.) or 'random': ").lower()
    pen_width = int(input("Enter pen width (e.g., 2): "))
    return color, pen_width

# Save canvas to image
def save_art(canvas, filename):
    canvas.postscript(file=filename + ".eps")
    img = Image.open(filename + ".eps")
    img.save(filename + ".png")
    print(f"Artwork saved as {filename}.png")

# Main program
def main():
    screen = turtle.Screen()
    screen.bgcolor("black")
    artist = turtle.Turtle()
    artist.speed(0)

    while True:
        print("\nChoose a pattern to draw:")
        print("1. Spiral")
        print("2. Star")
        print("3. Polygon")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        artist.clear()
        artist.penup()
        artist.home()
        artist.pendown()

        if choice == '1':
            color, pen_width = get_user_style()
            draw_spiral(artist, color, pen_width)
        elif choice == '2':
            size = int(input("Enter star size: "))
            color, pen_width = get_user_style()
            draw_star(artist, size, color, pen_width)
        elif choice == '3':
            sides = int(input("Number of sides: "))
            size = int(input("Side length: "))
            color, pen_width = get_user_style()
            draw_polygon(artist, sides, size, color, pen_width)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
            continue

        # Ask to save
        save = input("Do you want to save this art? (yes/no): ").lower()
        if save == "yes":
            filename = input("Enter filename (without extension): ")
            canvas = turtle.getcanvas()
            save_art(canvas, filename)

    turtle.done()

if __name__== "__main__":
    main()
