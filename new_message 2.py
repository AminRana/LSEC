
import tkinter as tk
import tkinter.scrolledtext as tkst

import message_manager as messages
import font_manager as fonts


class NewMessage:
    def __init__(self, window, message_id=None):
        self.window = window
        self.message_id = message_id

        # ----- Window Settings -----
        self.window.geometry("500x330")

        if message_id is None:
            self.window.title("New Message")
        else:
            self.window.title(f"Message #{message_id}")

        # ======= ROW 0: Sender =======
        tk.Label(window, text="Sender:").grid(row=0, column=0, sticky="E", padx=10, pady=10)
        self.sender_txt = tk.Entry(window, width=40)
        self.sender_txt.grid(row=0, column=1, columnspan=5, sticky="W", padx=10)

        # ======= ROW 1: Recipient =======
        tk.Label(window, text="Recipient:").grid(row=1, column=0, sticky="E", padx=10, pady=10)
        self.recipient_txt = tk.Entry(window, width=40)
        self.recipient_txt.grid(row=1, column=1, columnspan=5, sticky="W", padx=10)

        # ======= ROW 2: Subject =======
        tk.Label(window, text="Subject:").grid(row=2, column=0, sticky="E", padx=10, pady=10)
        self.subject_txt = tk.Entry(window, width=40)
        self.subject_txt.grid(row=2, column=1, columnspan=5, sticky="W", padx=10)

        # ======= ROW 3: Content =======
        self.content_txt = tkst.ScrolledText(window, width=48, height=6, wrap="word")
        self.content_txt.grid(row=3, column=0, columnspan=6, padx=10, pady=10)

        # ======= ROW 4: Priority + Buttons =======
        tk.Label(window, text="Priority (1-5):").grid(row=4, column=0, sticky="E", padx=10)

        self.priority_txt = tk.Entry(window, width=3)
        self.priority_txt.grid(row=4, column=1, sticky="W", padx=10)

        # Buttons depend on create / read mode
        if message_id is None:
            # Creating a new message
            tk.Button(window, text="Send", command=self.send_message).grid(row=4, column=2, padx=10)
            tk.Button(window, text="Cancel", command=self.close).grid(row=4, column=3, padx=10)
        else:
            # Reading existing message
            tk.Button(window, text="Update Priority", command=self.update_priority).grid(row=4, column=2, padx=10)
            tk.Button(window, text="Delete", command=self.delete_message).grid(row=4, column=3, padx=10)
            tk.Button(window, text="Close", command=self.close).grid(row=4, column=4, padx=10)

        # Load message data (if existing)
        if message_id is not None:
            self.load_existing_message()
        else:
            self.priority_txt.insert(0, "3")   # Default priority for new messages

    # ----------------------------------------------------------------------
    # Load data for existing messages (read-only)
    # ----------------------------------------------------------------------
    def load_existing_message(self):
        sender = messages.get_sender(self.message_id)

        if sender is None:
            self.content_txt.insert(tk.END, "No such message")
            self.content_txt.config(state="disabled")
            return

        # Populate fields
        self.sender_txt.insert(tk.END, sender)
        self.recipient_txt.insert(tk.END, messages.get_recipient(self.message_id))
        self.subject_txt.insert(tk.END, messages.get_subject(self.message_id))
        self.content_txt.insert(tk.END, messages.get_content(self.message_id))

        # Make fields read-only
        self.sender_txt.config(state="readonly")
        self.recipient_txt.config(state="readonly")
        self.subject_txt.config(state="readonly")
        self.content_txt.config(state="disabled")

    # ----------------------------------------------------------------------
    # Send new message
    # ----------------------------------------------------------------------
    def send_message(self):
        sender = self.sender_txt.get()
        recipient = self.recipient_txt.get()
        subject = self.subject_txt.get()
        content = self.content_txt.get("1.0", tk.END).strip()

        # Validate
        if not sender or not recipient or not subject or not content:
            print("❌ All fields must be filled to send a message.")
            return

        try:
            priority = int(self.priority_txt.get())
            if priority < 1 or priority > 5:
                raise ValueError
        except ValueError:
            print("❌ Priority must be a number between 1 and 5.")
            return

        # Save via message_manager
        messages.create_message(sender, recipient, subject, content, priority)
        print("✅ Message sent successfully!")
        self.close()

    # ----------------------------------------------------------------------
    # Update priority for existing messages
    # ----------------------------------------------------------------------
    def update_priority(self):
        try:
            priority = int(self.priority_txt.get())
            if priority < 1 or priority > 5:
                raise ValueError
        except ValueError:
            print("❌ Priority must be between 1 and 5.")
            return

        messages.set_priority(self.message_id, priority)
        print("✅ Priority updated.")

    # ----------------------------------------------------------------------
    # Delete existing message
    # ----------------------------------------------------------------------
    def delete_message(self):
        messages.delete_message(self.message_id)
        print("🗑️ Message deleted.")
        self.close()

    # ----------------------------------------------------------------------
    def close(self):
        self.window.destroy()


# ----------------------------------------------------------------------
# Run standalone
# ----------------------------------------------------------------------
if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    NewMessage(window, None)  # Start in "new message" mode
    window.mainloop()
