# Your HTML template with placeholders

from datetime import datetime
verbose_date = datetime.now().strftime("%A, %B %d, %Y")
print(verbose_date)

html_template = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {{
  box-sizing: border-box;
}}

/* Add a gray background color with some padding */
body {{
  font-family: Arial;
  padding: 20px;
  background: #f1f1f1;
}}

/* Header/Blog Title */
.header {{
  padding: 30px;
  font-size: 40px;
  text-align: center;
  background: white;
}}

/* Create two unequal columns that floats next to each other */
/* Left column */
.leftcolumn {{   
  float: left;
  width: 75%;
}}

/* Right column */
.rightcolumn {{
  float: left;
  width: 25%;
  padding-left: 20px;
}}

/* Fake image */
.fakeimg {{
  background-color: #aaa;
  width: 100%;
  padding: 20px;
}}

/* Add a card effect for articles */
.card {{
   background-color: white;
   padding: 20px;
   margin-top: 20px;
}}

/* Clear floats after the columns */
.row:after {{
  content: "";
  display: table;
  clear: both;
}}

/* Footer */
.footer {{
  padding: 20px;
  text-align: center;
  background: #ddd;
  margin-top: 20px;
}}

/* Responsive layout - when the screen is less than 800px wide, make the two columns stack on top of each other instead of next to each other */
@media screen and (max-width: 800px) {{
  .leftcolumn, .rightcolumn {{   
    width: 100%;
    padding: 0;
  }}
}}
</style>
</head>
<body>

<div class="header">
  <h2>{title}</h2>
</div>

<div class="row">
  <div class="leftcolumn">
    <div class="card">
      <h2>{header_hook} </h2>
      <h5>{verbose_date}</h5>
      {content_hook}
      
      
    </div>
    <div class="card">
      <h2> to fill </h2>
      <p> to fill </p>
    </div>
  </div>
  <div class="rightcolumn">
    <div class="card">
      <h2>About Me</h2>
      <div class="fakeimg" style="height:100px;">Image</div>
      <p>Some text about me in culpa qui officia deserunt mollit anim..</p>
    </div>
    <div class="card">
      <h3>Popular Post</h3>
      <div class="fakeimg">Image</div><br>
      <div class="fakeimg">Image</div><br>
      <div class="fakeimg">Image</div>
    </div>
    <div class="card">
      <h3>Follow Me</h3>
      <p>Some text..</p>
    </div>
  </div>
</div>

<div class="footer">
  <h2>Footer</h2>
</div>

</body>
</html>
"""

# Variables to insert into the template
title = "My Blog ha ha "
header_hook = "why my blog"
content_hook = """Growing tomatoes offers a myriad of delights, encapsulating the joy of gardening, the taste of freshness, and the satisfaction of self-sufficiency. The process begins with the simple act of planting a seed or a small plant, an act that holds the promise of future bounty. As these plants grow, they demand care—watering, staking, and sometimes pruning—turning gardening into a daily ritual of nurturing and attentiveness.

The first delight comes with the sight of green shoots breaking through the soil, a sign of life and growth. This is quickly followed by the appearance of delicate flowers, the precursors to the fruit. The transformation of these flowers into tiny green orbs, and their gradual swelling and changing color, is a slow-motion spectacle of nature. Watching tomatoes ripen, transitioning from green to shades of yellow, orange, and finally, a deep, luscious red, is a visual feast. It's a process that teaches patience and appreciation for the slow, natural rhythms of life.

The taste of home-grown tomatoes is incomparable to those bought from a store. The sun-warmed, freshly picked fruits burst with flavor, a perfect blend of sweetness and acidity, with a depth and richness that supermarket tomatoes seldom possess. This superior taste is the result of the fruits being allowed to ripen on the vine, absorbing the sun's energy and the plant's nutrients until the very last moment. The satisfaction of eating something you've grown yourself, knowing the care and effort that went into its cultivation, adds an extra layer of enjoyment to every bite.

Growing tomatoes also allows for experimentation. There are countless varieties to choose from, each with its unique flavor, color, and size. Gardeners can explore the nuances between heirloom varieties, with their quirky shapes and vibrant colors, and the more uniform but no less delicious modern hybrids. This diversity encourages creativity in the kitchen, from fresh salads and salsas to sauces and soups.

Moreover, the act of growing tomatoes connects us to the cycle of the seasons and the environment. It fosters an understanding of the importance of weather, soil health, and pollinators in the production of our food. This connection can lead to a deeper respect for nature and a commitment to more sustainable living practices.

Finally, there's the community aspect. Gardening is often a shared activity, whether it's swapping tips with neighbors, sharing surplus produce, or teaching a younger generation how to grow their own food. The delight of growing tomatoes thus extends beyond the individual, contributing to a sense of community and shared experience.

In sum, the delights of growing tomatoes are many and varied. From the anticipation of the first sprouts to the pleasure of tasting the fruits of one's labor, gardening is a deeply rewarding endeavor. It engages the senses, fosters creativity, connects us with nature, and brings people together, making it a truly enriching experience."""

####################### text to html xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# Convert the text block to HTML format
def text_to_html(text):
    # Escape special HTML characters
    import html
    escaped_text = html.escape(text)
    
    # Convert newlines to <br> for HTML line breaks
    html_content = escaped_text.replace('\n', '<br>\n')
    
    # Wrap the content in <p> tags or any other necessary HTML formatting
    html_content = f"<p>{html_content}</p>"
    
    return html_content

# Convert your text block to HTML
formatted_html = text_to_html(content_hook)

# Example output
print(formatted_html)


# Use the format method to insert variables into the template
html_content = html_template.format(title=title, header_hook=header_hook,verbose_date=verbose_date, content_hook=formatted_html)

# Save the formatted HTML to a file
with open("pages/blog_page2.html", "w", encoding='utf-8') as file:
    file.write(html_content)
