# CS4221 LLM Comparer

This is a simple Flask application that demonstrates SQL queries from LLMs.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.x.
- You have a Windows/Linux/Mac machine.

## Setting Up the Application

To set up the application, follow these steps:

1. Clone the repository:

```
git clone https://github.com/joenzkc/cs4221-llm-comparer.git
```

2. Navigate to the project directory:

```
cd your-repository
```

3. Create a virtual environment:

- For Windows:
  ```
  python -m venv venv
  ```
- For macOS/Linux:
  ```
  python3 -m venv venv
  ```

4. Activate the virtual environment:

- For Windows:
  ```
  .\venv\Scripts\activate
  ```
- For macOS/Linux:
  ```
  source venv/bin/activate
  ```

5. Install the dependencies:

```
pip install -r requirements.txt
```

6. Set up the environment variables:

- Copy the `.env.example` file to `.env`:
  ```
  cp .env.example .env
  ```
- Open the `.env` file and fill in the required environment variables.

7. Initialize the database (if applicable):

```
python seed.py
```

- Note: Run this once!

8. Run the application:

```
python run.py
```

9. Access the application in your browser at [http://localhost:5000](http://localhost:5000).
