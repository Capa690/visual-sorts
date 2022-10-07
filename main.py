import turtle

def reset():
  pen.penup()
  pen.goto(-190,-190)
  pen.pendown()
  pen.clear()

pen = turtle.Turtle()
pen.speed(0)
turtle.tracer(False)
reset()


def rectangle(x):
  pen.forward(50)
  pen.left(90)
  pen.forward(x)
  pen.left(90)
  pen.forward(50)
  pen.left(90)
  pen.forward(x)
  pen.left(90)
  pen.forward(50)

def draw_bars(nums):
  for i in nums:
    rectangle(i)


nic = [150, 340, 190, 220, 290, 260]

def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            draw_bars(arr)
            turtle.update()
            reset()
    print(arr)

bubble_sort(nic)
