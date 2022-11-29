
import math 
import random

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def generate_triples():
    #pick a random odd square number
    n = random.choice([x for x in range(9, 100) if x % 2 == 1 and math.isqrt(x) ** 2 == x])

    #determine the odd integers up to n and sum them to make var
    var = sum([x for x in range(1, n + 1) if x % 2 == 1])
    
    #return the square roots of the three numbers as a pythagorean triple
    return render_template("index.html", x=n, a=math.sqrt(n), b=math.sqrt(var), c=math.sqrt(n + var))
