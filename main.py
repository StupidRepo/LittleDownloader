import sys
from tkinter import ttk
import requests
import tkinter
from queue import Queue
from threading import Thread

tk = tkinter.Tk()
tk.geometry("720x65")
tk.resizable(True, False)
tk.title('LittleDownloader: Ready')

statusVar = tkinter.StringVar()

def out(text):
    statusVar.set(text)

def checkForUpdates():
    out('Checking for updates...')
    try:
        r = requests.get('https://raw.githubusercontent.com/StupidRepo/LittleDownloader/main/version.txt')
        if int(r.text) > 3:
            out('An update is available! Please download the latest version from GitHub!')
        else:
            out('Enter a URL in the box above, then press Enter to start downloading.')
    except Exception as e:
        pass

chunk_size = 512

def doDownload(url):
    cut = url.split('/')
    path = f"{cut[-1]}"
    website = f"{cut[2]}"

    tk.title(f'LittleDownloader: Preparing - ({queue.qsize()} files left)')
    out(f'Starting download from {website}, please wait...')
    r = requests.get(url, stream=True)
    with open(path, 'wb+') as f:
        total_length = int(r.headers.get('content-length'))
        total_chunks = total_length / chunk_size
        current_chunk = 0
        total_mb = round(total_length / 1024 ** 2, 1)
        for chunk in r.iter_content(chunk_size=chunk_size):
            current_chunk += 1
            current_mb = round(current_chunk * chunk_size / 1024 ** 2, 1)
            percentage = min(round(current_chunk / total_chunks * 100, 2), 100.0)
            queuesize = queue.qsize()
            progressBar['value'] = percentage
            tk.title(f'LittleDownloader: Downloading - {percentage}% ({queuesize} files left)')
            out(f'Downloading {path} - {current_mb} MB ({percentage}%) of {total_mb} MB downloaded! (Files left: {queuesize})\r')
            if chunk:
                f.write(chunk)
                f.flush()

    sys.stdout.flush()

    if queue.qsize() == 0:
        tk.title(f'LittleDownloader: Ready')
        out(f'Downloaded all files successfully!')
    else:
        tk.title(f'LittleDownloader: Waiting - {queuesize} files left')

    progressBar['value'] = 0.0

class DownloadWorker(Thread):
    def __init__(self, theQueue):
        Thread.__init__(self)
        self.queue = theQueue

    def run(self):
        while True:
            link = self.queue.get()
            try:
                doDownload(link)
            except requests.exceptions.MissingSchema:
                out('Please include the protocol (http:// or https://) in the URL.')
            except requests.exceptions.ConnectionError:
                out('Connection error. Please check your connection and try again.')
            except requests.exceptions.InvalidURL:
                out('Invalid URL. Please check the URL and try again.')
            except requests.exceptions.InvalidSchema:
                out('Invalid protocol. http:// or https:// are the only accepted protocols.')
            except TypeError:
                out('Could not determine file size or something else.')
            except Exception as e:
                out(f'An unknown error occured: {e}')
            finally:
                self.queue.task_done()

queue = Queue()

worker = DownloadWorker(queue)
worker.daemon = True
worker.start()

def makeWorkerAndRun(urlToDownload):
    queue.put(urlToDownload)

urlVar = tkinter.StringVar()

urlInputBox = tkinter.Entry(tk, textvariable=urlVar, width=200, justify='center')
urlInputBox.pack()
urlInputBox.focus_set()
urlInputBox.bind('<Return>', lambda eaea: makeWorkerAndRun(urlVar.get()))

statusLabel = tkinter.Label(tk, textvariable=statusVar)
statusLabel.pack()

progressBar = ttk.Progressbar(tk, orient='horizontal', mode='determinate', length=500)
progressBar.pack()

checkForUpdates()

tk.mainloop()