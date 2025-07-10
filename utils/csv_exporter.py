import csv

def export_to_csv(data, path):
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Data', 'Gold Inicial', 'Gold Final', 'Ganho'])
        writer.writerows(data)
