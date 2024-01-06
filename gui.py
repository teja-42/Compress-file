from tkinter import * 
from compressmodule import compress,decompress
from tkinter import filedialog

def open_file():
    file_name=filedialog.askopenfilename(initialdir='/',title="Select a file to compress")
    return file_name

def compression(i,o):
    compress(i,o)

def decompression(i,o):
    decompress(i,o)
root=Tk()

root.title("Compression engine")
root.geometry("600x400")

'''input_entry=Entry(root,)
output_entry=Entry(root,)

li=Label(root,text="File to be compressed")
li.grid(row=0,column=0)
input_entry.grid(row=0,column=1)

lo=Label(root,text="Name of the compressed file")
lo.grid(row=1,column=0)
output_entry.grid(row=1,column=1)'''

b=Button(root,text="Compress",command=lambda: compression(open_file(),"compressedoutput1.txt"))
b.grid(row=2,column=1)

'''b=Button(root,text="Decompress",command=lambda: decompression(input_entry.get(),output_entry.get()))
b.grid(row=3,column=1)'''


root.mainloop()