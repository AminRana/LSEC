import tkinter as tk
import tkinter.scrolledtext as tkst

import message_manager as messages
import font_manager as fonts


class ReadMessage():
    def __init__(self, window, message_id):
        self.message_id = message_id

        self.window = window
        self.window.geometry("500x320")
        self.window.title(f"Read Message {message_id}")

        sender_lbl = tk.Label(window, text="From:")
        sender_lbl.grid(row=0, column=0, sticky="E", padx=10, pady=10)

        self.sender_txt = tk.Entry(window, width=40)
        self.sender_txt.grid(row=0, column=1, columnspan=5, sticky="W", padx=10, pady=10)

        recipient_lbl = tk.Label(window, text="To:")
        recipient_lbl.grid(row=1, column=0, sticky="E", padx=10, pady=10)

        self.recipient_txt = tk.Entry(window, width=40)
        self.recipient_txt.grid(row=1, column=1, columnspan=5, sticky="W", padx=10, pady=10)

        subject_lbl = tk.Label(window, text="Subject:")
        subject_lbl.grid(row=2, column=0, sticky="E", padx=10, pady=10)

        self.subject_txt = tk.Entry(window, width=40)
        self.subject_txt.grid(row=2, column=1, columnspan=5, sticky="W", padx=10, pady=10)

        self.content_txt = tkst.ScrolledText(window, width=48, height=6, wrap="word")
        self.content_txt.grid(row=3, column=0, columnspan=6, sticky="W", padx=10, pady=10)

        subject_lbl = tk.Label(window, text="New priority (1-5):")
        subject_lbl.grid(row=4, column=0, columnspan=2, sticky="E", padx=10, pady=10)

        self.priority_txt = tk.Entry(window, width=3)
        self.priority_txt.grid(row=4, column=2, sticky="W", padx=10, pady=10)

        update_btn = tk.Button(window, text="Update", command=self.update_priority)
        update_btn.grid(row=4, column=3, sticky="W", padx=10, pady=10)

        delete_btn = tk.Button(window, text="Delete", command=self.delete_message)
        delete_btn.grid(row=4, column=4, padx=10, pady=10)

        close_btn = tk.Button(window, text="Close", command=self.close)
        close_btn.grid(row=4, column=5, padx=10, pady=10)

        if message_id is not None:
            sender = messages.get_sender(message_id)
            if sender is not None:
                self.sender_txt.insert(tk.END, sender)
                self.sender_txt.configure(state='readonly')
                self.recipient_txt.insert(tk.END, messages.get_recipient(message_id))
                self.recipient_txt.configure(state='readonly')
                self.subject_txt.insert(tk.END, messages.get_subject(message_id))
                self.subject_txt.configure(state='readonly')
                self.content_txt.insert(tk.END, messages.get_content(message_id))
            else:
                self.content_txt.insert(tk.END, 'No such message')
        self.content_txt["state"] = "disabled"

    def delete_message(self):
        if self.message_id is not None:
            messages.delete_message(self.message_id)
        self.close()

    def update_priority(self):
        if self.message_id is not None:
            messages.set_priority(self.message_id, int(self.priority_txt.get()))

    def close(self):
        self.window.destroy()


if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()  # create a TK object
    fonts.configure()  # configure the fonts
    ReadMessage(window, None)  # open the ReadMessage GUI
    window.mainloop()  # run the window main loop, reacting to button presses, etc
