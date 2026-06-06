import customtkinter as ctk
from deck import Deck

# --- App settings ---
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class FlipwiseApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Flipwise")
        self.geometry("500x600")
        self.deck = Deck()
        self.deck.load()
        self.current_index = 0
        self.answer_visible = False
        
        self._build_ui()

    def _build_ui(self):
        # configure the main window grid
        # weight=1 means the column stretches to fill available space
        self.grid_columnconfigure(0, weight=1)
        

        # --- Header Frame ---
        self.frame_header = ctk.CTkFrame(self)
        self.frame_header.grid(
            row=0, column=0, 
            columnspan=2, 
            padx=20, pady=(20,10), 
            sticky="ew"
        )
        # make the header frame's internal columns stretchable
        # column 0 = title (left), column 1 = card count (right)
        self.frame_header.grid_columnconfigure(1, weight=1)


        # --- App title label ---
        self.lbl_title = ctk.CTkLabel(
            self.frame_header, 
            text="Flipwise",
            font=ctk.CTkFont(size=22, weight="bold")
        )
        self.lbl_title.grid(
            row=0, column=0,
            padx=15, pady=10, 
            sticky="w"
        )
        
        # Card Count Label
        self.lbl_card_count = ctk.CTkLabel(
            self.frame_header,
            text="0 cards",
            font=ctk.CTkFont(size=13), 
            text_color="gray"
        )
        self.lbl_card_count.grid(
            row=0, column=1,
            padx=15, pady=10,
            sticky="e"
        )

        # --- Creating Tab View ---
        self.tabview = ctk.CTkTabview(self)
        self.tabview.grid(
            row=1, column=0,        # row 1, right below the header
            padx=20, pady=(0,20),   # 20px sides, 20px bottom
            sticky="nsew"           # stretch in all directions
        )

        # Configure the row to expand vertically/ if not the tabview won't grow
        self.rowconfigure(1, weight=1)

        # --- Adding Tabs ---
        self.tab_quiz = self.tabview.add("Quiz")
        self.tab_add = self.tabview.add("Add Card")
        self.tab_stats = self.tabview.add("Stats")

        # Configuring the tab's grid to be stretchy
        self.tab_quiz.grid_columnconfigure(0, weight=1)
        self.tab_add.grid_columnconfigure(0, weight=1)
        self.tab_stats.grid_columnconfigure(0, weight=1)

        # Calling each tabs contents
        self._build_quiz_tab()
        self._build_add_tab()
        self._build_stats_tab()

    def _build_quiz_tab(self):
        pass

    def _build_add_tab(self):
        pass

    def _build_stats_tab(self):
        pass

    def _show_quiz(self):
        # display current flashcard question
        pass

    def _reveal_answer(self):
        # reveal the answer
        pass

    def _mark_correct(self):
        # mark card correct, move to next
        pass

    def _mark_incorrect(self):
        # mark card incorrect, move to next
        pass

    def _add_card(self):
        # get input from entry fields and add card
        pass

    def _save_and_exit(self):
        # save deck and close app
        pass

if __name__ == "__main__":
    app = FlipwiseApp()
    app.mainloop()