import tkinter as tk

class RectangularSelectionApp:
    def _init_(self, master):
        self.master = master
        self.master.title("Rectangular Selection")

        self.canvas = tk.Canvas(self.master, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.rect_start_x = None
        self.rect_start_y = None
        self.rect_id = None

        self.master.bind("<ButtonPress-1>", self.on_press)
        self.master.bind("<B1-Motion>", self.on_drag)
        self.master.bind("<ButtonRelease-1>", self.on_release)


    def on_press(self, event):
        self.rect_start_x = self.canvas.canvasx(event.x)
        self.rect_start_y = self.canvas.canvasy(event.y)

        # Remove previous rectangles
        self.canvas.delete("rect")

        # Create a new rectangle
        self.rect_id = self.canvas.create_rectangle(
            self.rect_start_x,
            self.rect_start_y,
            self.rect_start_x,
            self.rect_start_y,
            outline="black",
            tags="rect",
        )


    def on_drag(self, event):
        cur_x = self.canvas.canvasx(event.x)
        cur_y = self.canvas.canvasy(event.y)

        # Update the rectangle size as the mouse is dragged
        self.canvas.coords(self.rect_id, self.rect_start_x, self.rect_start_y, cur_x, cur_y)


    def on_release(self, event):
        # Get the coordinates of the selected region
        rect_end_x = self.canvas.canvasx(event.x)
        rect_end_y = self.canvas.canvasy(event.y)

        # Perform actions based on the selected region
        selected_region_start = (self.rect_start_x, self.rect_start_y)
        selected_region_end = (rect_end_x, rect_end_y)

        print("Selected Region Start:", selected_region_start)
        print("Selected Region End:", selected_region_end)

        # Perform additional actions based on the selected region
        # For example, you can highlight or process the selected items within the region


if _name_ == "_main_":
    root = tk.Tk()
    app = RectangularSelectionApp(root)
    root.geometry("400x300")
    root.mainloop()