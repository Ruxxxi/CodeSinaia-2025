'''
import ast

###
# Loads a dataset of mountains from the disk
# The "mountains_db.tsv" contains one mountain per line, each line containing
# several fields separated by TAB: mountain name, elevantion, country where it is located and
# the ISO3 code of that country.
# The method returns two values:
# - the map associating each country to the list of {mountain, elevation} pairs from within
# - the total count of mountains in the database
def load_mountains(mountains_file):
    mountains_map = {}
    count = 0
    with open(mountains_file, "r", encoding="utf-8-sig") as data_file:
        for line in data_file.readlines():
            line_parts = line.split("\t")
            mountain_name = line_parts[0]
            mountain_elevation = ast.literal_eval(line_parts[1]) if line_parts[1] != "NULL" else None
            country_name = line_parts[2]
            country_iso = line_parts[3]
            if not country_name in mountains_map:
                mountains_map[country_name] = []
            mountains_map[country_name].append({"name":mountain_name, "elevation":mountain_elevation})
            count += 1
    return mountains_map, count


if __name__ == "__main__":
    mountains_map, count = load_mountains("mountains_db.tsv")
    print(f"Loaded {count} mountains from {len(mountains_map.keys())} countries.")

import matplotlib.pyplot as plt
mountains_by_country, count2 = load_mountains("mountains_db.tsv")
country_max_altitudes[country_name] = max(valid_elevations)
for country_name, mountains in mountains_by_country.items():
    # Filter out mountains with None elevation and find the maximum
    valid_elevations = [m["elevation"] for m in mountains if m["elevation"] is not None]
    if valid_elevations:  # Only if there are valid elevations
        country_max_altitudes[country_iso] = max(valid_elevations)

# Extract countries and altitudes for the chart
countries = list(country_max_altitudes.keys())
max_altitudes = list(country_max_altitudes.values())
plt.figure(figsize=(15,8))
plt.bar(countries, max_altitudes, color='skyblue', edgecolor='navy')
plt.xlabel('Country (ISO Code)')
plt.ylabel('Highest Altitude (meters)')
plt.title('Highest Mountain Altitude by Country')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()'''

import ast
import matplotlib.pyplot as plt

def load_mountains(mountains_file):
    mountains_map = {}  # key = ISO code, value = list of mountains
    count = 0
    with open(mountains_file, "r", encoding="utf-8-sig") as data_file:
        for line in data_file.readlines():
            line_parts = line.strip().split("\t")
            if len(line_parts) < 4:
                continue  # skip malformed lines
            mountain_name = line_parts[0]
            mountain_elevation = ast.literal_eval(line_parts[1]) if line_parts[1] != "NULL" else None
            country_name = line_parts[2]
            country_iso = line_parts[3]

            if country_iso not in mountains_map:
                mountains_map[country_iso] = []
            mountains_map[country_iso].append({"name": mountain_name, "elevation": mountain_elevation})
            count += 1
    return mountains_map, count

if __name__ == "__main__":
    mountains_by_country, total_mountains = load_mountains("mountains_db.tsv")
    print(f"Loaded {total_mountains} mountains from {len(mountains_by_country)} countries.")

    # Prepare data for bar chart
    country_codes = []
    mountain_counts = []

    for iso_code, mountains in mountains_by_country.items():
        country_codes.append(iso_code)
        mountain_counts.append(len(mountains))

    # Plot cerinta 5
    plt.figure(figsize=(15, 8))
    plt.bar(country_codes, mountain_counts, color='skyblue', edgecolor='navy')
    plt.xlabel('Country (ISO Code)')
    plt.ylabel('Number of Mountains')
    plt.title('Number of Mountains by Country')
    plt.xticks(rotation=90)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

#bar chart cerinta 6
