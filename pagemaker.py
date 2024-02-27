import os

# Path to your 'pages' folder
pages_folder = r'C:\Users\rober\Desktop\ai-blog-writer\pages'

# Create or open the HTML file for writing
with open('list.html', 'w') as html_file:
    html_file.write('<html>\n<head>\n<title>Pages List</title>\n</head>\n<body>\n')
    html_file.write('<h1>Contents of Pages Folder</h1>\n<ul>\n')

    # Loop through each file in the pages folder
    for filename in os.listdir(pages_folder):
        # Create a clickable link for each file
        file_path = os.path.join(pages_folder, filename)
        html_file.write(f'<li><a href="{file_path}">{filename}</a></li>\n')

    html_file.write('</ul>\n</body>\n</html>')

print('HTML page created successfully.')
