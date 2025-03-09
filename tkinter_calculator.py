from tkinter import *
import math
from tkinter import simpledialog, messagebox
import numpy as np
import statistics as stats

# -------------------- Global Variables --------------------
calc_operator = ""
text_input = None
E = '*10**'  # Exponential operator shortcut

# -------------------- Basic Operation Functions --------------------
def button_click(char):
    global calc_operator
    calc_operator += str(char)
    text_input.set(calc_operator)

def button_clear_all():
    global calc_operator
    calc_operator = ""
    text_input.set("")

def button_delete():
    global calc_operator
    calc_operator = calc_operator[:-1]
    text_input.set(calc_operator)

def button_equal():
    global calc_operator
    # Pull the latest text from the Entry widget
    calc_operator = text_input.get()
    try:
        result = str(eval(calc_operator))
    except Exception:
        result = "ERROR"
    text_input.set(result)
    calc_operator = result


def sign_change():
    global calc_operator
    if calc_operator.startswith('-'):
        calc_operator = calc_operator[1:]
    else:
        calc_operator = '-' + calc_operator
    text_input.set(calc_operator)

def percent():
    global calc_operator
    try:
        result = str(eval(calc_operator + '/100'))
    except Exception:
        result = "ERROR"
    calc_operator = result
    text_input.set(result)

# -------------------- Mathematical Functions --------------------
def factorial(n):
    return 1 if n in (0, 1) else n * factorial(n - 1)

def fact_func():
    global calc_operator
    try:
        result = str(factorial(int(calc_operator)))
    except Exception:
        result = "ERROR"
    calc_operator = result
    text_input.set(result)

def square_root():
    global calc_operator
    try:
        if float(calc_operator) >= 0:
            result = str(eval(calc_operator + '**(1/2)'))
        else:
            result = "ERROR"
    except Exception:
        result = "ERROR"
    calc_operator = result
    text_input.set(result)

def third_root():
    global calc_operator
    try:
        if float(calc_operator) >= 0:
            result = str(eval(calc_operator + '**(1/3)'))
        else:
            result = "ERROR"
    except Exception:
        result = "ERROR"
    calc_operator = result
    text_input.set(result)

def exp_ex():
    """Computes e^x using the current value."""
    global calc_operator
    try:
        result = str(math.exp(float(calc_operator)))
    except Exception:
        result = "ERROR"
    calc_operator = result
    text_input.set(result)

def exp_10x():
    """Computes 10^x using the current value."""
    global calc_operator
    try:
        result = str(10 ** float(calc_operator))
    except Exception:
        result = "ERROR"
    calc_operator = result
    text_input.set(result)

# -------------------- Trigonometric Functions --------------------
def trig_sin():
    global calc_operator
    try:
        result = str(math.sin(math.radians(float(calc_operator))))
    except Exception:
        result = "ERROR"
    calc_operator = result
    text_input.set(result)

def trig_cos():
    global calc_operator
    try:
        result = str(math.cos(math.radians(float(calc_operator))))
    except Exception:
        result = "ERROR"
    calc_operator = result
    text_input.set(result)

def trig_tan():
    global calc_operator
    try:
        result = str(math.tan(math.radians(float(calc_operator))))
    except Exception:
        result = "ERROR"
    calc_operator = result
    text_input.set(result)

def trig_cot():
    global calc_operator
    try:
        result = str(1 / math.tan(math.radians(float(calc_operator))))
    except Exception:
        result = "ERROR"
    calc_operator = result
    text_input.set(result)

def trig_sinh():
    global calc_operator
    try:
        result = str(math.sinh(float(calc_operator)))
    except Exception:
        result = "ERROR"
    calc_operator = result
    text_input.set(result)

def trig_cosh():
    global calc_operator
    try:
        result = str(math.cosh(float(calc_operator)))
    except Exception:
        result = "ERROR"
    calc_operator = result
    text_input.set(result)

def trig_tanh():
    global calc_operator
    try:
        result = str(math.tanh(float(calc_operator)))
    except Exception:
        result = "ERROR"
    calc_operator = result
    text_input.set(result)

# -------------------- Conversion Functions --------------------
def to_radians():
    global calc_operator
    try:
        result = str(math.radians(float(calc_operator)))
        text_input.set(result + " rad")
        calc_operator = result
    except Exception:
        text_input.set("ERROR")

def to_degrees():
    global calc_operator
    try:
        result = str(math.degrees(float(calc_operator)))
        text_input.set(result + "°")
        calc_operator = result
    except Exception:
        text_input.set("ERROR")

