import tkinter
import customtkinter
from pytube import YouTube
import re

# system settings
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
  def __init__(self):
    super().__init__()

    # Global parameters
    self.resolution_box_var = customtkinter.StringVar()    
    self.url_var = tkinter.StringVar()
    
    # Window settings
    self.title("My App")
    self.minsize(500, 300)

    # create 2x2 grid system
    # self.grid_rowconfigure(0, weight=1)
    # self.grid_columnconfigure((0, 1), weight=1)

    # Widgets
    self.windows_title = customtkinter.CTkLabel(master=self, text="YouTube Downloader")
    self.windows_title.grid(row=0, column=0, columnspan=2, sticky="nsew")

    self.link = customtkinter.CTkEntry(master=self, width=400, height=40, textvariable=self.url_var) 
    self.link.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

    self.resolution_box = customtkinter.CTkComboBox(master=self, width=100, height=40, values=["High", "Low"])
    self.resolution_box.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)


    # Finish download
    self.finishLabel = customtkinter.CTkLabel(master=self, text="", font=("Arial", 20))
    self.finishLabel.grid(row=3, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

    self.download_btn = customtkinter.CTkButton(master=self, text="Download", width=100, height=40, command=self.start_download)
    self.download_btn.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

  def start_download(self):
      try:      
        self.finishLabel.configure(text="Downloading...")
        yt = YouTube(self.link.get())

        self.windows_title.configure(text=yt.title, text_color="white")

        # Formated title - Delete specials caracters and spaces in title
        formatted_title = yt.title
        formatted_title = re.sub(r'[^\w\s]',"_",formatted_title)
        formatted_title = re.sub(r'\s+',"_",formatted_title)

        ytVideo = yt.streams
        if self.resolution_box.get() == "High":
          ytVideo = ytVideo.get_highest_resolution()
        elif self.resolution_box.get() == "Low":
          ytVideo = ytVideo.get_lowest_resolution()      
        ytVideo.download(skip_existing=True, output_path="downloads", filename_prefix=re.sub(r'[^\w\s]',"_",yt.channel_id), filename=formatted_title + ".mp4")
        self.finishLabel.configure(text="Donwload finished!")          
      except Exception as e:
        print(e)
        self.finishLabel.configure(text="Une Erreur est survenue", fg_color="red")


# Run app
if __name__ == "__main__":
    app = App()
    app.mainloop()