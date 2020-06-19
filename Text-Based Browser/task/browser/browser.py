import sys
import os

args = sys.argv
folder = ''

if len(args) > 1:
    if not os.path.exists(args[1]):
        os.mkdir(args[1])

    folder = args[1] + '/'

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

known_sites = {'nytimes.com': nytimes_com, 'bloomberg.com': bloomberg_com}
saved_pages = {}
history = []

while True:
    url = input()

    if url == 'back':
        if len(history) == 0:
            continue
        else:
            history.pop()
            if len(history) != 0:
                print(known_sites[history.pop()])

    elif ('.' not in url and url != 'exit') and (url not in saved_pages) or url == 'blooomberg.com':
        print('Error: Incorrect URL')
        continue

    elif url == 'exit':
        sys.exit()

    elif url in saved_pages:
        with open(saved_pages[url], 'r') as f:
            web_page = f.read()
            print(web_page)

    elif url in known_sites:
        print(known_sites[url])
        file_name = url[:-url[::-1].index('.')-1]
        file_path = folder + file_name + '.txt'

        with open(file_path, 'w') as f:
            f.writelines(known_sites[url])

        saved_pages[file_name] = file_path
        history.append(url)

    # print(saved_pages)
