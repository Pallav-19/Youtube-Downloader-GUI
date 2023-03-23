import tkinter
import customtkinter
from pytube import YouTube


def startDownload():
    try:
       
        ytLink = linkInput.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title, text_color="yellow")
        video.download()

        finishText.configure(text="Download Complete!", text_color='green')
    except:

        finishText.configure(text="YouTube Link is invalid", text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded/total_size) * 100
    pPercentage.configure(text=str(int(percentage))+"%")
    pPercentage.update()
    title.configure()
    progressBar.set(float(percentage)/100)


# appearance
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")
app = customtkinter.CTk()  # init app
# frame
app.geometry("720x480")
app.title('YouTube Downloader')
# elements

title = customtkinter.CTkLabel(app, text="Insert a YouTube video link")
title.pack(padx=10, pady=10)
# input
url_var = tkinter.StringVar()
linkInput = customtkinter.CTkEntry(
    app, height=40, width=350, textvariable=url_var, placeholder_text="Paste the video link here!")
linkInput.pack(padx=10, pady=10)
# finishText
finishText = customtkinter.CTkLabel(app, text=" ")
finishText.pack()
# button
download = customtkinter.CTkButton(
    app, width=100, height=40, text="Download", command=startDownload)
download.pack(padx=10, pady=10)
# progress
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()
progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)
# Run app
app.mainloop()
