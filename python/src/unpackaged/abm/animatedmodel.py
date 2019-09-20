import random
import tkinter
from tkinter import *

import matplotlib
matplotlib.use('TkAgg')
#matplotlib.use('macosx')
import matplotlib.pyplot
import matplotlib.animation 

import agentframework
import csv


import requests
import bs4

read_site = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = read_site.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)

num_of_agents = 20
num_of_iterations = 200

# 20 is the radius around agents
neighbourhood = 20

# Setting the figure size for the plot to (width = 7, height = 7)
fig = matplotlib.pyplot.figure(figsize=(7, 7))

# Adding axes at position [left, bottom, widht, height]
ax = fig.add_axes([0, 0, 1, 1])

carry_on = True

#ax.set_autoscale_on(False)

# =============================================================================
# # Creating an empty list called "environment" 
# (as it will store environmental data) to move the data read from the csv
# file into a 2D list  
# =============================================================================
environment = []
# Reading the csv file called "in.csv" 
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


# =============================================================================
def make_agents():
     
    agents = []
    for i in range(num_of_agents):
        y = int(td_ys[i].text)
        x = int(td_xs[i].text)
        agents.append(agentframework.Agent(environment, agents, y, x))

# =============================================================================

# Creating the agents
agents = []
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents, y, x))


def update(frame_number):
    
    global carry_on
    fig.clear()   
    
    
    # Using the matplot librabry to plot our agents        
    matplotlib.pyplot.xlim(0, 300)
    matplotlib.pyplot.ylim(300, 0)
    
    # Checking that the data has been imported correctly by plotting it
    matplotlib.pyplot.imshow(environment)
    
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
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < num_of_iterations) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

def run():
    #make_agents()
    
    animation = matplotlib.animation.FuncAnimation(fig, update, interval=1000,
            repeat=False, frames=gen_function)
    #canvas.show()
    canvas.draw()

def IO_agent_num():
    global w
    input_num = w.get()
    global num_of_agents
    num_of_agents = int(input_num)
    
def IO_iterations_num():
    global iteration_scale
    input_num = iteration_scale.get()
    global num_of_iterations
    num_of_iterations = int(input_num)

root = tkinter.Tk()
root.wm_title("Model")
root.geometry("7000x10000")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)


# =============================================================================
# tk_text = tkinter.Text(root, height=10, width=30)
# tk_text.pack(anchor=NW)
# intructions = """ INSTRUCTIONS TO RUN THE CODE: (step by step)
#     1) """
# tk_text.insert(tkinter.END, intructions)
# =============================================================================

var = tkinter.DoubleVar()
iteration_scale = Scale(root, from_=0, to=200, orient=HORIZONTAL)
iteration_scale.pack(anchor=CENTER)
btn = Button(root, text="Iteration number", command=IO_iterations_num)  
btn.pack(anchor=CENTER) 
#first_set = tkinter.OptionMenu(root, var, "100", "300", "500")
#first_set.configure(font=("Arial", 25))
#first_set.grid(row=1, column=0)
# =============================================================================
# menu_bar.add_cascade(label="Number of iterations", menu=model_menu)
# model_menu.add_command(label="100", command=run)
# model_menu.add_command(label="200", command=run)
# 
# =============================================================================
# =============================================================================
# # =============================================================================

# 
# =============================================================================
w = Entry(root)
w.pack()
w.focus_set()
b = Button(root,text='Number of agents',command=IO_agent_num)
b.pack(side='bottom')

tkinter.mainloop()













