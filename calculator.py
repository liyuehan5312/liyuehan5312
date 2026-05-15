 # Display
    self.display = tk.Entry(root, font=("Arial", 20), justify="right")
    self.display.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

    # Mode for degrees/radians
    self.mode = "degrees"  # or "radians"

    # Buttons
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('C', 1, 4),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('(', 2, 4),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), (')', 3, 4),
        ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3), ('DEL', 4, 4),
        ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('log', 5, 3), ('ln', 5, 4),
        ('asin', 6, 0), ('acos', 6, 1), ('atan', 6, 2), ('sqrt', 6, 3), ('^', 6, 4),
        ('pi', 7, 0), ('e', 7, 1), ('exp', 7, 2), ('mod', 7, 3), ('DEG/RAD', 7, 4)
    ]

    for (text, row, col) in buttons:
        button = tk.Button(root, text=text, font=("Arial", 14), command=lambda t=text: self.on_button_click(t))
        button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    # Configure grid weights
    for i in range(8):
        root.grid_rowconfigure(i, weight=1)
    for j in range(5):
        root.grid_columnconfigure(j, weight=1)

def on_button_click(self, text):
    if text == '=':
        try:
            expression = self.display.get()
            result = self.evaluate_expression(expression)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")
    elif text == 'C':
        self.display.delete(0, tk.END)
    elif text == 'DEL':
        current = self.display.get()
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, current[:-1])
    elif text == 'DEG/RAD':
        self.mode = "radians" if self.mode == "degrees" else "degrees"
    else:
        self.display.insert(tk.END, text)

def evaluate_expression(self, expression):
    # Replace functions and constants
    expression = expression.replace('pi', str(math.pi))
    expression = expression.replace('e', str(math.e))

    # Trigonometric functions
    if self.mode == "degrees":
        expression = expression.replace('sin(', 'math.sin(math.radians(')
        expression = expression.replace('cos(', 'math.cos(math.radians(')
        expression = expression.replace('tan(', 'math.tan(math.radians(')
        expression = expression.replace('asin(', 'math.degrees(math.asin(')
        expression = expression.replace('acos(', 'math.degrees(math.acos(')
        expression = expression.replace('atan(', 'math.degrees(math.atan(')
    else:
        expression = expression.replace('sin(', 'math.sin(')
        expression = expression.replace('cos(', 'math.cos(')
        expression = expression.replace('tan(', 'math.tan(')
        expression = expression.replace('asin(', 'math.asin(')
        expression = expression.replace('acos(', 'math.acos(')
        expression = expression.replace('atan(', 'math.atan(')

    # Other functions
    expression = expression.replace('log(', 'math.log10(')
    expression = expression.replace('ln(', 'math.log(')
    expression = expression.replace('sqrt(', 'math.sqrt(')
    expression = expression.replace('exp(', 'math.exp(')
    expression = expression.replace('^', '**')
    expression = expression.replace('mod', '%')

    # Close parentheses for trig functions in degrees mode
    if self.mode == "degrees":
        expression = expression.replace(')', '))')

    # Evaluate
    return eval(expression)
