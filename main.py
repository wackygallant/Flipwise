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
        # --- Main Window Grid ---
        self.grid_columnconfigure(0, weight=1)
        

        # --- Header Frame ---
        self.frame_header = ctk.CTkFrame(self)
        self.frame_header.grid(
            row=0, column=0, 
            columnspan=2, 
            padx=20, pady=(20,10), 
            sticky="ew"
        )
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

        # --- Tabs ---
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
        # --- Stats Row Frame  ---
        self.frame_stats = ctk.CTkFrame(self.tab_quiz)
        self.frame_stats.grid(
            row=0, column=0,
            padx=10, pady=(10,5),
            stick="ew"
        )

        # Makes all 3 columns equal in size inside the frame
        self.frame_stats.grid_columnconfigure((0,1,2), weight=1)

        # -- Total cards label --
        self.lbl_total = ctk.CTkLabel(
            self.frame_stats, 
            text="Total: 0",
            font=ctk.CTkFont(size=13)
        )
        self.lbl_title.grid(row=0, column=0, pady=8)

        # -- Correct count label --
        self.lbl_correct = ctk.CTkLabel(
            self.frame_stats,
            text="Correct: 0",
            font=ctk.CTkFont(size=13),
            text_color="#1D9E75"     # Green Color
        )
        self.lbl_correct.grid(row=0, column=1,pady=8, sticky="ew")

        # Incorrect count label
        self.lbl_incorrect = ctk.CTkLabel(
            self.frame_stats,
            text="Incorrect: 0",
            font=ctk.CTkFont(size=13),
            text_color="#D85A30"       # Red Color
        )
        self.lbl_incorrect.grid(row=0, column=2, pady=8, sticky="ew")

        # -- Card Frame--
        self.frame_card = ctk.CTkFrame(self.tab_quiz)
        self.frame_card.grid(
            row=1, column=0,
            padx=10, pady=5, 
            sticky="ew"
        )
        self.frame_card.columnconfigure(0, weight=1)

        # Progress Label
        self.lbl_progress = ctk.CTkLabel(
            self.frame_card, 
            text="Card 0 of 0",
            font=ctk.CTkFont(size=12), 
            text_color="gray"
        )
        self.lbl_progress.grid(row=0, column=0, padx=15, pady=(15,5), sticky="w")

        self.lbl_question = ctk.CTkLabel(
            self.frame_card,
            text="No cards yet!\nAdd some cards to get started.",
            font=ctk.CTkFont(size=18, weight="bold"),
            wraplength=400, 
            justify="left"
        )
        self.lbl_question.grid(row=1, column=0, padx=15, pady=(5,15), sticky="w")

        # Frame divider
        self.divider = ctk.CTkFrame(self.frame_card, height=1, fg_color="gray")
        self.divider.grid(row=2, column=0, padx=15, sticky="ew")

        # Answer Label
        self.lbl_answer = ctk.CTkLabel(
            self.frame_card,
            text="", 
            font= ctk.CTkFont(size=15),
            wraplength=400, 
            justify="left",
            text_color="gray"
        )
        self.lbl_answer.grid(row=3, column=0, padx=15, pady=(10,15), sticky="w")

        # --Reveal Button --
        self.btn_reveal = ctk.CTkButton(
            self.tab_quiz, 
            text="Reveal Answer", 
            command=self._reveal_answer
        )
        self.btn_reveal.grid(
            row=2, column=0, 
            padx=10, pady=(5,5),
            sticky="ew"
        )

        # Got it / Missed it Buttons
        self.frame_actions = ctk.CTkFrame(self.tab_quiz, fg_color="transparent")
        self.frame_actions.grid(
            row=3, column=0,
            padx=10, pady=(0, 10),
            sticky="ew"
        )
        self.frame_actions.grid_columnconfigure((0,1), weight=1)
        
        # Correct Button
        self.btn_correct = ctk.CTkButton(
            self.frame_actions, 
            text="Got it",
            fg_color="#1D9E75",
            hover_color="#0F6E56",
            command=self._mark_correct
        )
        self.btn_correct.grid(row=0, column=0, padx=(0,5), sticky="ew")

        # Incorrect Button
        self.btn_incorrect = ctk.CTkButton(
            self.frame_actions,
            text="Missed it",
            fg_color="#D85A30",
            hover_color="#993C1D",
            command=self._mark_incorrect
        )
        self.btn_incorrect.grid(row=0, column=1, padx=(0,5), sticky="ew")

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