# -------------------- Statistical Functions --------------------
def get_numbers():
    user_input = simpledialog.askstring("Input", "Enter numbers separated by commas:")
    if user_input:
        try:
            return list(map(float, user_input.split(',')))
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Enter numbers separated by commas.")
    return None

def calc_mean():
    numbers = get_numbers()
    if numbers:
        text_input.set(stats.mean(numbers))

def calc_median():
    numbers = get_numbers()
    if numbers:
        text_input.set(stats.median(numbers))

def calc_mode():
    numbers = get_numbers()
    if numbers:
        try:
            text_input.set(stats.mode(numbers))
        except stats.StatisticsError:
            text_input.set("No unique mode.")

def calc_range():
    numbers = get_numbers()
    if numbers:
        text_input.set(max(numbers) - min(numbers))

def calc_variance():
    numbers = get_numbers()
    if numbers:
        if len(numbers) > 1:
            text_input.set(stats.variance(numbers))
        else:
            text_input.set("Variance requires at least two numbers.")

def calc_stdev():
    numbers = get_numbers()
    if numbers:
        if len(numbers) > 1:
            text_input.set(stats.stdev(numbers))
        else:
            text_input.set("Std deviation requires at least two numbers.")

# -------------------- Combinatorial & Logarithm Functions --------------------
def log_base():
    numbers = get_numbers()
    if numbers and len(numbers) == 2:
        base = numbers[1]
        if base > 0 and base != 1:
            result = math.log(numbers[0], base)
            text_input.set(f"Log base {base}: {result}")
        else:
            text_input.set("Invalid base (must be >0 and ≠1)")

def calc_nCr():
    numbers = get_numbers()
    if numbers and len(numbers) == 2:
        n, r = numbers
        if 0 <= r <= n:
            text_input.set(f"{n}C{r}: {math.comb(int(n), int(r))}")
        else:
            text_input.set("Invalid values (0 ≤ r ≤ n)")

def calc_nPr():
    numbers = get_numbers()
    if numbers and len(numbers) == 2:
        n, r = numbers
        if 0 <= r <= n:
            text_input.set(f"{n}P{r}: {math.perm(int(n), int(r))}")
        else:
            text_input.set("Invalid values (0 ≤ r ≤ n)")

# -------------------- New Base Conversion Functions --------------------
def dec_to_bin():
    """Convert the current decimal value in calc_operator to binary."""
    global calc_operator
    try:
        val = int(float(calc_operator))  # Handle floats by truncating
        result = bin(val)  # e.g. '0b1010'
        text_input.set(result)
        calc_operator = result
    except:
        text_input.set("ERROR")

def dec_to_oct():
    """Convert the current decimal value in calc_operator to octal."""
    global calc_operator
    try:
        val = int(float(calc_operator))
        result = oct(val)  # e.g. '0o12'
        text_input.set(result)
        calc_operator = result
    except:
        text_input.set("ERROR")

def dec_to_hex():
    """Convert the current decimal value in calc_operator to hexadecimal."""
    global calc_operator
    try:
        val = int(float(calc_operator))
        result = hex(val)  # e.g. '0xa'
        text_input.set(result)
        calc_operator = result
    except:
        text_input.set("ERROR")

def bin_to_dec():
    """Convert the current binary value in calc_operator to decimal."""
    global calc_operator
    try:
        val = int(calc_operator, 2)
        text_input.set(str(val))
        calc_operator = str(val)
    except:
        text_input.set("ERROR")

def oct_to_dec():
    """Convert the current octal value in calc_operator to decimal."""
    global calc_operator
    try:
        val = int(calc_operator, 8)
        text_input.set(str(val))
        calc_operator = str(val)
    except:
        text_input.set("ERROR")

def hex_to_dec():
    """Convert the current hexadecimal value in calc_operator to decimal."""
    global calc_operator
    try:
        val = int(calc_operator, 16)
        text_input.set(str(val))
        calc_operator = str(val)
    except:
        text_input.set("ERROR")

# -------------------- Tkinter Setup --------------------
tk_calc = Tk()
tk_calc.configure(bg="#293C4A", bd=10)
tk_calc.title("Scientific Calculator")

text_input = StringVar()
text_display = Entry(
    tk_calc, font=('sans-serif', 20, 'bold'),
    textvariable=text_input, bd=5, insertwidth=5,
    bg='#BBB', justify='right'
)
text_display.grid(columnspan=6, padx=10, pady=15)

# Bind the Enter key to your "button_equal" function
text_display.bind("<Return>", lambda event: button_equal())


# Button style parameters
button_params = {'bd': 5, 'fg': '#BBB', 'bg': '#3C3636', 'font': ('sans-serif', 20, 'bold')}
button_params_main = {'bd': 5, 'fg': '#000', 'bg': '#BBB', 'font': ('sans-serif', 20, 'bold')}

