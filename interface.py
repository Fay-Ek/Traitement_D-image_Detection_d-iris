import os
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
import histogram 
import filtre_medianP
import hough2
import contour2
import SIFT
import eucledienne

class App(tk.Tk):
    
    def __init__(self):
        super().__init__()
        
        self.title('Bievenue dans le systeme d\'identification par l\'IRIS ')
        self.resizable(0, 0)
        self.rowconfigure(0, minsize=800, weight=1)
        self.columnconfigure(1, minsize=800, weight=1)

        canvas_images_opts = {
            'width': 220,
            'height': 220,
            'bg': '#e2e8f0',
        }
        
        canvas_images_opts2 = {
            'width': 445,
            'height': 230,
            'bg': '#e2e8f0',
        }
        
        canvas_images_opts3 = {
            'width': 400,
            'height': 230,
            'bg': '#f2edd7',
        }
        
        
        root_frame = tk.Frame(self)
        root_frame.pack(fill=tk.BOTH)
        root_frame.rowconfigure(0, weight=1)
        root_frame.columnconfigure(0, weight=1)

        frame_1 = tk.Frame(root_frame)
        frame_1.grid(row=0, column=0, sticky=tk.W+tk.E)

        self.canvas_1 = tk.Canvas(frame_1, **canvas_images_opts)
        self.canvas_1.grid(row=0, column=0, rowspan=2, padx=(10, 0), pady=(10, 0))
        self.canvas_1.create_image((100, 90), anchor=tk.CENTER, tag='original_image')
    
        btns_frame = tk.Frame(frame_1)
        btns_frame.grid(row=0, column=1)

        btn_opts = {'height': 2, 'width': 10, 'border': 5, 'bg': 'grey', 'fg': 'black'}
        btn_grid_opts = {'padx': (10, 0), 'sticky': tk.W+tk.E}

        btn_enroll = tk.Button(btns_frame, text='Enroll', **btn_opts, command=self.enroll)
        btn_enroll.grid(row=0, column=0, **btn_grid_opts)

        btn_recognition = tk.Button(btns_frame, text='Recognition', **btn_opts,command=self.histogram)
        btn_recognition.grid(row=1, column=0, **btn_grid_opts)

        frame_2 = tk.Frame(root_frame)
        frame_2.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E+tk.W+tk.N+tk.S)

        frame_2.columnconfigure(0, weight=1)
        frame_2.columnconfigure(1, weight=1)
        frame_2.columnconfigure(2, weight=1)
        frame_2.columnconfigure(3, weight=1)
        frame_2.columnconfigure(4, weight=1)

        self.canvas_2 = tk.Canvas(frame_2, **canvas_images_opts)
        self.canvas_2.grid(row=0, column=0, padx=(0, 0), pady=(10, 0))
        self.canvas_2.create_image((100, 90), anchor=tk.CENTER, tag='Egalisation_histogramme')
        self.label_canvas_2 = tk.Label(frame_2, text='Egalisation d’histogramme')
        self.label_canvas_2.grid(row=1, column=0, sticky='nswe')
        

        self.canvas_3 = tk.Canvas(frame_2, **canvas_images_opts)
        self.canvas_3.grid(row=0, column=1, padx=(10, 10), pady=(10, 0))
        self.canvas_3.create_image((100, 90), anchor=tk.CENTER, tag='filtre_medianP')
        self.label_canvas_3 = tk.Label(frame_2, text='filtre median Pondéré')
        self.label_canvas_3.grid(row=1, column=1, sticky='nswe')        

        

        self.canvas_4 = tk.Canvas(frame_2, **canvas_images_opts)
        self.canvas_4.grid(row=0, column=2, padx=(0, 10), pady=(10, 0))
        self.canvas_4.create_image((110, 110), anchor=tk.CENTER, tag='hough')
        self.label_canvas_4 = tk.Label(frame_2, text='Extraction de l\'iris')
        self.label_canvas_4.grid(row=1, column=2, sticky='nswe')

        self.canvas_5 = tk.Canvas(frame_2, **canvas_images_opts)
        self.canvas_5.grid(row=0, column=3, padx=(0, 10), pady=(10, 0))
        self.canvas_5.create_image((110, 110), anchor=tk.CENTER, tag='contour2')
        self.label_canvas_5 = tk.Label(frame_2, text='Filtre contour')
        self.label_canvas_5.grid(row=1, column=3, sticky='nswe')

        self.canvas_6 = tk.Canvas(frame_1, **canvas_images_opts2)
        self.canvas_6.grid(row=0, column=2, padx=(20, 0), pady=(10, 0))
        self.canvas_6.create_image((222, 115), anchor=tk.CENTER, tag='sift')
        self.label_canvas_6 = tk.Label(frame_1, text='SIFT')
        self.label_canvas_6.grid(row=1, column=2, sticky='nswe')
        
        
        
        #text
        
        
        
        self.canvas_7 = tk.Canvas(frame_1, **canvas_images_opts3,borderwidth=1, relief="solid")
        self.canvas_7.grid(row=0, column=3, padx=(20, 0), pady=(10, 0))
        self.canvas_7.create_text(225,80, tag="eucledienne" ,font=("Purisa", 20))
        self.label_canvas_7 = tk.Label(frame_1, text='Resultat')
        self.label_canvas_7.grid(row=1, column=3, sticky='nswe')
        
        
     
        
    def enroll(self):

        path_image = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select Image', filetypes=[('BMP File', '*.bmp')])

        if (path_image):
            image = Image.open(path_image)
            image1 = Image.open(path_image)
            self.image = image.resize((320, 280))
            self.image2 = ImageTk.PhotoImage(self.image)
            self.canvas_1.itemconfig('original_image', image=self.image2, anchor=tk.CENTER)
        
    def histogram(self):
        self.image = histogram.histogram(self.image)
        self.image3 = ImageTk.PhotoImage(self.image)
        self.canvas_2.itemconfig('Egalisation_histogramme', image=self.image3)
        self.update()
        self.image1 = filtre_medianP.filtre_medianP(self.image)
        self.image4 = ImageTk.PhotoImage(self.image1)
        self.canvas_3.itemconfig('filtre_medianP', image=self.image4)
        self.update()
        self.image = hough2.extraction_oeuil(self.image)
        self.image5 = ImageTk.PhotoImage(self.image)
        self.canvas_4.itemconfig('hough', image=self.image5)
        self.update()
        self.image = contour2.contour2(self.image)
        self.image6 = ImageTk.PhotoImage(self.image)
        self.canvas_5.itemconfig('contour2', image=self.image6)
        self.update()
        
        
        self.image,self.labelText,opt= SIFT.sift()
        self.image = self.image.resize((454, 230))
        self.image7 = ImageTk.PhotoImage(self.image)
        self.canvas_6.itemconfig('sift', image=self.image7)
        self.update()
        
        #self.labelText= eucledienne.eucledienne()
        if opt==1:
            self.canvas_7.itemconfig('eucledienne', text=self.labelText,fill = 'green',justify='center')
        else:
            self.canvas_7.itemconfig('eucledienne', text=self.labelText,fill = 'red',justify='center')

        
if __name__ == "__main__":
    app = App()
    app.mainloop()