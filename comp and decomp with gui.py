import tkinter as tk
import base64,zlib
# from comp_and_decom_with_func import compress,decompress
from tkinter import filedialog # filedialog is used for open and select file menu
from tkinter import messagebox
import random

def compressed(inputfile,outputfile):
    data= open(inputfile,'r').read()
    data_bytes=bytes(data,'utf-8') # utf-8, specifies the character encoding scheme 
    co_data=base64.b64encode(zlib.compress(data_bytes,9)) 
    de_data=co_data.decode('utf-8')
    co_file=open(outputfile,'w')
    co_file.write(de_data)
    messagebox.showinfo("info", "compressed successfully")

def decompress(inputfile,outputfile):
    file_content=open(inputfile,'r').read()
    en_data=file_content.encode('utf-8')
    decompressed_data=zlib.decompress(base64.b64decode(en_data))
    decoded_data=decompressed_data.decode('utf-8')
    file=open(outputfile,'w')
    file.write(decoded_data)
    file.close()
    messagebox.showinfo("info", "Decompressed successfully")

def open_file():
    filename=filedialog.askopenfilename(initialdir='/',title="select a file to compress")
    return filename

# def compression(i,o):
#     compress(i,o)

# def decompression(i,o):
#     decompress(i,o)
    
i = 1
def output():
    # outpute=''
    # if len(output_entery.get())>0:
    #     outpute=output_entery.get()
    # else:
    #     a=a+1
    #     outpute='decompressed'+str(a)
    # return outpute
    global i
    inpute = ''
    if len(output_entery.get()) > 0:
        inpute = output_entery.get()
    else:
        inpute = 'decompressed' + str(i)
        i += 1
    return inpute



window=tk.Tk()
window.title("Compression enigne")
window.geometry("600x400")

input_entery=tk.Entry(window)
output_entery=tk.Entry(window)

input_label=tk.Label(window,text="File to be compressed")
output_lable=tk.Label(window,text="give name with .txt extension of the file after compressing you want ? ")

compress_button=tk.Button(window,text="Compress",command=lambda:compressed(open_file(),output()))
  
input_label.grid(row=1,column=1)
# input_entery.grid(row=0,column=1)
output_lable.grid(row=2,column=0)
output_entery.grid(row=2,column=1)
compress_button.grid(row=3,column=1)

input_label1=tk.Label(window,text="File to be decompressed")
output_lable1=tk.Label(window,text="give name with .txt extension of the file after compressing you want ? ")

compress_button1=tk.Button(window,text="deCompress",command=lambda:decompress(open_file(),output()))
input_label1.grid(row=4,column=1)
output_lable1.grid(row=5,column=0)
input_entery.grid(row=5,column=1)
compress_button1.grid(row=7,column=1)

window.mainloop()