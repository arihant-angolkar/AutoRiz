import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Paragraph, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def generate_student_pdf(data, output_folder):
    doc = SimpleDocTemplate(os.path.join(output_folder, f"{data['USN']}_report.pdf"), pagesize=letter)
    elements = []

    logo_path = "jcer.png"
    if os.path.exists(logo_path):
        logo = Image(logo_path, width=40, height=40)
        elements.append(logo)

    # Add college header
    college_name = "JAIN COLLEGE OF ENGINEERING AND RESEARCH"
    college_header_style = ParagraphStyle(name='CenteredHeader', alignment=1, parent=getSampleStyleSheet()['Heading1'])
    college_header = Paragraph(college_name, college_header_style)
    elements.append(college_header)
    elements.append(Spacer(1, 12))

    # Add student information
    student_info_data = [
        ["Name", data["Name"]], 
        ["USN", data["USN"]],
        ["Father's Name", data["Father's Name"]],
        ["Mother's Name", data["Mother's Name"]],
        ["Contact", data["Contact"]]
    ]
    student_info_table = Table(student_info_data, colWidths=[210, 360], rowHeights=35)
    student_info_table.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 1, colors.black),
                                           ('ALIGN', (0, 0), (-1, -1), 'LEFT')
                                           ]))
    elements.append(student_info_table)
    elements.append(Spacer(1, 12))

    # Add course data (sample)
    course_data = [["Sl_No", "Course", "Course Code", "Max Marks", "Marks Scored","Attendance"]]
    for i in range(1, 6):
        course_name_key = f"Course {i}"
        course_code_key = f" Course code {i}"
        max_marks_key = f"Max Marks  {i}"
        marks_scored_key = f"Marks Scored {i}"
        attendance_key = f"Attendance {i}"

        if course_name_key in data:
            course_row = [
                i, data[course_name_key], data.get(course_code_key, ""), 
                data.get(max_marks_key, ""), data.get(marks_scored_key, ""), 
                data.get(attendance_key, "")
            ]
            course_data.append(course_row)
        
    course_table = Table(course_data, colWidths=[50, 110, 100, 100, 100], rowHeights=45)
    course_table.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 1, colors.black),
                                     ('ALIGN', (0, 0), (-1, -1), 'LEFT')]))
    elements.append(course_table)

    doc.build(elements)
    return os.path.join(output_folder, f"{data['USN']}_report.pdf")