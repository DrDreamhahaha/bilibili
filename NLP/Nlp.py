from flask import Flask, render_template, request
from transformers import AutoTokenizer, AutoModelForCausalLM

# Initialize Flask application
app = Flask(__name__)

# Specify the correct model name
model_name = 'gpt2-medium'

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Define a route for the index page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get input text from the form
        input_text = request.form['input_text']

        # Encode input text
        input_ids = tokenizer.encode(input_text, return_tensors='pt')

        # Generate output
        output = model.generate(input_ids, max_length=50, num_return_sequences=1, early_stopping=True)
        generated_title = tokenizer.decode(output[0], skip_special_tokens=True)

        return render_template('index.html', input_text=input_text, generated_title=generated_title)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