# -------------------- Button Layout --------------------
# Row 1: Basic operations & math
Button(tk_calc, **button_params, text='abs', command=lambda: button_click('abs(')).grid(row=1, column=0, sticky="nsew")
Button(tk_calc, **button_params, text='mod', command=lambda: button_click('%')).grid(row=1, column=1, sticky="nsew")
Button(tk_calc, **button_params, text='div', command=lambda: button_click('//')).grid(row=1, column=2, sticky="nsew")
Button(tk_calc, **button_params, text='x!', command=fact_func).grid(row=1, column=3, sticky="nsew")
Button(tk_calc, **button_params, text='e', command=lambda: button_click(str(math.exp(1)))).grid(row=1, column=4, sticky="nsew")

# Row 2: Standard Trigonometric functions & π
Button(tk_calc, **button_params, text='sin', command=trig_sin).grid(row=2, column=0, sticky="nsew")
Button(tk_calc, **button_params, text='cos', command=trig_cos).grid(row=2, column=1, sticky="nsew")
Button(tk_calc, **button_params, text='tan', command=trig_tan).grid(row=2, column=2, sticky="nsew")
Button(tk_calc, **button_params, text='cot', command=trig_cot).grid(row=2, column=3, sticky="nsew")
Button(tk_calc, **button_params, text='π', command=lambda: button_click(str(math.pi))).grid(row=2, column=4, sticky="nsew")

# Row 3: Exponentiation & Powers
Button(tk_calc, **button_params, text='x\u00B2', command=lambda: button_click('**2')).grid(row=3, column=0, sticky="nsew")
Button(tk_calc, **button_params, text='x\u00B3', command=lambda: button_click('**3')).grid(row=3, column=1, sticky="nsew")
Button(tk_calc, **button_params, text='x^n', command=lambda: button_click('**')).grid(row=3, column=2, sticky="nsew")
Button(tk_calc, **button_params, text='x\u207b\xb9', command=lambda: button_click('**(-1)')).grid(row=3, column=3, sticky="nsew")
custom_button_params_10x = button_params.copy()
custom_button_params_10x['font'] = ('sans-serif', 15, 'bold')
Button(tk_calc, **custom_button_params_10x, text='10^x', command=lambda: button_click('10**')).grid(row=3, column=4, sticky="nsew")

# Row 4: Roots & Logarithms
Button(tk_calc, **button_params, text='\u00B2\u221A', command=square_root).grid(row=4, column=0, sticky="nsew")
Button(tk_calc, **button_params, text='\u00B3\u221A', command=third_root).grid(row=4, column=1, sticky="nsew")
Button(tk_calc, **button_params, text='\u221A', command=lambda: button_click('**(1/')).grid(row=4, column=2, sticky="nsew")
custom_button_params_log = button_params.copy()
custom_button_params_log['font'] = ('sans-serif', 16, 'bold')
Button(tk_calc, **custom_button_params_log, text='log\u2081\u2080', command=lambda: button_click('log(')).grid(row=4, column=3, sticky="nsew")
Button(tk_calc, **button_params, text='ln', command=lambda: button_click('ln(')).grid(row=4, column=4, sticky="nsew")

# Row 5: Parentheses, Sign, Percent, e^x
Button(tk_calc, **button_params, text='(', command=lambda: button_click('(')).grid(row=5, column=0, sticky="nsew")
Button(tk_calc, **button_params, text=')', command=lambda: button_click(')')).grid(row=5, column=1, sticky="nsew")
Button(tk_calc, **button_params, text='\u00B1', command=sign_change).grid(row=5, column=2, sticky="nsew")
Button(tk_calc, **button_params, text='%', command=percent).grid(row=5, column=3, sticky="nsew")
Button(tk_calc, **button_params, text='e^x', command=lambda: button_click('e(')).grid(row=5, column=4, sticky="nsew")

# Row 6: Digits 7-9 and delete buttons
for (txt, col) in [('7', 0), ('8', 1), ('9', 2)]:
    Button(tk_calc, **button_params_main, text=txt, command=lambda t=txt: button_click(t)).grid(row=6, column=col, sticky="nsew")
Button(tk_calc, bd=5, fg='#000', font=('sans-serif', 20, 'bold'),
       text='DEL', command=button_delete, bg='#db701f').grid(row=6, column=3, sticky="nsew")
Button(tk_calc, bd=5, fg='#000', font=('sans-serif', 20, 'bold'),
       text='AC', command=button_clear_all, bg='#db701f').grid(row=6, column=4, sticky="nsew")

