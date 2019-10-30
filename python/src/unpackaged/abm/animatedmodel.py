import random
import tkinter as tk
import matplotlib
matplotlib.use('TkAgg')
#matplotlib.use('macosx')
import matplotlib.pyplot
import matplotlib.animation 
import agentframework
import csv
import requests
import bs4


# =============================================================================
# Reading the data from the specified url, "read_site" return the response 200,
# which means a successful execution of request
# =============================================================================
read_site = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')

# Getting the content of the HTML page (including HTML tags) by using ".text"
content = read_site.text

# Using the "Beautiful Soup" Python library to pull data out of HTML
soup = bs4.BeautifulSoup(content, 'html.parser')


# =============================================================================
# # Using the attribute "class" in searches by putting it into a dictionary and
# then passing the dictionary into the "find_all()" as the "attrs" argument
# =============================================================================
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)


# Initializing global variables and giving them default values
num_of_agents = 20
num_of_iterations = 200

# 20 is the radius around agents
neighbourhood = 20

# Setting the figure size for the plot to (width = 7, height = 7)
fig = matplotlib.pyplot.figure(figsize=(7, 7))

# Adding axes at position [left, bottom, widht, height]
ax = fig.add_axes([0, 0, 1, 1])

# Initially setting the global boolean variable "carry_on" to True
carry_on = True


# =============================================================================
# # Creating an empty list called "environment" 
# (as it will store environmental data) to store the data read from the csv
# file into a 2D list  
# =============================================================================
environment = []

# Reading the data from the csv file "in.csv" for pixelation" 
f = open('in.csv', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
 # A list of rows
for row in reader:
    # Creating an empty list called "rowlist" to store all the values
     rowlist = []
     
     # A list of value
     for value in row:
         rowlist.append(value)


# =============================================================================
#    # Adding the values from each row to the "environment" list making it a 
#    #2D List
# =============================================================================
     environment.append(rowlist)
     
# Once done with the reader close the file
f.close()


# Creating the agents
agents = []
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents, y, x))


def update(frame_number):
    """
    In this function we are plotting the agents, randomly shuffling them,
    making them move, eat and share with neighbours until their store 
    (grass consumption) is greater than 1000.
    """
    global carry_on
    fig.clear()   
    
    
    # Using the matplot librabry to plot our agents        
    matplotlib.pyplot.xlim(0, 300)
    matplotlib.pyplot.ylim(300, 0)
    


# =============================================================================
#     # Checking that the data has been imported correctly by plotting it
#     choosing and specifying the colormap
# =============================================================================
    matplotlib.pyplot.imshow(environment,cmap='summer')
    
    # Randomly shuffling the agents
    random.shuffle(agents)
    
    for i in range(num_of_agents):
        #print('store - {0}'.format(agents[i].store))
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)



# =============================================================================
#         Scaling the agent by setting the size ("s") equal to the amount of 
#         grass eaten so they grow as they eat more and when they ate, in other
#         words when "store" is more than 1000 stop as they are full
# =============================================================================
        matplotlib.pyplot.scatter(agents[i].get_x(),agents[i].get_y(),
                                  s=agents[i].store, marker=r'$\clubsuit$')
        if agents[i].store > 1000:
            print("Agent {} is full!".format(i))
            carry_on = False
        #print('store - {0}'.format(agents[i].store))
        
    

def gen_function(b = [0]):
    """ 
    In this function we are setting some conditions:
    while the value is less than the specified number of iterations 
    (num_of_iterations) and "carry_on" is true return (yield: Returns 
    control and waits next call) the value, which is initally set to 0 and
    add 1 to it each time until the conditions are no longer true
    """
    a = 0
    global carry_on 
    while (a < num_of_iterations) & (carry_on) :
        yield a	# Returns control and waits next call.
        a = a + 1


def run():
    """ 
    In this function we are making the animation by calling a function 
    "func" over and over again. 
    """
    animation = matplotlib.animation.FuncAnimation(fig, update, interval=1000,
            repeat=False, frames=gen_function)

    canvas.draw()



def IO_agent_num():
    """ 
    In this function we are getting the number of agents specified by
    the user and then casting them to integer.
    """
    global entry
    input_num = entry.get()
    global num_of_agents
    num_of_agents = int(input_num)
    


