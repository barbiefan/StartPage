from config import Config

def container(data):
    category_prefix = '            <div class="category">\n'
    category_suffix = '            </div>\n'
    categories = []


    cat_names = data.keys()
    for catn in cat_names:
        category = category_prefix
        category += f'                <h3 class="hello">{catn}</h3>\n'
        link_names = data[catn]
        for linkn in link_names:
            category += f'                <li><a class="bm" href={data[catn][linkn]}>{linkn}</a></li>\n'
        category += category_suffix
        categories.append(category)
    
    categories_string = '\n'.join(categories)
    return(categories_string)

HTML = \
f'''
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Home</title>
	<link href="lib/bootstrap.min.css" rel="stylesheet">	
	<link href="style.css" rel="stylesheet">	
  </head>

  <body class="text-center">
      <!-- HelloText -->
	<h1 class="hello">{Config['HelloText']}</h1>
	<h1 id="time" class="timing"></h1>
	<div class="search">
		<form action="https://search.brave.com/search?q=%s&source=web" autofocus=true>
			<input class="input_box" type="text" name="q" placeholder="{Config['SearchPrompt']}">
		</form>
	</div>
        <div class="container">
{container(Config['Container'])}
        </div>
    
    <script src="script.js"></script>
  

	</body>
</html>
'''

with open('index.html', 'w') as file:
    file.write(HTML)
