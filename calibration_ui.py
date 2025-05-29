import tkinter as tk

class GestureCalibrationUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("GhostTouch Calibration")

        self.click_threshold = tk.IntVar(value=40)
        self.scroll_threshold = tk.IntVar(value=20)
        self.click_cooldown = tk.DoubleVar(value=0.8)

        self._create_slider("Click Sensitivity (pinch distance)", self.click_threshold, 10, 100)
        self._create_slider("Scroll Sensitivity (vertical movement)", self.scroll_threshold, 5, 50)
        self._create_slider("Click Cooldown (seconds)", self.click_cooldown, 0.1, 3.0, is_float=True)

        tk.Button(self.window, text="Start GhostTouch", command=self._on_close).pack(pady=10)

    def _create_slider(self, label, variable, min_val, max_val, is_float=False):
        tk.Label(self.window, text=label).pack()
        scale = tk.Scale(self.window, from_=min_val, to=max_val, orient="horizontal",
                         resolution=0.1 if is_float else 1, variable=variable)
        scale.pack()

    def run(self):
        self.window.protocol("WM_DELETE_WINDOW", self._on_close)
        self.window.mainloop()

    def _on_close(self):
        self.window.quit()
        self.window.destroy()

    def get_settings(self):
        return {
            "click_threshold": self.click_threshold.get(),
            "scroll_threshold": self.scroll_threshold.get(),
            "click_cooldown": self.click_cooldown.get()
        }
