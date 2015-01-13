import Tkinter
# you must create a root window before you can create Tk variables
root = Tkinter.Tk()

# create a Tk string variable
myVar = Tkinter.StringVar()

# define a callback function that describes what it sees
# and also modifies the value
def callbackFunc(name, index, mode):
  print "callback called with name=%r, index=%r, mode=%r" % (name, index, mode)
  varValue = root.globalgetvar(name)
  print "    and variable value = %r" % varValue
  # modify the value, just to show it can be done
  root.globalsetvar(name, varValue + " modified by %r callback" % (mode,))

# set up a trace for writing and for reading;
# save the returned names for future deletion of the trace
wCallbackName = myVar.trace_variable('w', callbackFunc)
rCallbackname = myVar.trace_variable('r', callbackFunc)

# set a value, triggering the write callback
myVar.set("first value")

# get the value, triggering a read callback and then print the value;
# do not perform the get in the print statement
# because the output from the print statement and from the callback
# will be blended together in a confusing fashion
varValue = myVar.get() # trigger read callback
print "after first set, myVar =", varValue

# set and get again to show that the trace callbacks persist
myVar.set("second value")
varValue = myVar.get() # trigger read callback
print "after second set, myVar =", varValue

# delete the write callback and do another set and get
myVar.trace_vdelete('w', wCallbackName)
myVar.set("third value")
varValue = myVar.get() # trigger read callback
print "after third set, myVar =", varValue
root.mainloop()