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
        self.protocol("WM_DELETE_WINDOW", self._save_and_exit)

        self._build_ui()
        self._update_quiz()
        self._update_stats()

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
        self.lbl_total.grid(row=0, column=0, pady=8)

        # -- Correct count label --
        self.lbl_correct = ctk.CTkLabel(
            self.frame_stats,
            text="Correct: 0",
            font=ctk.CTkFont(size=13),
            text_color="#1D9E75"     # Green Color
        )
        self.lbl_correct.grid(row=0, column=1,pady=8)

        # Incorrect count label
        self.lbl_incorrect = ctk.CTkLabel(
            self.frame_stats,
            text="Incorrect: 0",
            font=ctk.CTkFont(size=13),
            text_color="#D85A30"       # Red Color
        )
        self.lbl_incorrect.grid(row=0, column=2, pady=8)

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
        # ---Question Label ---
        self.lbl_q_prompt = ctk.CTkLabel(
            self.tab_add,
            text="Question",
            font=ctk.CTkFont(size=13, weight="bold")
        )
        self.lbl_q_prompt.grid(
            row=0, column=0,
            padx=20, pady=(20,5),
            sticky="w"
        )

        # Question Entry Box
        self.entry_question = ctk.CTkEntry(
            self.tab_add,
            placeholder_text="Enter your question:... ",
            height=40
        )
        self.entry_question.grid(
            row=1, column=0,
            padx=20, pady=(0,10),
            sticky="ew"
        )

        # --- Answer Label ---
        self.lbl_a_prompt = ctk.CTkLabel(
            self.tab_add,
            text="Answer",
            font=ctk.CTkFont(size=13, weight="bold")
        )
        self.lbl_a_prompt.grid(
            row=2, column=0, 
            padx=20, pady=(10,5),
            sticky="w"
        )
        
        # Answer Entry Box
        self.textbox_answer = ctk.CTkTextbox(
            self.tab_add,
            height=120
        )
        self.textbox_answer.grid(
            row=3, column=0,
            padx=20, pady=(0,10),
            sticky="ew"
        )

        # Add Card Button
        self.btn_add_card = ctk.CTkButton(
            self.tab_add,
            text="Add Flashcard",
            command=self._add_card
        )
        self.btn_add_card.grid(
            row=4, column=0,
            padx=20, pady=(5,10),
            sticky="ew"
        )

        # Delete Card Section
        ctk.CTkFrame(
            self.tab_add, fg_color="gray"
        ).grid(
            row=5, column=0, 
            padx=20, pady=15,
            sticky="ew"
        )
        self.lbl_delete_prompt = ctk.CTkLabel(
            self.tab_add, 
            text="Delete a card by index",
            font=ctk.CTkFont(size=13, weight="bold")
        )
        self.lbl_delete_prompt.grid(
            row=6,column=0,
            padx=20, pady=(0,5),
            sticky="w"
        )

        # --- Delete row -entry + button side by side ---
        self.frame_delete = ctk.CTkFrame(self.tab_add, fg_color="transparent")
        self.frame_delete.grid(
            row=7, column=0, 
            padx=20, pady=(0,20),
            sticky="ew"
        )
        self.frame_delete.grid_columnconfigure(0, weight=1)

        # Single line entry for the card index to delete
        self.entry_delete_index = ctk.CTkEntry(
            self.frame_delete,
            placeholder_text="Card index e.g. 0, 1, 2 ...",
            height=40
        )
        self.entry_delete_index.grid(
            row=0, column=0,
            padx=(0,10), sticky="ew"
        )

        # Delete button 
        self.btn_delete_card = ctk.CTkButton(
            self.frame_delete,
            text="Delete",
            fg_color="#D85A30",
            hover_color="#993C1D",
            width=80, 
            command=self._delete_card
        )
        self.btn_delete_card.grid(
            row=0, column=1,
        )

    def _build_stats_tab(self):
        # Title Label
        self.lbl_stats_title = ctk.CTkLabel(
            self.tab_stats,
            text="Your Progress",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        self.lbl_stats_title.grid(
            row=0, column=0,
            padx=20, pady=(20,5),
            sticky="w"
        )

        # Stats Card Frame
        self.frame_stats_cards = ctk.CTkFrame(self.tab_stats, fg_color="transparent")
        self.frame_stats_cards.grid(
            row=1, column=0, 
            padx=20, pady=(20,5),
            sticky="ew"
        )
        self.frame_stats_cards.grid_columnconfigure((0,1,2), weight=1)

        # Total Cards Stat
        self.frame_stat_total = ctk.CTkFrame(self.frame_stats_cards)
        self.frame_stat_total.grid(row=0, column=0, padx=(0, 5), sticky="ew")
        self.frame_stat_total.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            self.frame_stat_total,
            text="Total Cards",
            font=ctk.CTkFont(size=11),
            text_color="gray"
        ).grid(row=0, column=0, pady=(10,2))


        self.lbl_stat_total = ctk.CTkLabel(
            self.frame_stat_total,
            text="0",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        self.lbl_stat_total.grid(row=1, column=0, pady=(0, 10))

        # Correct stat - Green
        self.frame_stat_correct = ctk.CTkFrame(self.frame_stats_cards)
        self.frame_stat_correct.grid(row=0, column=1, padx=5, sticky="ew")
        self.frame_stat_correct.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            self.frame_stat_correct,
            text="Correct",
            font=ctk.CTkFont(size=11),
            text_color="gray"
        ).grid(row=0, column=0, pady=(10, 2))

        self.lbl_stat_correct = ctk.CTkLabel(
            self.frame_stat_correct, 
            text="0",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color="#1D9E75"
        )
        self.lbl_stat_correct.grid(row=1, column=0, pady=(0, 10))

        # Incorrect stat - red
        self.frame_stat_incorrect = ctk.CTkFrame(self.frame_stats_cards)
        self.frame_stat_incorrect.grid(row=0, column=2, padx=(5, 0), sticky="ew")
        self.frame_stat_incorrect.grid_columnconfigure(0, weight=1)
        
        ctk.CTkLabel(
            self.frame_stat_incorrect,
            text="Incorrect",
            font=ctk.CTkFont(size=11),
            text_color="gray"
        ).grid(row=0, column=0, pady=(10,2))

        self.lbl_stat_incorrect = ctk.CTkLabel(
            self.frame_stat_incorrect, 
            text="0", 
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color="#D85A30",
        )
        self.lbl_stat_incorrect.grid(row=1, column=0, pady=(0, 10))

        # Accuracy Bar
        self.lbl_accuracy_title = ctk.CTkLabel(
            self.tab_stats,
            text="Accuracy",
            font=ctk.CTkFont(size=13, weight="bold")
        )
        self.lbl_accuracy_title.grid(
            row=2, column=0,
            padx=20, pady=(15, 5),
            sticky="w"
        )

        # Progress Bar
        self.accuracy_bar = ctk.CTkProgressBar(self.tab_stats)
        self.accuracy_bar.set(0)
        self.accuracy_bar.grid(
            row=3, column=0,
            padx=20, pady=(0, 5), 
            sticky="ew"
        )

        # Accuracy Percentage Label
        self.lbl_accuracy_pct = ctk.CTkLabel(
            self.tab_stats, 
            text="0% accuracy",
            font=ctk.CTkFont(size=13),
            text_color="gray"
        )
        self.lbl_accuracy_pct.grid(
            row=4, column=0, 
            padx=20, pady=(0, 15), 
            sticky="w"
        )

        # Card List
        self.lbl_card_list_title = ctk.CTkLabel(
            self.tab_stats,
            text="Card Breakdown",
            font=ctk.CTkFont(size=13, weight="bold")
        )
        self.lbl_card_list_title.grid(
            row=5, column=0, 
            padx=20, pady=(5,5),
            sticky="w"
        )

        # Scrollable Frame
        self.frame_card_list = ctk.CTkScrollableFrame(self.tab_stats)
        self.frame_card_list.grid(
            row=6, column=0,
            padx=20, pady=(0, 20), 
            sticky="nsew"
       )
        self.frame_card_list.grid_columnconfigure(0, weight=1)

        # Expand row 6 to fill remaining space
        self.tab_stats.grid_rowconfigure(6, weight=1)

    def _show_quiz(self):
        # display current flashcard question
        pass

    def _reveal_answer(self):
        # reveal the answer
        if not self.deck.cards:
            return
        
        # Get the currecnt card using index
        card = self.deck.cards[self.current_index]

        # Update the answer label
        self.lbl_answer.configure(text=card.answer)
        self.answer_visible = True        

    def _mark_correct(self):
        # mark card correct, move to next
        if not self.deck.cards or not self.answer_visible:
            return                     # do nothing if answer not reviewed yet
        
        card = self.deck.cards[self.current_index]
        card.mark_correct()            # Update the cards score
        self._next_card()              # Move to the next card

    def _mark_incorrect(self):
        if not self.deck.cards or not self.answer_visible:
            return
        
        card = self.deck.cards[self.current_index]
        card.mark_incorrect()
        self._next_card()

    def _next_card(self):
        # Move the card to the next, loop if at the end of the deck
        self.current_index = (self.current_index + 1) % len(self.deck.cards)
        self.answer_visible = False      # Hide Answer for the next card
        self._update_quiz()              # Refrest the UI
        self._update_stats()

    def _update_quiz(self):
        # called whenever to refresh the quiz display
        if not self.deck.cards:
            return
        
        card = self.deck.cards[self.current_index]
        total = len(self.deck.cards)

        # Count correct and incorrect cards
        correct = sum(c.correct for c in self.deck.cards)
        attempted = sum(c.attempted for c in self.deck.cards)
        incorrect = attempted - correct

        # Update all the labels with fresh data
        self.lbl_progress.configure(text=f"Card {self.current_index + 1} of {total}")
        self.lbl_question.configure(text=card.question)
        self.lbl_answer.configure(text="")          # Hide answer in new card
        self.lbl_total.configure(text=f"Total: {total}")
        self.lbl_correct.configure(text=f"Correct: {correct}")
        self.lbl_incorrect.configure(text=f"Incorrect: {incorrect}")
        self.lbl_card_count.configure(text=f"{total} cards")

    def _update_stats(self):
        # To refresh the stats tab
        total = len(self.deck.cards)
        correct = sum(c.correct for c in self.deck.cards)
        attempted = sum(c.attempted for c in self.deck.cards)
        incorrect = attempted - correct

        # Update the stat number labels
        self.lbl_stat_total.configure(text=str(total))
        self.lbl_stat_correct.configure(text=str(correct))
        self.lbl_stat_incorrect.configure(text=str(incorrect))

        # Calculate and display accuracy
        accuracy = (correct / attempted) if attempted > 0 else 0
        self.accuracy_bar.set(accuracy)
        self.lbl_accuracy_pct.configure(text=f"{int(accuracy * 100)}% accuracy")

        # Rebuild the card breakdown list
        for widget in self.frame_card_list.winfo_children():
            widget.destroy()

        # Create a row for each card
        for i, card in enumerate(self.deck.cards):
            row_frame = ctk.CTkFrame(self.frame_card_list, fg_color="transparent")
            row_frame.grid(row=i, column=0, pady=4, sticky="ew")
            row_frame.grid_columnconfigure(0, weight=1)

            # Question text
            question_preview = card.question[:45] + "..." \
                    if len(card.question) > 45 else card.question
            
            ctk.CTkLabel(
                row_frame, 
                text=question_preview,
                font=ctk.CTkFont(size=12), 
                anchor="w"
            ).grid(row=0, column=0, sticky="w")

            ctk.CTkLabel(
                row_frame, 
                text=card.get_stats(), 
                font=ctk.CTkFont(size=11), 
                text_color="gray",
                anchor="w"
            ).grid(row=1, column=0, sticky="w")

    def _add_card(self):
        # Read the question from the entry field
        question = self.entry_question.get().strip()
        
        # Read the answer from the textbook
        answer = self.textbox_answer.get("1.0", "end").strip()

        # Validate 
        if not question or not answer:
            print("Please fill in both fields!")
            return
        
        # Add the card to deck
        self.deck.add_card(question, answer)

        # Save to file
        self.deck.save()

        # Clear the entry fields
        self.entry_question.delete(0, "end")
        self.textbox_answer.delete("1.0","end")

        # Refresh quiz display
        self._update_quiz()
        self._update_stats()
        print(f"Card added! Total Cards : {len(self.deck.cards)}")

    def _delete_card(self):
        # read the index from the entry field
        index_str = self.entry_delete_index.get().strip()

        # validate
        if not index_str.isdigit():
            print("Please enter a valid index number!")
            return
        
        index= int(index_str)

        result = self._deck.delete_card(index)
        print(result)

        self.deck.save()
        self._update_quiz()
        self._update_stats()

        self.entry_delete_index.delete(0, "end")

    def _save_and_exit(self):
        self.deck.save()
        self.destroy()

if __name__ == "__main__":
    app = FlipwiseApp()
    app.mainloop()