def IO_iterations_num():
    """ 
    In this function we are getting the number of iterations specified by
    the user and then casting them to integer.
    """
    global iteration_scale
    input_num = iteration_scale.get()
    global num_of_iterations
    num_of_iterations = int(input_num)


# Creating the main window
root = tk.Tk()

# =============================================================================
# Setting a minimum size for the main window by using the  Tkinter built-in 
# function minsize(height, width)
# =============================================================================
root.minsize(800,800)
# Setting the title for the main window
root.wm_title("Model")
# Creating canvas
canvas = tk.Canvas(root)


# =============================================================================
# Using the Frame from the Tkinter library to organize widgets, passing the 
# parent  window ("root") and specifying the size of the border
# =============================================================================
image_frame = tk.Frame(root, bd=10)


# =============================================================================
# Using the geometry manager "place" to organize the image frame in a specific
# position in the parent widget. 
# - relx, rely: horizontal and vertical offset (floating number between 0.0 and 1.0)
# - relheight, relwidth: height and width (floating number between 0.0 and 1.0)
# - anchor: the precise location of the widget, in this case 'center'
# =============================================================================
image_frame.place(relx=0.5, rely=0.7, relheight= 0.6, relwidth=0.75,
                  anchor='center')


# =============================================================================
# Creating and laying out a matplotlib canvas embedded inside the window and 
# connected with "fig", setting the "image_frame" as the master (parent widget) 
# =============================================================================
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, 
                  master=image_frame)


# =============================================================================
# Using the geometry manager "pack", specifying the:
# - side: to decide which side of the parent widget packs againtst (TOP)
# - fill: to decide whether widget fills any extra space reserved for it by the
#   packer, in this case "BOTH" - fill both horizontally and vertically
# - expand: to allow the widget to expand and fill out any space not used 
#    inside the widget's parent 
# =============================================================================
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
# Creating the main menu
menu_bar = tk.Menu(root)
# Displaying the main menu
root.config(menu=menu_bar)
model_menu = tk.Menu(menu_bar)
# Creating a submenu by using "add_cascade", passing it the label and menu
menu_bar.add_cascade(label="Model", menu=model_menu)


# =============================================================================
# Adding menu item to the menu, passing it the label and command to call the 
# run function
# =============================================================================
model_menu.add_command(label="Run model", command=run)



# =============================================================================
# Creating another frame for the agents number, specifying root (parent window)
# background colour and size of the border
# =============================================================================
agentsNum_frame = tk.Frame(root, bg='#80c1ff', bd=5)
agentsNum_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, 
                      anchor='n')

# Creating the Entry widget to allow the user to enter the number of agents 
entry = tk.Entry(agentsNum_frame)
entry.place(relwidth=0.65, relheight=0.5)

# Using entry.focus_set() to set direct input focus to this widget
entry.focus_set()


# =============================================================================
# Creating the Button on the "agentsNum_frame" with text to display in the 
# button and "IO_agent_num" function is called when the button is pressed
# =============================================================================
agentsNum_btn = tk.Button(agentsNum_frame,text='Number of agents',
                          command=IO_agent_num)
agentsNum_btn.place(relx=0.70, relheight=1, relwidth=0.3)


# =============================================================================
# Creating another frame for the iterations number, specifying root 
#(parent window), background colour and size of the border
# =============================================================================
iterationsNum_frame = tk.Frame(root, bg='yellow', bd=5)
iterationsNum_frame.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.1,
                          anchor='n')
# Setting the returned value to be a float
var = tk.DoubleVar()


# =============================================================================
# Creating the Scale widget, which will allow the user to select a numerical 
# value by moving the slider, the minumum and maximum value have been specified. 
# Furthermore, we specify that we want a "HORIZONTAL" slider.
# =============================================================================
iteration_scale = tk.Scale(iterationsNum_frame, from_=0, to=200,
                           orient=tk.HORIZONTAL)
iteration_scale.place(relwidth=0.65, relheight=0.5)  
iteration_btn = tk.Button(iterationsNum_frame, text="Iteration number",
                          command=IO_iterations_num)
iteration_btn.place(relx=0.70,relheight=1, relwidth=0.3)  



# Execution of the python program halts here
tk.mainloop()













