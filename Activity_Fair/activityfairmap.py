data = [
    {'number': 1, 'color': '#ff0000', 'link': 'link1.html'},
    {'number': 2, 'color': '#00ff00', 'link': 'link2.html'},
    {'number': 3, 'color': '#0000ff', 'link': 'link3.html'},
    # Add more data entries here
]

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Interactive Map</title>
<style>
    .grid-container {
        display: grid;
        grid-template-columns: repeat(10, 50px);
        grid-template-rows: repeat(10, 50px);
        gap: 5px;
    }
    .grid-item {
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 18px;
        font-weight: bold;
        color: white;
        cursor: pointer;
        text-decoration: none;
    }
</style>
</head>
<body>
<div class="grid-container">
"""

for item in data:
    html_content += f'<a href="{item["link"]}" class="grid-item" style="background-color: {item["color"]};">{item["number"]}</a>'

html_content += """
</div>
</body>
</html>
"""

with open('interactive_map.html', 'w') as f:
    f.write(html_content)
