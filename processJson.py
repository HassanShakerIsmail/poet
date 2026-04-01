# input files are jsons from https://huggingface.co/datasets/DanFosing/public-domain-poetry 
# these jsons have author, text, title key value pairs - this code combines them into a processed output file to 
# ultimately be used to train the transformer. the code generalizes pretty straightforwardly

# uncomment below if you need to pull the data set again (or replace with whatever)
# pdf = pd.read_json("hf://datasets/DanFosing/public-domain-poetry/poems.json") # author,text,title
# pdf.to_json("rawInput.json", orient="records", indent=4)


import pandas as pd

df = pd.read_json("rawInput.json")

SEPARATOR = "---------------------"

# process each poem into formatted string
def format_poem(row):
    author = row["Author"]
    title = row["Title"]
    text = row["text"]
    return f"{author}\n{title}:\n\n{text}\n\n{SEPARATOR}"

# combine all poems
output_text = "\n".join(df.apply(format_poem, axis=1))

# write to input.txt
with open("input.txt", "w", encoding="utf-8") as f:
    f.write(output_text)

print(f"Processed {len(df)} poems to input.txt")
print(f"Total characters: {len(output_text)}")

