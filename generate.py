import json

starters = []
chain = {}

print("Building Markov Chains...")
with open("input.txt", "r") as file:
    for line in file:
        line = line.rstrip() # .lower()
        
        if len(line) == 0:
            continue
        
        line = line.split(" ")
        
        starters.append(line[0])
        prev = ""
        for word in line:
            if prev != "":
                if prev in chain:
                    chain[prev].append(word)
                else:
                    chain[prev] = [word]
             
            prev = word
print(f"  Starter Count: {len(starters)}, Chain Count: {len(chain)}")
print("  [DONE]")

print("Writing Markov Chains To File...")
with open("output.json", "w") as output:
    output.write(json.dumps({
        "starters": starters,
        "chains": chain
    }))
print("  [DONE]")

template = f"""
    <!DOCTYPE html>
    <html>
        <!--
            Code Written By: Trevor Martin
            Treaty of Versailles Articles 1-30 From: https://wwi.lib.byu.edu/index.php/Articles_1_-_30_and_Annex
                Bezhani, Hirgen. "Articles 1 - 30 and Annex." Edited by Richard Hacken and Bkimberl. The World War I 
                    Document Archive, 5 May 2007, wwi.lib.byu.edu/index.php/Articles_1_-_30_and_Annex. Accessed 13 
                    Mar. 2022. 
        
        -->
        <head>
            <title>Blabber - APWH Dadaism Project</title>
            <style>
                /* https://coolors.co/6da34d-56445d-548687-8fbc94-c5e99b */
                
                html, body {{
                    padding: 10px;
                    background-color: #A5A5A5;
                }}
                
                .wrapper {{
                    width: 75%;
                    mid-width: 600px;
                    
                    padding: 10px;
                    padding-left: 25px;
                    padding-right: 25px;
                    margin: auto;
                    
                    background-color: #0D0C1D;
                    border: 5px solid #32936F;
                    
                    color: #32936F;
                }}
                
                button {{
                    background-color: #0D0C1D;
                    border: 3px solid #32936F;
                    
                    margin: 0px auto;
                    padding: 5px;
                    display: block;
                    
                    color: #32936F;
                    font-weight: bold;
                }}
                
                button:hover {{
                    background-color: #32936F;
                    color: #0D0C1D;
                }}
                
                .noselect {{
                    -webkit-touch-callout: none; /* iOS Safari */
                    -webkit-user-select: none; /* Safari */
                    -khtml-user-select: none; /* Konqueror HTML */
                        -moz-user-select: none; /* Old versions of Firefox */
                        -ms-user-select: none; /* Internet Explorer/Edge */
                            user-select: none; /* Non-prefixed version, currently
                                                    supported by Chrome, Edge, Opera and Firefox */
                }}
            </style>
        </head>
        <body onload="generate()">
            <script>
                const response_goal = 250;
                const starters = {json.dumps(starters)};
                const chains = {json.dumps(chain)};
                
                function randomIn(array) {{
                    return array[Math.floor(Math.random() * array.length)];
                }}
                
                function generate() {{
                    let res = "";
                    
                    while(res.length < response_goal) {{
                        let curr;
                        for(curr = randomIn(starters); curr in chains; curr = randomIn(chains[curr])) {{
                            res += curr + " ";
                        }}
                        res += curr;
                    }}
                    
                    document.getElementById("quote").innerHTML = res;
                    
                    return res;
                }}
            </script>
        
            <div class="wrapper">
                <h1>Blabber - APWH Dadaism Project</h1>
                
                <h3 class="noselect" id="quote"></h3>
                <button onclick="generate()">Regenerate</button>
                
                </br>
                <p><b>Read <a target="_blank" href="https://github.com/19UV/Blabber">README</a> for explanation</b></p>
            </div>
        </body>
    </html>
"""

print("Writing Template File...")
with open("output.html", "w") as output_html:
    output_html.write(template)
print("  [DONE]")

"""
import random

res = ""
curr = random.choice(starters)
while curr in chain:
    res += curr + " "
    
    curr = random.choice(chain[curr])
res += curr

print(res)
"""