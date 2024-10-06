import pandas as pd

def generate_csv(filename='data.csv'):
    data = {
        'ID': [1, 2],
        'Name': ['Alice', 'Bob'],
        'Age': [25, 30],
        'Email': ['alice@example.com', 'bob@example.com']
    }
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"{filename} has been created.")

if __name__ == "__main__":
    generate_csv()
