import fitz

def fill_pdf(input_pdf, output_pdf, data):
    pdf = fitz.open(input_pdf)
    for page in pdf:
        for field in page.widgets():
            if field.field_name in data:
                field.field_value = str(data[field.field_name])
                field.update()
    pdf.save(output_pdf)