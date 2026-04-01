import numpy as np
import pandas as pd
import torch

df = pd.read_json("hf://datasets/DanFosing/public-domain-poetry/poems.json") # author,text,title

chars = sorted(list(set(df.text.str.cat()))) # unique characters in the text
vocab_size = len(chars)

def tokenize(idx): # takes in some input sequence(s), tokenizes each character; and includes their posn. encoding, too
    
    return