import sys

try:
    from pypdf import PdfReader
except ImportError:
    try:
        from PyPDF2 import PdfReader
    except ImportError:
        print("No PDF library found.")
        sys.exit(1)

reader = PdfReader("Kola_Henrick_CV_Nov_21_2025_Final.pdf")
with open("cv_content.txt", "w") as f:
    for page in reader.pages:
        f.write(page.extract_text())
        f.write("\n")
print("Text extracted to cv_content.txt")
