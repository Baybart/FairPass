import pandas as pd

chunk_size = 600

# Create a CSV reader with the specified chunk size
csv_reader = pd.read_csv('train_UpBound.csv', chunksize=chunk_size)

firstChunk = True
# Process each chunk and update the first row
for i, chunk in enumerate(csv_reader):
    if i == 0:
        # Set all values in the first row to 1
        chunk.iloc[0, :] = 980
    if firstChunk:
        firstChunk = False
        chunk.iloc[0, 0] = "client_id"
    # Save the modified chunk to a new CSV file
    chunk.to_csv(f'output_chunk_{i}.csv', index=False)