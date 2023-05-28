from defillama2alpha.defillama2alpha import DefiLlama
import sys
import os

dl = DefiLlama()
# Save the original stdout
original_stdout = sys.stdout

# Delete the file
os.remove('defillama2alpha.doc')

with open('temp', 'w') as f:
    # Redirect stdout to the file
    sys.stdout = f
    help(dl)

# Reset stdout to the original value
sys.stdout = original_stdout

with open('temp', 'r') as f:
    contents = f.read()
    # Replace all "|" with empty string
    contents = contents.replace("|", "")

# Delete the temporary file
os.remove('temp')


# Replace all "---------" with : string
contents = contents.replace("\n       ----------", ":")
contents = contents.replace("\n       -------", ":")

with open('defillama2alpha.doc', 'w') as f:
    f.write(contents)
    


