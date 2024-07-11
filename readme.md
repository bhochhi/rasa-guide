Since Rasa doesn't support Python 3.11 yet, let's make sure we use a compatible Python version (e.g., 3.8).


1. **Install Python 3.8 Using Homebrew**:
   ```bash
   brew install python@3.8
   ```

2. **Check Installation**:
   ```bash
   python3.8 --version
   ```

3. **Create and Activate Virtual Environment**:
   ```bash
   python3.8 -m venv rasaenv
   source rasaenv/bin/activate
   ```

4. **Upgrade pip and setuptools**:
   ```bash
   pip install --upgrade pip setuptools wheel
   ```

5. **Create Constraints File**:
   - Save the following content into a file named `constraints.txt`:
     ```plaintext
     absl-py==0.9.0
     SQLAlchemy==1.3.24
     PyJWT==1.7.1
     ```

6. **Install Rasa with Constraints**:
   ```bash
   pip install rasa --constraint constraints.txt
   ```

7. **Install protobuf**:
   ```bash
   pip install protobuf==3.20.3
   ```

## following you rerun everytime you change the nlu.yml and retrain the model.

8. **Train the model **:
   ```bash
   rasa train nlu --nlu nlu.yml
   ```

9. **Explode the model**:
```bash
tar -xzvf models/nlu-20240710-234444.tar.gz -C models/
```

10. **run the service**:
```bash
python3.8 app.py
```

### input from browser: `http://127.0.0.1:5000/parse?text=i want to know routing number`
### output in json:
```json
{
  "entities": [],
  "intents": [
    {
      "confidence": 0.65,
      "name": "home_insurance"
    },
    {
      "confidence": 0.29,
      "name": "insurance_quote"
    },
    {
      "confidence": 0.03,
      "name": "account_opening"
    },
    {
      "confidence": 0.01,
      "name": "business_loan"
    },
    {
      "confidence": 0.01,
      "name": "greeting"
    }
  ],
  "text": "insurance"
}

```
