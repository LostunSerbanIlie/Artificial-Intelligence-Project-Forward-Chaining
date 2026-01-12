import tkinter as tk
from tkinter import ttk, messagebox
from date import get_date_inegalitati, get_date_multimi
from inferenta import forward_chaining

class InferenceGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Inference Engine - Forward Chaining")
        self.geometry("900x650")
        
        # paleta de culori
        bg_color = "#2b2b2b"       # dark gray
        fg_color = "#ffffff"       # alb text
        btn_bg = "#404040"         # light gray butoane
        text_bg = "#1e1e1e"        # dark background text box

        self.configure(bg=bg_color)
        
        self.style = ttk.Style(self)
        self.style.theme_use('clam') # tema de baza
        
        # butoane
        self.style.configure(
            'TButton', 
            font=('Segoe UI', 10, 'bold'),
            padding= 6,                        
            relief="flat", 
            borderwidth=0, 
            background=btn_bg, 
            foreground=fg_color
        )
        self.style.map('TButton', background=[('active', "#000000")]) # culoare la apasare

        self.style.configure(
            'TRadiobutton', 
            font=('Segoe UI', 11), 
            background=bg_color, 
            foreground=fg_color,
            indicatorcolor=bg_color,
            indicatorrelief="flat"
        )

        # stil labeluri si frame
        self.style.configure('TLabel', font=('Segoe UI', 12), background=bg_color, foreground=fg_color)
        self.style.configure('TFrame', background=bg_color)
        self.style.configure('TRadiobutton', font=('Segoe UI', 11), background=bg_color, foreground=fg_color)
        self.style.map('TRadiobutton', background=[('active', "#000000")]) # negru pentru selectat

        self.create_widgets(bg_color, fg_color, text_bg)

    def create_widgets(self, bg_color, fg_color, text_bg):
        # Title
        title = ttk.Label(self, text="Select Application Type", font=("Segoe UI", 16, "bold"), background=bg_color, foreground=fg_color)
        title.pack(pady=20)

        # Button Frame
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=5)

        self.app_type = tk.StringVar()
        self.app_type.set("inegalitati") # default
        
        # aplicatiile disponibile
        app_types = [
            ("Tranzitivitate Inegalități", "inegalitati"),
            ("Incluziune Mulțimi", "multimi"),
        ]
        for text, value in app_types:
            b = ttk.Radiobutton(btn_frame, text=text, variable=self.app_type, value=value, style='TRadiobutton')
            b.pack(side=tk.LEFT, padx=18, ipadx=8, ipady=4)

        # butoane run si clear
        btns_action_frame = ttk.Frame(self)
        btns_action_frame.pack(pady=20)

        run_btn = ttk.Button(btns_action_frame, text="Run Inference", command=self.run_inference, style='TButton')
        run_btn.pack(side=tk.LEFT, padx=10, ipadx=5, ipady=2)

        clear_btn = ttk.Button(btns_action_frame, text="Clear", command=self.clear_results, style='TButton')
        clear_btn.pack(side=tk.LEFT, padx=10, ipadx=5, ipady=2)

        # Results label
        results_label = ttk.Label(self, text="Inference Results:", font=("Segoe UI", 14, "bold"), background=bg_color, foreground=fg_color)
        results_label.pack(pady=(10, 5))

        # Results Text Box
        self.results_text = tk.Text(
            self, 
            height=28, 
            width=100, 
            bg=text_bg, 
            fg="#cccccc", 
            font=("Consolas", 12),
            wrap=tk.WORD, 
            borderwidth=0, 
            relief="flat",
            padx=10, pady=10
        )
        self.results_text.pack(padx=20, pady=5)
        self.results_text.config(state=tk.DISABLED)

    def clear_results(self):
        self.results_text.config(state=tk.NORMAL)
        self.results_text.delete(1.0, tk.END)
        self.results_text.config(state=tk.DISABLED)

    def run_inference(self):
        app_type = self.app_type.get()
        try:
            if app_type == "inegalitati":
                reguli, fapte_initiale = get_date_inegalitati()
                titlu = "[Tranzitivitate Inegalități]"
            elif app_type == "multimi":
                reguli, fapte_initiale = get_date_multimi()
                titlu = "[Incluziune Mulțimi]"
            else:
                self.display_results("Nicio aplicație selectată.")
                return

            # Executa inferenta
            fapte_finale = forward_chaining(reguli, fapte_initiale)

            # Formateaza si afiseaza rezultatele
            result = titlu + "\n\n"
            result += "Fapte inițiale:\n"
            for f in fapte_initiale:
                result += f"  - {f}\n"
            result += "\nReguli:\n"
            for r in reguli:
                result += f"  - {r}\n"
            result += "\nFapte deduse (toate):\n"
            for i, fapt in enumerate(fapte_finale, 1):
                status = "(Inițial)" if fapt in fapte_initiale else "--> Dedus"
                result += f"{i}. {fapt} {status}\n"

            self.display_results(result)
        except Exception as e:
            self.display_results(f"Eroare la rularea inferenței:\n{e}")

    def display_results(self, text):
        self.results_text.config(state=tk.NORMAL)
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, text)
        self.results_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    app = InferenceGUI()
    app.mainloop()