# Row 7: Digits 4-6 and multiplication/division
for (txt, col) in [('4', 0), ('5', 1), ('6', 2)]:
    Button(tk_calc, **button_params_main, text=txt, command=lambda t=txt: button_click(t)).grid(row=7, column=col, sticky="nsew")
Button(tk_calc, **button_params_main, text='*', command=lambda: button_click('*')).grid(row=7, column=3, sticky="nsew")
Button(tk_calc, **button_params_main, text='/', command=lambda: button_click('/')).grid(row=7, column=4, sticky="nsew")

# Row 8: Digits 1-3 and addition/subtraction
for (txt, col) in [('1', 0), ('2', 1), ('3', 2)]:
    Button(tk_calc, **button_params_main, text=txt, command=lambda t=txt: button_click(t)).grid(row=8, column=col, sticky="nsew")
Button(tk_calc, **button_params_main, text='+', command=lambda: button_click('+')).grid(row=8, column=3, sticky="nsew")
Button(tk_calc, **button_params_main, text='-', command=lambda: button_click('-')).grid(row=8, column=4, sticky="nsew")

# Row 9: Digit 0, decimal, EXP, and equals
Button(tk_calc, **button_params_main, text='0', command=lambda: button_click('0')).grid(row=9, column=0, sticky="nsew")
Button(tk_calc, **button_params_main, text='.', command=lambda: button_click('.')).grid(row=9, column=1, sticky="nsew")
custom_button_params_main_exp = button_params_main.copy()
custom_button_params_main_exp['font'] = ('sans-serif', 16, 'bold')
Button(tk_calc, **custom_button_params_main_exp, text='EXP', command=lambda: button_click(E)).grid(row=9, column=2, sticky="nsew")
Button(tk_calc, **button_params_main, text='=', command=button_equal).grid(row=9, column=3, columnspan=2, sticky="nsew")

# -------------------- Menus --------------------
menu_bar = Menu(tk_calc)

# Statistics Menu (includes statistical, logarithmic, and combinatorial functions)
stats_menu = Menu(menu_bar, tearoff=0)
stats_menu.add_command(label="Mean", command=calc_mean)
stats_menu.add_command(label="Median", command=calc_median)
stats_menu.add_command(label="Mode", command=calc_mode)
stats_menu.add_command(label="Range", command=calc_range)
stats_menu.add_command(label="Variance", command=calc_variance)
stats_menu.add_command(label="Standard Deviation", command=calc_stdev)
stats_menu.add_command(label="Log Base", command=log_base)
stats_menu.add_command(label="nCr (Combinations)", command=calc_nCr)
stats_menu.add_command(label="nPr (Permutations)", command=calc_nPr)
menu_bar.add_cascade(label="Statistics", menu=stats_menu)

# Trigonometry Menu (includes standard, hyperbolic, and conversion functions)
trig_menu = Menu(menu_bar, tearoff=0)
trig_menu.add_command(label="Sin", command=trig_sin)
trig_menu.add_command(label="Cos", command=trig_cos)
trig_menu.add_command(label="Tan", command=trig_tan)
trig_menu.add_command(label="Cot", command=trig_cot)
trig_menu.add_command(label="Sinh", command=trig_sinh)
trig_menu.add_command(label="Cosh", command=trig_cosh)
trig_menu.add_command(label="Tanh", command=trig_tanh)
trig_menu.add_separator()
trig_menu.add_command(label="Convert to Radians", command=to_radians)
trig_menu.add_command(label="Convert to Degrees", command=to_degrees)
menu_bar.add_cascade(label="Trigonometry", menu=trig_menu)

# Exponential Menu (still includes e^x, 10^x)
exp_menu = Menu(menu_bar, tearoff=0)
exp_menu.add_command(label="e^x", command=exp_ex)
exp_menu.add_command(label="10^x", command=exp_10x)
menu_bar.add_cascade(label="Exponential", menu=exp_menu)

# -------------------- New "Conversions" Menu --------------------
conv_menu = Menu(menu_bar, tearoff=0)
conv_menu.add_command(label="Dec → Bin", command=dec_to_bin)
conv_menu.add_command(label="Dec → Oct", command=dec_to_oct)
conv_menu.add_command(label="Dec → Hex", command=dec_to_hex)
conv_menu.add_separator()
conv_menu.add_command(label="Bin → Dec", command=bin_to_dec)
conv_menu.add_command(label="Oct → Dec", command=oct_to_dec)
conv_menu.add_command(label="Hex → Dec", command=hex_to_dec)
menu_bar.add_cascade(label="Conversions", menu=conv_menu)

tk_calc.config(menu=menu_bar)
tk_calc.mainloop()
