import os
import pandas as pd

# 📁 Source folder containing CSVs
csv_folder = r"C:\Users\Downloads\data"  # Replace with your path

# 📁 Output folder for generated MD files
md_output_folder = os.path.join(csv_folder, "converted_md")
os.makedirs(md_output_folder, exist_ok=True)

# 🔁 Convert each CSV to MD
for root, dirs, files in os.walk(csv_folder):
    for file in files:
        if file.endswith(".csv"):
            csv_path = os.path.join(root, file)
            df = pd.read_csv(csv_path)

            # Create Markdown content
            md_lines = []
            md_lines.append(f"# Converted from {file}\n")
            md_lines.append("| " + " | ".join(df.columns) + " |")
            md_lines.append("|" + " --- |" * len(df.columns))
            for _, row in df.iterrows():
                row_str = "| " + " | ".join(map(str, row.values)) + " |"
                md_lines.append(row_str)

            # Write to .md file
            md_filename = os.path.splitext(file)[0] + ".md"
            md_path = os.path.join(md_output_folder, md_filename)
            with open(md_path, "w", encoding="utf-8") as f:
                f.write("\n".join(md_lines))

            print(f"✅ Converted: {file} → {md_filename}")

print("\n🎉 All CSV files converted to Markdown!")
